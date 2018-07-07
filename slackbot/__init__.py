import json as __json
import os as __os
from slackclient import SlackClient as __SlackClient

__CONFIG_FILE = '.slackbot.json'

def bot(token, name):
    with open(__CONFIG_FILE, 'w') as f:
        f.write(__json.dumps({'token':token, 'name':name}))

def __load():
    if not __os.path.isfile(globals().get('__CONFIG_FILE')):
        print("You must first set up a bot's name and a token.")
        return None
    return __json.load(open(globals().get('__CONFIG_FILE'), 'r'))


def message(to, msg):
    __bot = __load()
    if __bot:
        __SLACK = __SlackClient(__bot.get('token'))
        return __SLACK.api_call(
                'chat.postMessage',
                channel=f'@{to}',
                text=msg,
                as_user=__bot.get('name'))