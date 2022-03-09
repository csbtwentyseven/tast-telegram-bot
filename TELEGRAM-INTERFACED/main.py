from telegram import *
from telegram.ext import *
from requests import *


def startCommand(update: Updater,context: CallbackContext):
    user = update.message.from_user
    buttons = [[KeyboardButton("🔥 CHANNELS")],[KeyboardButton("💥 POSTS")],[KeyboardButton("✅ BOT IS ACTIVE")]]
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hello {} Welcome to bot!".format(user['username']), reply_markup=ReplyKeyboardMarkup(buttons))

def mainMenu(update,context):
    buttons = [[KeyboardButton("🔥 CHANNELS")],[KeyboardButton("💥 POSTS")],[KeyboardButton("✅ BOT IS ACTIVE")]]
    context.bot.send_message(chat_id=update.effective_chat.id, text="Please Select the Group",reply_markup=ReplyKeyboardMarkup(buttons))


def generalMessageHandler(update: Updater, context: CallbackContext):
#------------------------------GENERAL----------------------------#
    if("🔥 CHANNELS" in update.message.text):
        #fileListener(update,context)
        listChannels(update,context)
    if("💥 POSTS" in update.message.text):
        listPosts(update,context)

    if ("✅ BOT IS ACTIVE" in update.message.text):
        deactivateBot()

    if ("⬅️ BACK" in update.message.text):
        print("Back Tapped")
        mainMenu(update,context)
#------------------------------GENERAL----------------------------#
#------------------------------LIST CHANNELS----------------------------#
    for index in range(1,11):
        if ("🔆 CHANNEL {}".format(index) in update.message.text):
            # fileListener(update,context)
            print("Channel {}".format(index))


def listChannels(update,context):
    buttons = [[KeyboardButton("🔆 CHANNEL 1")], [KeyboardButton("🔆 CHANNEL 2")],[KeyboardButton("➕ ADD CHANNEL")],[KeyboardButton("⛔ REMOVE CHANNEL")], [KeyboardButton("⬅️ BACK")]]
    context.bot.send_message(chat_id=update.effective_chat.id, text="Please Select the Group", reply_markup=ReplyKeyboardMarkup(buttons))

    if ("⬅️ BACK" in update.message.text):
        mainMenu(update,context)

def listPosts(update,context):
    buttons = [[KeyboardButton("✉️ POST 1")], [KeyboardButton("✉️ POST 2")],[KeyboardButton("➕ ADD POST")],[KeyboardButton("⛔ REMOVE POST")],[KeyboardButton("⬅️ BACK")]]
    context.bot.send_message(chat_id=update.effective_chat.id, text="Please Select the Group", reply_markup=ReplyKeyboardMarkup(buttons))


def deactivateBot():
    print("Bot Is Deactivating")




def fileListener(update,context):
    print("image handler")
    context.bot.get_file(update.message.document).download()


if __name__ == '__main__':

    updater = Updater(token="5149901305:AAFBvwD3N1UCCkBDmNlRE9nH5YMa6fFAYtM")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start",startCommand))
    dispatcher.add_handler(MessageHandler(Filters.text, generalMessageHandler))


    dispatcher.add_handler(MessageHandler(Filters.document,fileListener))

    updater.start_polling()
    updater.idle()