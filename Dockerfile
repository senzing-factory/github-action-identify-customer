FROM python:3@sha256:61c06383336ec271f3ff69ceae4a4f011faa6f78638fefad00a1d82e807e5c39

COPY /send-to-slack.py /

RUN pip install \
  slackclient

HEALTHCHECK CMD echo "healthcheck"

USER 1001

WORKDIR /
ENTRYPOINT ["/send-to-slack.py"]
