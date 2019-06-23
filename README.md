# HeyJobs Python Assessment Task by Christian Granados

* Runs a python application which:
   * scrapes data from heyjobs website
   * stores results in the database (Postgres)

#### Database
The scraped data is stored in the database table public.ads
with the structure:
```
id | uid | title
```

### Running the Task
```
docker-compose run --rm start_dependencies
docker-compose up scraper
```
