# pull the official base image
FROM python:3.8-alpine

# Create working dir
RUN mkdir /app

# set work directory
WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip 
COPY website/requirements.txt /app
RUN pip install --no-cache-dir -r requirements.txt

# copy project
COPY website /app

EXPOSE 8000

# run entrypoint.sh
ENTRYPOINT ["/app/entrypoint-dev.sh"]