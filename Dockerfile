FROM python:3.6

WORKDIR /app

RUN apt-get update && apt-get install --no-install-recommends -y \
  vim-tiny \
  binutils \
  libproj-dev \
  gdal-bin \
  python3-gdal \
  && rm -rf /var/lib/apt/lists/* && pip install --upgrade pip && pip install pip-tools

COPY requirements.in /app/requirements.in
RUN pip-compile && pip install --no-cache-dir -r requirements.txt

COPY . /app
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
