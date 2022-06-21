FROM python:latest as env

# base
RUN apt-get update
RUN apt-get install git -y
RUN apt-get install mariadb-client default-libmysqlclient-dev -y

RUN pip install pipenv

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY Pipfile Pipfile.lock ./
RUN pipenv lock --requirements > requirements.txt
RUN pip install -r requirements.txt

# start dev env
FROM env as dev
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
