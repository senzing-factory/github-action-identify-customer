#! /usr/bin/env python3

import json
import os
import urllib.request

import slack

slack_bearer_token = os.getenv("TOKEN")
repo = os.getenv("REPO_URL")
issue_number = os.getenv("NUMBER")
maker = os.getenv("CREATOR")
title = os.getenv("TITLE")
slack_string = os.getenv("SLACK_HASHES")
slack_channel = "community-notifications"
repo_url = "https://github.com/{}".format(repo)
issue = "https://github.com/{}/issues/{}".format(repo, issue_number)
user_url = "https://github.com/{}".format(maker)
result = []

codeowners_url = "https://raw.githubusercontent.com/{}/main/.github/CODEOWNERS".format(
    repo
)
try:
    codeowners = urllib.request.urlopen(codeowners_url)
except BaseException:
    codeowners_url = (
        "https://raw.githubusercontent.com/{}/main/.github/CODEOWNERS".format(repo)
    )
    codeowners = urllib.request.urlopen(codeowners_url)

SENZING_GITHUB_SLACK_MAP = json.loads(str(slack_string))

codeowners = urllib.request.urlopen(codeowners_url)

for line in codeowners:
    decoded_line = line.decode("utf-8")
    uncommented_line = decoded_line.split("#")[0]
    split_line = uncommented_line.split()
    for split in split_line:
        key = split.replace("@", "")
        if key in SENZING_GITHUB_SLACK_MAP.keys():
            values = SENZING_GITHUB_SLACK_MAP.get(key)
            if type(values) != list:
                values = [values]
            for value in values:
                if value not in result:
                    result.append(value)

slack_message = (
    "Customer created GitHub issue:\n*Repository:* <"
    "{0}|{1}>\n      *Customer*: <"
    "{2}|{3}>\n      *Issue:* <"
    "{4}|{5}>\n      *Attention*: ".format(
        repo_url, repo, user_url, maker, issue, title
    )
)

for value in result:
    slack_message = slack_message + "<@" + value + ">"

# Create a client that communicates with Slack.

slack_client = slack.WebClient(token=slack_bearer_token)

response = slack_client.chat_postMessage(channel=slack_channel, text=slack_message)
