#!/usr/bin/python3
# -*- encoding: utf-8 -*-

from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters

"""This is where the code will interface with the bot platform!"""
from re import sub
import logging

# Setting up the token
updater = Updater(token='token goes here')

# This is a good time to set up the logging module, so you will know when and
# why things don't work as expected.
logformat = '%(asctime)s - %(name)s - %(levelname)s - $(message)s'
logging.basicConfig(format=logformat, level=logging.INFO)

# Funcs go here
def start(bot, update, msg="I'm a bot, please talk to me!"):
    """Initial commands."""
    bot.send_message(chat_id=update.message.chat_id, text=msg)

def echo(bot, update):
    """Repeats messages sent to the bot."""
    bot.send_message(chat_id=update.message.chat_id, text=update.message.text)

def caps(bot, update, args):
    """Returns messages in uppercase."""
    text_caps = ' '.join(args).upper()
    bot.send_message(chat_id=update.message.chat_id, text=text_caps)

def unknown(bot, update):
    wat = "I'm sorry, I didn't understand that command."
    bot.send_message(chat_id=update.message.chat_id, text=wat)

start_handler = CommandHandler('start', start)
echo_handler = MessageHandler(Filters.text, echo)
# Error message handlers should go last.
unknown_handler = MessageHandler(Filters.command, unknown)

dispatcher = updater.dispatcher
dispatcher.add_handler(start_handler)
dispatcher.add_handler(echo_handler)
dispatcher.add_handler(inline_caps_handler)
dispatcher.add_handler(unknown_handler)

# Starts listening to updates
print("It's alive!")
updater.start_polling()
