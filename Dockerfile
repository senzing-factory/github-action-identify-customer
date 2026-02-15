FROM python:3@sha256:151ab3571dad616bb031052e86411e2165295c7f67ef27206852203e854bcd12

COPY /send-to-slack.py /

RUN pip install \
  slackclient

HEALTHCHECK CMD echo "healthcheck"

USER 1001

WORKDIR /
ENTRYPOINT ["/send-to-slack.py"]
