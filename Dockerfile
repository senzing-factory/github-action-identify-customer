FROM python:3@sha256:511f025a0718f01b977d5ad572bc431745b31887ceccc538c85b87e82ad2956f

COPY /send-to-slack.py /

RUN pip install \
  slackclient

HEALTHCHECK CMD echo "healthcheck"

USER 1001

WORKDIR /
ENTRYPOINT ["/send-to-slack.py"]
