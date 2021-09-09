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
slack_channel = "playground"
repo_url = "https://github.com/" +repo
issue = "https://github.com/" +repo + "/issues/" + issue_number
user_url = "https://github.com/" + maker
codeowners_url = "https://raw.githubusercontent.com/" + repo + "/master/.github/CODEOWNERS"
result = []

SENZING_GITHUB_SLACK_MAP = json.loads(slack_string)

codeowners = urllib.request.urlopen(codeowners_url)

for line in codeowners:
        decoded_line = line.decode('utf-8')
        uncommented_line = decoded_line.split("#")[0]
        split_line = uncommented_line.split()
        for split in split_line:
            key = split.replace("@","")
            if key in SENZING_GITHUB_SLACK_MAP.keys():
                values = SENZING_GITHUB_SLACK_MAP.get(key)
                if type(values) != list:
                    values = [values]
                for value in values:
                    if not value in result:
                        result.append(value)
    
slack_message = "Customer created GitHub issue:\n*Repository:* <" + repo_url + "|" + repo + ">\n    *Customer*: <" + user_url + "|" + maker + ">\n    *Issue:* <" + issue + "|" + title + ">\n    *Attention*: "

for value in result:
    slack_message = slack_message + "<@" + value + ">"
    
# Create a client that communicates with Slack.

slack_client = slack.WebClient(token=slack_bearer_token)

response = slack_client.chat_postMessage( channel=slack_channel, text=slack_message )
