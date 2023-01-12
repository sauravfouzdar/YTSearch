
# YTSearch

API server to fetch YT videos for given search-query[cricket, football etc.] using distributed task processing on YT API using celery/rabbitMQ
 
## Scalibility 

- The App can be scaled horizontally using Postgres
- Pagination
- Bulk create to optimize number of write queries.
- Use of distributed task processing to fetch videos asyncronously using Celery, RabbitMQ/Redis for high scalibility. 
- In-built logging


## Tech Stack

- Django
- Django-Restframework
- ~~Sqlite~~ Postgres
- Youtube API
- Docker
- Celery
- RabbitMQ/Redis

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


Docker Setup
---
 * Install [docker compose](https://docs.docker.com/compose/install/)
 * Run docker:
> Create logs foleder with `app.log` and `error.log` file inside root directory

> docker-compose build

> docker-compose up
 * To check the server, open `http://localhost:8000/`


### API Endpoints

List of available routes:

**Video routes**:\
`GET api/v1/test` - get api to test server\
`POST api/v1/search-video` - api to getVideo from YT for given searchQuery\
`GET api/v1/video` - API to fetch video from Db in reverse chrono order\
`GET api/v1/video?page_number=1&page_size=4` using pagination\
`GET api/v1/video?title=cricket&description=playing` search api with title & description


## Approach for bonus questions
* Adding api keys to limit request with single APIKey
  - Create a APIkey table that stores `UserId`,`APIKey`,`requests`
  - APIKey will be generated using `APIKeyGenerator` Service
  - Each time user send request using key, `requests` field will be decremented by 1.
  - to generate APIKey, will have to implement `JWT Authentication`, to allow user create API Key if `Authenticated`
  - When `100 requests` are exhausted, Will search for next APIKey with `UserId`, and `requests` field with greater than zero  

* Skipping the second second bonus question, since it's optional
* Optimizing API search for partial match using title & description 
  - Here I need to create a `Custom Search Filter` linear string matching
  - Algorithm(Naive approach):
    - take search query as tokens/words
    - store targeted model field in list where each element of list contains one word
    - and do `bruteForce` search for each word 
    - Time Complexity : O(n*m) ,where n = length_of_search_query/total_words/token, m = length_of_model_field/total words
    - Space Complexity : O(m), extra space required to stored query in RAM, here ignoring model field space as it is stored in Disk/Database


## Contributors
Saurav Fouzdar and amazing developers who created django,django_rest_framework





