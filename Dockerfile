FROM python:3@sha256:37cba1153c7a3cd4477640ce0f976f7460308f812bc29d7149532e352a97ac8b

COPY /send-to-slack.py /

RUN pip install \
  slackclient

HEALTHCHECK CMD echo "healthcheck"

USER 1001

WORKDIR /
ENTRYPOINT ["/send-to-slack.py"]
