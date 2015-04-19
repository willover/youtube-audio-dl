YouTube Audio Downloader
========================

A Django web application for extracting the audio from a YouTube video and converts it to MP3 that a user can download.

**Live Site:** http://www.youtubeadl.com


Technology Stack
----------------

- Python 2.7
- Django 1.8
- Twitter Bootstrap 3
- PostgreSQL
- Nginx
- Gunicorn
- Celery
- Redis
- Supervisor
- Virtualenv


Getting Started with Docker and Docker Compose for Local Development
--------------------------------------------------------------------

### Install Docker

https://docs.docker.com/installation/

### Install Docker Compose

http://docs.docker.com/compose/install/

### Start the Docker containers

In the project root (where the `docker-compose.yml` file is located), run:

`docker-compose up -d`

This will start the containers in the background (run `docker-compose --help` to see all available options).

### Run the Django database migrations

`docker-compose run django python manage.py migrate`

To run any management command inside the docker container, simply prepend `docker-compose run django`.

### View the logs

`docker-compose logs`