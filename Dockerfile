FROM python:3@sha256:61346539f7b26521a230e72c11da5ebd872924745074b19736e7d65ba748c366

COPY /send-to-slack.py /

RUN pip install \
  slackclient

HEALTHCHECK CMD echo "healthcheck"

USER 1001

WORKDIR /
ENTRYPOINT ["/send-to-slack.py"]
