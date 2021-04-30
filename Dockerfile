# pull official base image
FROM python:3.9.2-alpine


# set work directory
WORKDIR /usr/src/sapience_trio

# install psycopg2 dependencies
RUN apk update \
    && apk --no-cache add --virtual build-dependencies \
     postgresql-dev gcc python3-dev musl-dev \
     jpeg-dev zlib-dev libffi-dev cairo-dev pango-dev gdk-pixbuf-dev

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY . .