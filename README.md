# BBC News Crawler

## Functionality:
1. Crawls http://bbc.com/news
2. Store the data on MongoDB
3. Provides api endpoint to get all content with pagination
4. Search contents with given query

## Installation
1. Clone the project and get into the project directory
2. Create a virtualenv
3. Install pacakages from requirement.txt `pip install -r requirements.txt`
4. Run this command `export APP_SETTINGS="config.ProductionConfig"`
5. Run these command `export MONGO_URI="your mongo uri"`, `export MONGO_DBNAME="your mongodb name"`
6. Run this command `export MERCURY_API_KEY='your mercury api key'`
7. Run this command to crawl the bbc.com, `scrapy crawl bbc_crawler`
8. Run the server using this command `python manage.py runserver`
9. Browse `localhost:5000`
10. To run the tests, execute this command `python manage.py test`

## API Endpoint

### `http://localhost:5000/`
This will fetch all the content on the db
You can do pagination with `page` and `limit` parameter.
Default value `page=1`, `limit=30`

### `http://localhost:5000/search?q=test`
This will fetch all the content where the query parameter `q`'s value exist
You can do pagination with `page` and `limit` parameter.
Default value `page=1`, `limit=30`

## Server Information
You can check the API endpoint from here: https://fast-shore-63416.herokuapp.com/
Example: https://fast-shore-63416.herokuapp.com/search?q=syria
