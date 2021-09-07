#! /usr/bin/env python3

import urllib
import slack
import os 
import json

slack_bearer_token = os.getenv('TOKEN')
repo = os.getenv('REPO_URL')
issue_number = os.getenv('NUMBER')
maker = os.getenv('CREATOR')
title = os.getenv('TITLE')
slack_string = os.getenv('SLACK_HASHES')
slack_channel = "Playground"
repo_url = "https://github.com/" +repo
issue = "https://github.com/" +repo + "/issues/" + issue_number
user_url = "https://github.com/" + maker
codeowners_url = "https://raw.githubusercontent.com/" + repo + "/master/.github/CODEOWNERS"
codeowners = "{ "
count = 1
hash_map = json.loads(slack_string)
file = urllib.request.urlopen(codeowners_url)

for line in file:
    decoded_line = line.decode("utf-8")
    if("@" in decoded_line):
      name = decoded_line.split("@",1)[1]
      codeowners = codeowners + "\"owners" + str(count) + "\":" + "\""+ name.strip() + "\","
      count+=1

codeowners = codeowners[:-1]
codeowners = codeowners + "}"

codeowners_json = json.loads(codeowners)

slack_message = "Customer created GitHub issue:\n*Repository:* <" + repo_url + "|" + repo + ">\n  *Customer*: <" + user_url + "|" + maker + ">\n  *Issue:* <" + issue + "|" + title + ">\n  *Attention*: "

count = 1
for name in codeowners_json:
  value = codeowners_json[name]
  
  if "/" in value:
    for ID in hash_map[value]:
      if ID not in slack_message:
        slack_message = slack_message + "<@" + ID + ">"
        
  else:
    slack_message = slack_message + "<@" + hash_map[value] + ">"


# Create a client that communicates with Slack.

slack_client = slack.WebClient(token=slack_bearer_token)

response = slack_client.chat_postMessage( channel=slack_channel, text=slack_message )
