#!/usr/bin/python3
# -*- encoding: utf-8 -*-

"""This is where the code will interface with the bot platform!"""
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
from re import sub
import logging
import self_care
import datetime
import time

class ModelWrapper():
    """Needed to implement the periodic message function properly."""

    def __init__(self, interval, msg_func, chat_id):
        self.chat_id = chat_id
        self.msg_func = msg_func
        self.interval = interval

    def periodic_reminder(self):
        start_time = time.time()

        # Infinite loop
        while True:
            print("Current time: %s" % (time.time() - start_time))
            if ((time.time() - start_time) > self.interval):
                self.msg_func(self.chat_id, self_care.get_phrase())
                start_time = time.time()
            time.sleep(1)

# Global vars
TOKEN='324349241:AAFixmHzkAcuXpwq6spU4Vue8aboo3jMhxc'
MSG_INTERVAL = 3600

# Setting up the updater
updater = Updater(TOKEN)

# This is a good time to set up the logging module, so you will know when and
# why things don't work as expected.
logformat = '%(asctime)s - %(name)s - %(levelname)s - $(message)s'
logging.basicConfig(format=logformat, level=logging.INFO)

# Funcs go here
def start(bot, update, msg="Starting..."):
    """Initial commands."""
    bot.send_message(chat_id=update.message.chat_id, text=msg)
    boot_time = datetime.datetime.now().strftime("%H:%M")
    boot_msg = "Bot was started at " + str(boot_time)
    bot.send_message(chat_id=update.message.chat_id, text=boot_msg)

    # Wrapper goes here
    w = ModelWrapper(MSG_INTERVAL, bot.send_message, update.message.chat_id)

    # Periodic reminder function goes here
    w.periodic_reminder()

def reminder(bot, update):
    """Gives a phrase when prompted"""
    phrase = self_care.get_phrase()
    bot.send_message(chat_id=update.message.chat_id, text=phrase)

def unknown(bot, update):
    wat = "I'm sorry, I didn't understand that command."
    bot.send_message(chat_id=update.message.chat_id, text=wat)

start_handler = CommandHandler('start', start)
reminder_handler = CommandHandler('reminder', reminder)

# Error message handlers should go last.
unknown_handler = MessageHandler(Filters.command, unknown)

dispatcher = updater.dispatcher
dispatcher.add_handler(start_handler)
dispatcher.add_handler(reminder_handler)
dispatcher.add_handler(unknown_handler)

# Starts listening to updates
print("It's alive!")
updater.start_polling()
