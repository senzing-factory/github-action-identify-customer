#! /usr/bin/env python3

import slack
import os 

slack_bearer_token = os.getenv('TOKEN')
slack_channel = "Playground"
repo = os.getenv('REPO_URL')
issue_number = os.getenv('NUMBER')
repo_url = "https://github.com/" +repo
issue = "https://github.com/" +repo + "/issues/" + issue_number

print(issue)
print(os.getenv('BOOL'))
print(os.getenv('CREATOR'))
print(os.getenv('TITLE'))


# Create a client that communicates with Slack.

slack_client = slack.WebClient(token=slack_bearer_token)

slack_message = "New customer submitted issue in <" + repo_url + "|" + repo+ ">\n issue number <" + issue + "|" + issue_number + ">"

response = slack_client.chat_postMessage(
                channel=slack_channel,
                text=slack_message
            )
