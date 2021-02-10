FROM python:3.7-alpine

# Recommended for the use of python with docker
ENV PYTHONUNBUFFERED 1
# ENV PATH="/scripts:${PATH}"

# From to
COPY ./requirements.txt /requirements.txt
RUN apk add --update --no-cache postgresql-client jpeg-dev
RUN apk add --update --no-cache --virtual .tmp-build-deps \
        gcc libc-dev linux-headers postgresql-dev musl-dev zlib zlib-dev
RUN pip install -r /requirements.txt
RUN apk del .tmp-build-deps

RUN mkdir /app
COPY ./app /app
WORKDIR /app
# COPY ./scripts /scripts

# RUN chmod +x /scripts/*

RUN mkdir -p /vol/web/media
RUN mkdir -p /vol/web/static

RUN adduser -D user
RUN chown -R user:user /vol/
RUN chmod -R 755 /vol/web
USER user

# CMD ["entrypoint.sh"]