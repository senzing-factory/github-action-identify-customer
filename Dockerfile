FROM python:3@sha256:8676e2e7a07b736aeea297a13a42ab7b235940623a7fcd3815c336662ffe33c8

COPY /send-to-slack.py /

RUN pip install \
  slackclient

HEALTHCHECK CMD echo "healthcheck"

USER 1001

WORKDIR /
ENTRYPOINT ["/send-to-slack.py"]
