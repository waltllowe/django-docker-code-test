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
RUN pip install -r cloud_test_app/requirements.txt
RUN pip install gunicorn

# TODO: set entrypoint and command (see entrypoint.sh)

RUN chmod +x /opt/entrypoint.sh
ENTRYPOINT ["/opt/entrypoint.sh"]
CMD ["--start-service"]