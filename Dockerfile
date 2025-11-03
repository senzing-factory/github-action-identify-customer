FROM python:3@sha256:934873f1360893d07afe0d25b99af46640e916a5900f1677fb86e41f73920253

COPY /send-to-slack.py /

RUN pip install \
  slackclient

HEALTHCHECK CMD echo "healthcheck"

USER 1001

WORKDIR /
ENTRYPOINT ["/send-to-slack.py"]
