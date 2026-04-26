FROM python:3@sha256:4bdca440e7381ba0d706e3718714c1a4cde97b460d8411c1af9c704bba1fba0f

COPY /send-to-slack.py /

RUN pip install \
  slackclient

HEALTHCHECK CMD echo "healthcheck"

USER 1001

WORKDIR /
ENTRYPOINT ["/send-to-slack.py"]
