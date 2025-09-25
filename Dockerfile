FROM python:3@sha256:2deb0891ec3f643b1d342f04cc22154e6b6a76b41044791b537093fae00b6884

COPY /send-to-slack.py /

RUN pip install \
  slackclient

HEALTHCHECK CMD echo "healthcheck"

USER 1001

WORKDIR /
ENTRYPOINT ["/send-to-slack.py"]
