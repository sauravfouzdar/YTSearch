
# YTSearch

API server to fetch YT videos for given search-query[cricket, football etc.] at a periodic interval using YT API


## Tech Stack

- Django
- Django-Restframework
- Sqlite
- Youtube API
- Docker

## Application Structure

```
|____fampay
| |____config
|____videos
| |____migrations
|
|____
|____requirements.txt
```
## Running the server locally

 * Install python3.8
 * Clone this repo
 * create virtual environment
   - apt-get install python3-venv  
   - python3 -m venv environment_name
   - activate virtual environment `source djangoenv/bin/activate`   or `workon environment_name`
 * Intall dependencies:
> pip install -r requirements.txt
 * Run the server:
> python manage.py runserver

### API Endpoints

List of available routes:

**Video routes**:\
`GET api/v1/test` - get api to test server\
`POST api/v1/search-video` - api to getVideo from YT for given searchQuery\
`GET api/v1/video` - API to fetch video from Db in reverse chrono order\


## Contributors
Saurav Fouzdar and amazing developers who created django,django_rest_framework

