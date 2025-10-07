FROM python:3@sha256:fe841081ec55481496a4ab25e538833741295d57d2abdec8d38d74d65fb4715b

COPY /send-to-slack.py /

RUN pip install \
  slackclient

HEALTHCHECK CMD echo "healthcheck"

USER 1001

WORKDIR /
ENTRYPOINT ["/send-to-slack.py"]
