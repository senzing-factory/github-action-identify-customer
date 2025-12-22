FROM python:3@sha256:492b292a9449d096aefe5b1399cc64de53359845754da3e4d2539402013c826b

COPY /send-to-slack.py /

RUN pip install \
  slackclient

HEALTHCHECK CMD echo "healthcheck"

USER 1001

WORKDIR /
ENTRYPOINT ["/send-to-slack.py"]
