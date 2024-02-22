FROM python:3.8-alpine3.16

WORKDIR /usr/src/app



RUN apk update \
    && apk add postgresql-dev gcc python3-dev zlib-dev jpeg-dev musl-dev ffmpeg libffi-dev libressl-dev openssl-dev  \
    freetype-dev libjpeg freetype-dev libjpeg-turbo-dev libjpeg-turbo gettext gettext-dev cairo-dev pango-dev fontconfig ttf-dejavu \
    pango cairo gdk-pixbuf py3-cffi py3-pillow nodejs npm py-pip
RUN npm install -g mjml@4.6.3

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY . .
