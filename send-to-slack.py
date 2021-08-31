#! /usr/bin/env python3

import slack
import os 

slack_bearer_token = os.getenv('TOKEN')
repo = os.getenv('REPO_URL')
issue_number = os.getenv('NUMBER')
maker = os.getenv('CREATOR')
title = os.getenv('TITLE')
slack_channel = "Playground"
repo_url = "https://github.com/" +repo
issue = "https://github.com/" +repo + "/issues/" + issue_number

# Create a client that communicates with Slack.

slack_client = slack.WebClient(token=slack_bearer_token)

slack_message = ">New customer submitted issue \"" + title + "\">/n Created by " +  maker + " in <" + repo_url + "|" + repo + "> issue <#" + issue + "|" + issue_number + ">"

response = slack_client.chat_postMessage(
                channel=slack_channel,
                text=slack_message
            )
