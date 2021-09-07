#! /usr/bin/env python3
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
codeowners_url = "https://raw.githubusercontent.com/" + repo_url + "/master/.github/CODEOWNERS"
printmap = "{"
codeowners = "{ "
count = 1

print(codeowners_url)

hash_json = json.loads(slack_string)
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

count = 1
for key in codeowners_json:
  value = codeowners_json[key]
  if( "/" in value):
    group = value
    
for key in codeowners_json:
  value = codeowners_json[key]
  if (value not in hash_map[group] and "/" not in value):
    printmap = printmap + "\"owners" + str(count) + "\":" + "\"" + value + "\","
    count+=1

for key in hash_map[group]:
  printmap = printmap + "\"owners" + str(count) + "\":" + "\""+ key +"\","
  count+=1
  
  
printmap = printmap[:-1]
printmap = printmap + "}"
user_json = json.loads(printmap)

for key in user_json:
  value = user_json[key]
  print(hash_map[value])


# Create a client that communicates with Slack.

slack_client = slack.WebClient(token=slack_bearer_token)

#slack_message = ">New customer submitted issue \"" + title + "\">/n Created by " +  maker + " in <" + repo_url + "|" + repo + "> issue <#" + issue + "|" + issue_number + ">"

slack_message = "Customer created GitHub issue:\n*Repository:* <" + repo_url + "|" + repo + ">\n  *Customer*: <" + user_url + "|" + maker + ">\n  *Issue:* <" + issue + "|" + title + ">\n  *Attention*: "

for key in user_json:
 slack_message = "<@" + key + ">"
  
print(slack_message)
#response = slack_client.chat_postMessage( channel=slack_channel, text=slack_message )
