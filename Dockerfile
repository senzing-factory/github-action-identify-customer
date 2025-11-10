FROM python:3@sha256:97aa8cc0b87a4a312a294d2d4d7b20f6e2a21ed6d4e64ef08c03088c4aa9890f

COPY /send-to-slack.py /

RUN pip install \
  slackclient

HEALTHCHECK CMD echo "healthcheck"

USER 1001

WORKDIR /
ENTRYPOINT ["/send-to-slack.py"]
