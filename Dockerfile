FROM python:3.6

WORKDIR /app

RUN apt-get update && apt-get install --no-install-recommends -y \
  vim-tiny \
  binutils \
  libproj-dev \
  gdal-bin \
  python3-gdal \
  && rm -rf /var/lib/apt/lists/* && pip install pip-tools

COPY . /app
RUN pip-compile && pip install --no-cache-dir -r requirements.txt


ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
