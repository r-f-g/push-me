class Slack:
    import json as __json
    import os as __os
    from slackclient import SlackClient as __SlackClient

    __CONFIG_FILE = '.slackbot.json'

    def __load(self):
        if not self.__os.path.isfile(self.__CONFIG_FILE):
            print("You must first set up a bot's name and a token.")
            return None
        return self.__json.load(open(self.__CONFIG_FILE, 'r'))

    @classmethod
    def bot(cls, token, name):
        with open(cls.__CONFIG_FILE, 'w') as f:
            f.write(cls.__json.dumps({'token':token, 'name':name}))

    @classmethod
    def message(cls, to, msg):
        bot = cls.__load(cls)
        if bot:
            SLACK = cls.__SlackClient(bot.get('token'))
            cls.response = SLACK.api_call(
                    'chat.postMessage',
                    channel=f'@{to}',
                    text=msg,
                    as_user=bot.get('name'))

class Pushover:
    import json as __json
    import os as __os
    from pushover import Client as  __Client
    __CONFIG_FILE = '.pushover.json'

    def __load(self):
        if not self.__os.path.isfile(self.__CONFIG_FILE):
            print("You must first set up pushover client.")
            return None
        return self.__json.load(open(self.__CONFIG_FILE, 'r'))

    @classmethod
    def set(cls, token, api_tokens):
        with open(cls.__CONFIG_FILE, 'w') as f:
            f.write(cls.__json.dumps({'token':token, 'api':{**api_tokens}}))

    @classmethod
    def add(cls, api_tokens):
        conf = cls.__load(cls)
        cls.set(
            token=conf['token'],
            api_tokens={**api_tokens, **conf['api']})

    @classmethod
    def message(cls, api, msg, title='INFO'):
        conf = cls.__load(cls)
        if conf:
            if api not in conf['api']:
                print(f"{api} - api is not set up in settings.")
            else:
                client = cls.__Client(conf['token'], api_token=conf['api'][api])
                cls.response = client.send_message(msg, title=title)
        