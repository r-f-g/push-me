# slack-bot
Slack bot for notifications from server.

[![Python3](https://img.shields.io/badge/python->=v3.6.5-blue.svg)](https://www.python.org/downloads/release/python-365)
[![Python3](https://img.shields.io/badge/slackbot-v0.2-brightgreen.svg)](https://github.com/r-f-g/slack-bot)

# Install packages
```bash
git clone https://github.com/r-f-g/slack-bot.git
pip install slack-bot/.
```
# Usage 
```python
from slackbot import bot, message

#set your slackbot
bot(SLACK_BOT_TOKEN, BOT_NAME)
#send message
message(USER, MESSAGE)
```