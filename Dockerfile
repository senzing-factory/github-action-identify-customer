FROM python:3@sha256:78ad0471881f0232093c9e6edf58addade7bf106377732e0790c0f0c914b3b7b

COPY /send-to-slack.py /

RUN pip install \
  slackclient

HEALTHCHECK CMD echo "healthcheck"

USER 1001

WORKDIR /
ENTRYPOINT ["/send-to-slack.py"]
