FROM python:latest

COPY /send-to-slack.py /

RUN pip install \
  slackclient
  
WORKDIR /
cat /github/workspace/.github/CODEOWNERS
ENTRYPOINT ["/send-to-slack.py"]
