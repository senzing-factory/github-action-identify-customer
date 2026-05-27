FROM python:3@sha256:250e5c97be05e1eb2272fbdbd810dfd638f9012e1e6f65c99390ad3239943a08

COPY /send-to-slack.py /

RUN pip install \
  slackclient

HEALTHCHECK CMD echo "healthcheck"

USER 1001

WORKDIR /
ENTRYPOINT ["/send-to-slack.py"]
