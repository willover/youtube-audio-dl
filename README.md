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
- RabbitMQ
- Supervisor
- Virtualenv


Getting Started with Docker and Docker Compose for Local Development
--------------------------------------------------------------------

### Install Docker

https://docs.docker.com/installation/

### Install Docker Compose

http://docs.docker.com/compose/install/

### Install the Python packages required by the project via pip

In the project root (where the `docker-compose.yml` file is located), run:

```
docker-compose run django pip install -r requirements.txt
```

To run any command inside the Django Docker container, simply prepend `docker-compose run django`.

### Start the Docker containers

```
docker-compose up -d
```

This will start the containers in the background.

### Run the Django database migrations

```
docker-compose run django python manage.py migrate
```

### View the logs

```
docker-compose logs
```