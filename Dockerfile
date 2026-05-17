FROM python:3@sha256:89a288a9a9e9141b9f0c51744c358138da6369897792f1af3f5425e407d9529a

COPY /send-to-slack.py /

RUN pip install \
  slackclient

HEALTHCHECK CMD echo "healthcheck"

USER 1001

WORKDIR /
ENTRYPOINT ["/send-to-slack.py"]
