#!/usr/bin/python3
# -*- encoding: utf-8 -*-

from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
from telegram.ext import InlineQueryHandler

# Needed for inline mode
from telegram import InlineQueryResultArticle, InputTextMessageContent
from re import sub
import logging

# Setting up the token
updater = Updater(token='209645836:AAFDLsNO3wjeMHzhEkFZzRDXNFYYroKCHuQ')

# This is a good time to set up the logging module, so you will know when and
# why things don't work as expected.
logformat = '%(asctime)s - %(name)s - %(levelname)s - $(message)s'
logging.basicConfig(format=logformat, level=logging.INFO)

# Funcs go here
def start(bot, update):
    """Initial commands."""
    msg = "I'm a bot, please talk to me! (plus obligatory Hello World!)"
    bot.send_message(chat_id=update.message.chat_id, text=msg)

def echo(bot, update):
    """Repeats messages sent to the bot."""
    bot.send_message(chat_id=update.message.chat_id, text=update.message.text)

def caps(bot, update, args):
    """Returns messages in uppercase."""
    text_caps = ' '.join(args).upper()
    bot.send_message(chat_id=update.message.chat_id, text=text_caps)

def inline_caps(bot, update):
    query = update.inline_query.query
    if not query:
        return
    results = list()
    results.append(
            InlineQueryResultArticle(
                id=query.upper(),
                title='Caps',
                input_message_content=InputTextMessageContent(query.upper())
                )
            )
    bot.answer_inline_query(update.inline_query.id, results)

def mimimi(bot, update, args):
    """Changes the vowels to i at output"""
    buf = ' '.join(args)
    out = sub(r'[aeiou]', 'i', buf)
    bot.send_message(chat_id=update.message.chat_id, text=out)

def unknown(bot, update):
    wat = "I'm sorry, I didn't understand that command."
    bot.send_message(chat_id=update.message.chat_id, text=wat)

start_handler = CommandHandler('start', start)
echo_handler = MessageHandler(Filters.text, echo)
caps_handler = CommandHandler('caps', caps, pass_args=True)
mimimi_handler = CommandHandler('mimimi', mimimi, pass_args=True)
inline_caps_handler = InlineQueryHandler(inline_caps)
# Error message handlers should go last.
unknown_handler = MessageHandler(Filters.command, unknown)

dispatcher = updater.dispatcher
dispatcher.add_handler(start_handler)
dispatcher.add_handler(echo_handler)
dispatcher.add_handler(caps_handler)
dispatcher.add_handler(mimimi_handler)
dispatcher.add_handler(inline_caps_handler)
dispatcher.add_handler(unknown_handler)

# Starts listening to updates
print("It's alive!")
updater.start_polling()
