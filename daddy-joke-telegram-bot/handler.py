import os
import json
import time
import logging
import requests
from telegram import Bot, Update
from emoji import emojize


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

RESPONSE = {
    "OK": {
        'statusCode': 200,
        'headers': {'Content-type': 'application/json'},
        'body': json.dumps("Ok")
    },
    "ERROR": {
        'statusCode': 400,
        'body': json.dumps("Something went wrong")
    }
}


def configure_telegram():
    TELEGRAM_TOKEN = os.environ.get('TELEGRAM_TOKEN')
    if not TELEGRAM_TOKEN:
        logging.error(
            'TELEGRAM_TOKEN Not found, it must be set before moving forward.')
        raise NotImplementedError
    return Bot(TELEGRAM_TOKEN)


def webhook(event, context):
    bot = configure_telegram()
    logging.info('Event: {}'.format(event))
    if event.get('httpMethod') == 'POST' and event.get('body'):
        logging.info("Message successfully received")
        update = Update.de_json(json.loads(event.get('body')), bot)
        chat_id = update.message.chat_id
        text = update.message.text
        if text == '/start':
            text = """Hello, human! I am an daddy jokes bot, built with Python and the Serverless Framework. I help with hilarious daddy joke {}.\n\
You can take a look at my source code here: https://github.com/vaibhavsingh97/serverless-enigma/tree/master/daddy-joke-telegram-bot.\n\
Found a {}, please drop a tweet to my creator: https://twitter.com/vaibhavsingh97. Happy botting!""".format(emojize("! :laughing:", use_aliases=True), emojize("! :bug:", use_aliases=True))
            bot.send_chat_action(chat_id=chat_id, action="TYPING")
            time.sleep(2)
            bot.send_message(chat_id=chat_id, text=text)
        elif text == '/newjoke':
            headers = {
                "Accept": "application/json",
                "User-Agent": "daddy joke telegram bot (https://github.com/vaibhavsingh97/serverless-enigma/tree/master/daddy-joke-telegram-bot)"
            }
            r = requests.get('https://icanhazdadjoke.com/', headers=headers)
            res = r.json()
            text = res["joke"]
            bot.send_chat_action(chat_id=chat_id, action="TYPING")
            time.sleep(2)
            bot.send_message(chat_id=chat_id, text=text)
        elif text == '/help':
            text = """
Hello! Daddy Joke bot welcomes you on the telegram!
Here's the commands:
- /start - to get know more about Daddy Joke Bot
- /newjoke - to get new joke
- /help - to view help text
This bot is being worked on, so it may break sometimes. Contact @vaibhavsingh97 on twitter \
or open issue [here](https://github.com/vaibhavsingh97/serverless-enigma/issues).
"""
            bot.send_chat_action(chat_id=chat_id, action="TYPING")
            time.sleep(2)
            bot.send_message(chat_id=chat_id, text=text, parse_mode="MARKDOWN")
        logging.info("Message successfully sent")
        # RESPONSE["OK"]["body"] = json.dumps("Message Sent")
        return RESPONSE["OK"]
    return RESPONSE["ERROR"]


def set_webhook(event, context):
    logging.info('Event: {}'.format(event))
    bot = configure_telegram()
    url = 'https://{}/{}'.format(
        event.get('headers').get('Host'),
        event.get('requestContext').get('stage')
    )
    webhook = bot.set_webhook(url)

    if webhook:
        RESPONSE["OK"]["body"] = json.dumps("Webhook URL successfully set.")
        return RESPONSE["OK"]

    return RESPONSE["ERROR"]


def get_webhook_info(event, context):
    logging.info('Event: {}'.format(event))
    bot = configure_telegram()
    webhook_info = bot.get_webhook_info()
    logging.info('Event: {}'.format(webhook_info))
    if webhook_info:
        RESPONSE["OK"]["body"] = str(webhook_info)
        return RESPONSE["OK"]
    return RESPONSE["ERROR"]
