import requests
import json
import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Return a dad joke from icanhazdadjoke.com
def dad_joke():
    api_url = "https://icanhazdadjoke.com/"
    headers =  {"Accept":"application/json"}
    response = requests.get(api_url, headers=headers)

    # Return an error message if the status is not 200
    if response.status_code != 200:
        return "An unexpected error occurred"

    return response.json()["joke"]


# If the message is 'Hello' return a dad joke, else suggest the user send hello
def handle_message(update, context):
    if update.effective_message.text == 'Hello':
        context.bot.send_message(chat_id=update.effective_chat.id, text=dad_joke())
    else:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Send 'Hello' for a dad joke")


# SETUP: Create updater and dispatcher
updater = Updater(token="5100736370:AAFNoFMKkDW0RIqnuNpvaR2626NVTCimPRM", use_context=True)
dispatcher = updater.dispatcher

# Register a message handler
dispatcher.add_handler(MessageHandler(Filters.text, handle_message))

# Begin polling
updater.start_polling()
