FROM python:3@sha256:d29cf0828933ed271be9234ca2c2d578c16f2911451418aacc4525ac04ac7114

COPY /send-to-slack.py /

RUN pip install \
  slackclient

HEALTHCHECK CMD echo "healthcheck"

USER 1001

WORKDIR /
ENTRYPOINT ["/send-to-slack.py"]
