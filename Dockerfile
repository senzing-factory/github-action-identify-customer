FROM python:latest

COPY /send-to-slack.py /

RUN pip install \
  slackclient
  
WORKDIR /
ENTRYPOINT ["/send-to-slack.py"]
