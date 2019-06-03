# Stage 1.1 - Compile needed python dependencies
FROM alpine:3.7 AS build
RUN apk --no-cache add \
    gcc \
    musl-dev \
    pcre-dev \
    linux-headers \
    postgresql-dev \
    python3 \
    python3-dev \
    # libraries installed using git
    git \
    # lxml dependencies
    libxslt-dev \
    # pillow dependencies
    jpeg-dev \
    openjpeg-dev \
    zlib-dev

RUN pip3 install virtualenv
RUN virtualenv /app/env

WORKDIR /app

COPY ./requirements.txt /app/
RUN /app/env/bin/pip install -r requirements.txt
#RUN /app/env/bin/pip install uwsgi
RUN /app/env/bin/pip install daphne

# Stage 1.2 - Compile needed frontend dependencies
RUN apk --no-cache add \
    # node.js
    nodejs \
    nodejs-npm \
    python

# COPY ./build /app/build
COPY ./src /app/src
# COPY ./*.js /app/
COPY ./*.json /app/

RUN npm install
# See: https://stackoverflow.com/questions/22115400/why-do-we-need-to-install-gulp-globally-and-locally
# RUN npm install -g gulp
# RUN npm install gulp
# RUN gulp build

# Stage 2 - Build docker image suitable for execution and deployment
FROM alpine:3.7
RUN apk --no-cache add \
    ca-certificates \
    mailcap \
    musl \
    pcre \
    postgresql \
    python3 \
    # lxml dependencies
    libxslt \
    # pillow dependencies
    jpeg \
    openjpeg \
    zlib \
    # frontend runtime requirement
    nodejs \
    nodejs-npm

COPY --from=build /app/src /app/src
COPY ./bin/docker_start.sh /start.sh
COPY --from=build /app/node_modules /app/node_modules
RUN mkdir /app/log

COPY --from=build /app/env /app/env

ENV PATH="/app/env/bin:${PATH}"
WORKDIR /app

ENV DJANGO_SETTINGS_MODULE=zac.conf.docker

ARG SECRET_KEY=dummy

# Run collectstatic, so the result is already included in the image
RUN python src/manage.py collectstatic --noinput

EXPOSE 8080
CMD ["/start.sh"]
