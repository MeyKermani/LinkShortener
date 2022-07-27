from __main__ import app, api
from views import URLShortener, redirect_url
""" Mapping urls to view function/classes """
api.add_resource(URLShortener, '/shorten')
app.add_url_rule('/<short_id>', 'redirect_url', view_func=redirect_url)
