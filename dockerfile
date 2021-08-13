FROM python:alpine
COPY entrypoint.sh /opt/
COPY cloud_test_app /opt/cloud_test_app
COPY etc/conf.py /etc/cloud_test/
RUN apk add --no-cache \
      bash \
      gcc \
      curl \
      g++ \
      libstdc++ \
      linux-headers \
      musl-dev \
      postgresql-dev \
      mariadb-dev;

# TODO: install django app requirements and gunicorn

EXPOSE 8000
WORKDIR /opt

# TODO: set entrypoint and command (see entrypoint.sh)
