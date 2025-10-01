FROM python:3@sha256:4382b09718538b99754cd19b0634d3a78419593f6ad8a07bf5e8b4112a9a6c5c

COPY /send-to-slack.py /

RUN pip install \
  slackclient

HEALTHCHECK CMD echo "healthcheck"

USER 1001

WORKDIR /
ENTRYPOINT ["/send-to-slack.py"]
