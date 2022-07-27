# LinkShortener
A very simple URL shortener API implemented using flask
## This projects uses flask and sqlite as the database.
You can run the project by simply cloning it and run ```python app.py```
## Examples
- request: ```curl --location --request POST 'http://127.0.0.1:5000/shorten' \
--header 'Content-Type: application/json' \
--data-raw '{"URL": "https://google.com/kjbcdnkjqebdkjeqbjkcbew;kjvbwe"}' ```
- response: ``` {
    "url": "https://google.com/kjbcdnkjqebdkjeqbjkcbew;kjvbwe",
    "shor_url": "http://127.0.0.1:5000/6wC0Rzqh"
} ```
