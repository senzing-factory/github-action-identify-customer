FROM python:3@sha256:049247cbb7ce998685d780c9d5325781a7429bc6693bbfab86bcb8e36e7a059e

COPY /send-to-slack.py /

RUN pip install \
  slackclient

HEALTHCHECK CMD echo "healthcheck"

USER 1001

WORKDIR /
ENTRYPOINT ["/send-to-slack.py"]
