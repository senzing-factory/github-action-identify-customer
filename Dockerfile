FROM python:3@sha256:5b95b240f2db781f34a5da81e6e2301378495b3ab78d689df325c937be267e1c

COPY /send-to-slack.py /

RUN pip install \
  slackclient

HEALTHCHECK CMD echo "healthcheck"

USER 1001

WORKDIR /
ENTRYPOINT ["/send-to-slack.py"]
