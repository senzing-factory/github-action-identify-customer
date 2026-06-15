FROM python:3@sha256:6f473f84b09fccf411d4875e19e9e2796b59d6b3c722463d2963384a43e59f39

COPY /send-to-slack.py /

RUN pip install \
  slackclient

HEALTHCHECK CMD echo "healthcheck"

USER 1001

WORKDIR /
ENTRYPOINT ["/send-to-slack.py"]
