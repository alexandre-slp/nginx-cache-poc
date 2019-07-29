# Image
FROM python:3.6.8-alpine

# Installing necessary components
RUN apk add musl-dev gcc tzdata

# Adjust Time Zone
ENV TZ=America/Sao_Paulo
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# Add files
COPY . /rpaas_test

# Go to working directory
WORKDIR /rpaas_test

# Install requirements
RUN pip install --upgrade pip --index-url='https://artifactory.globoi.com/artifactory/api/pypi/pypi/simple/'
RUN pip install -r requirements.txt --index-url='https://artifactory.globoi.com/artifactory/api/pypi/pypi/simple/'