FROM python:3.9.17-slim-bullseye

ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

ENV DockerHOME=/home/app
RUN mkdir -p $DockerHOME  
WORKDIR $DockerHOME   

COPY ./requirements.txt .

RUN apt-get update && apt-get install -y \
  build-essential \
  netcat

RUN pip install --upgrade pip && \
  pip install -r requirements.txt

COPY . .

COPY ./entrypoint.sh .
RUN sed -i 's/\r$//g' ${DockerHOME}/entrypoint.sh
RUN chmod +x ${DockerHOME}/entrypoint.sh

ENTRYPOINT ["sh", "/home/app/entrypoint.sh"]