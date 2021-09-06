#! /usr/bin/env python3

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
codeowners = "https://raw.githubusercontent.com/" + repo_url + "master/.github/CODEOWNERS"


file = urllib.request.urlopen(codeowners)

for line in file:
	decoded_line = line.decode("utf-8")
	echo(decoded_line)
    
    
hash_json = json.loads(slack_string)

slack_users = has_json['Senzing/senzing-engineering']
# Create a client that communicates with Slack.

slack_client = slack.WebClient(token=slack_bearer_token)

#slack_message = ">New customer submitted issue \"" + title + "\">/n Created by " +  maker + " in <" + repo_url + "|" + repo + "> issue <#" + issue + "|" + issue_number + ">"

slack_message = "Customer created GitHub issue:\n*Repository:* <" + repo_url + "|" + repo + ">\n  *Customer*: <" + user_url + "|" + maker + ">\n  *Issue:* <" + issue + "|" + title + ">\n  *Attention*: "

for user in slack_users:
  for ID in user:
    slack_message = slack_message + "" + ID + ""
  
response = slack_client.chat_postMessage(
                channel=slack_channel,
                text=slack_message
            )
