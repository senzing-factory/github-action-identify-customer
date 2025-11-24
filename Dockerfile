FROM python:3@sha256:edf6433343f65f94707985869aeaafe8beadaeaee11c4bc02068fca52dce28dd

COPY /send-to-slack.py /

RUN pip install \
  slackclient

HEALTHCHECK CMD echo "healthcheck"

USER 1001

WORKDIR /
ENTRYPOINT ["/send-to-slack.py"]
