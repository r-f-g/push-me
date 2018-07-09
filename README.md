# push-me
Push me notifications from any device.

[![Python3](https://img.shields.io/badge/python->=v3.6.5-blue.svg)](https://www.python.org/downloads/release/python-365)
[![Python3](https://img.shields.io/badge/pushme-v0.5-brightgreen.svg)](https://github.com/r-f-g/push-me.git)

# Install packages
```bash
git clone https://github.com/r-f-g/push-me.git
pip install push-me/.
```
# Usage of SlackBot
```python
from pushme import Slack

#set your slackbot
Slack.bot(SLACK_BOT_TOKEN, BOT_NAME)
#send message
Sleck.message(USER, MESSAGE)
```

# Usage of Pushover
```python
from pushme import Pushover

#set your pushover
#PUSHOVER_API_TOKENS = {USER: TOKEN, ...}
Pushover.set(PUSHOVER_TOKEN, PUSHOVER_API_TOKENS)
#send message
Pushover.message(API, MESSAGE, TITLE='INFO')
```