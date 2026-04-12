FROM python:3@sha256:8428c32065df71d5a7763099ccb8ee215314129b50d395f95ad589151887d52f

COPY /send-to-slack.py /

RUN pip install \
  slackclient

HEALTHCHECK CMD echo "healthcheck"

USER 1001

WORKDIR /
ENTRYPOINT ["/send-to-slack.py"]
