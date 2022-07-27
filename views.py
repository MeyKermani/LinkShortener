from datetime import datetime
from typing import Any, Tuple, Dict, Union
from flask_restful import Resource
from app import db
from helpers import generate_short_id
from flask import request, redirect
from models import ShortUrls
from validations import is_valid_url
from exceptions import UnableToCreateShorterURL, ErrorInSavingTheLinkInDatabase, ErrorInFindingTheOriginalURL
from decouple import config


class URLShortener(Resource):
    def post(self, *args: Any, **kwargs: Any) -> Tuple[Dict[str, Union[str, Any]], int]:
        """Creates a short link for the given URL in the request"""
        url = request.json.get('URL', None)
        short_id = request.json.get('custom_id', None)
        # Check if custom_id has already been used and exist in the database.
        if short_id and ShortUrls.query.filter_by(short_id=short_id).first() is not None:
            return {'message': 'Conflict: Please enter different custom id!'}, 409
        # Check if URL parameter has been passed during the API call.
        if not url:
            return {'message': 'BAD Request: URL is a mandatory field'}, 400
        # Check if URL in the request in a valid URL
        if not is_valid_url(url):
            return {'message': 'Unprocessable Entity: URL is not valid'}, 422
        # Check if the length of created URL is not longer than the original URL
        if not short_id:
            short_id = generate_short_id()
            if len(request.host_url + short_id) > len(url):
                raise UnableToCreateShorterURL("Couldn't create a shorter link")
        # Creates new ShortUrl object in order to save it to database in the next phase.
        new_link = ShortUrls(
            original_url=url, short_id=short_id, created_at=datetime.now())
        try:
            # Saves the created ShortUrl object into the database.
            db.session.add(new_link)
            db.session.commit()
            short_url = request.host_url + short_id
            return {'url': url, 'shor_url': short_url}, 201
        except ErrorInSavingTheLinkInDatabase as ex:
            pass

    def get(self, *args: Any, **kwargs: Any) -> Tuple[Dict[str, Union[str, Any]], int]:
        """ Avoids sending GET request to this endpoint and responses properly with a suitable standard status code"""
        return {'message': 'METHOD NOT ALLOWED: cant accept get requests'}, 405


def redirect_url(short_id):
    """Redirects short URL requests to the original URL"""
    link = ShortUrls.query.filter_by(short_id=short_id).first()
    if link:
        return redirect(link.original_url)
    else:
        raise ErrorInFindingTheOriginalURL()
