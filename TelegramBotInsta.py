import urllib.request
import json
import logging
import telegram
import requests
from bs4 import BeautifulSoup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram.error import (TelegramError, Unauthorized, BadRequest, 
                            TimedOut, ChatMigrated, NetworkError)
# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

token = "YOUR_TOKEN_HERE"



def start(update,context):
    name = update.message.from_user.first_name
    msg = "Hello "+name+".\nNice to meet you !\nI'm telegram bot written in Python by @vinayak_09\nFor more info type /help"
    update.message.reply_text(msg)

def help(update,context):
    msg = "Use following commands to download content from Instagram !\n/instadp <username>\n/instaphoto <photoURL>\n/instavideo <videoURL>"
    update.message.reply_text(msg)

def instaDp(update, context):
    try:
        textInstaProfileId = ' '.join(context.args)
        context.bot.send_chat_action(chat_id=update.effective_message.chat_id ,action=telegram.ChatAction.TYPING)
        fullLink="https://www.instagram.com/"+textInstaProfileId+"/?__a=1"
        update.message.reply_text('Fetching Details.....')
        context.bot.send_chat_action(chat_id=update.effective_message.chat_id ,action=telegram.ChatAction.UPLOAD_PHOTO)
        with urllib.request.urlopen(fullLink) as url:
            data = json.loads(url.read().decode())
            data2 = data['graphql']
            data3 = data2['user']
            profileUrl = data3['profile_pic_url_hd']
            context.bot.send_photo(chat_id=update.effective_chat.id, photo=profileUrl)
    except Exception as error:
        update.message.reply_text(str(error))


def instaPhoto(update,context):
    try:
        textInstaPhoto = ' '.join(context.args)
        context.bot.send_chat_action(chat_id=update.effective_message.chat_id ,action=telegram.ChatAction.TYPING)
        update.message.reply_text("Fetching Image...\nMake Sure Account is not Private !")
        imgLink =textInstaPhoto
        with urllib.request.urlopen(imgLink) as url:
            dataVid= url.read().decode()
            soup = BeautifulSoup(dataVid,features="lxml")
            j=soup.find(property="og:image")
            vLink=j.get('content')
            context.bot.send_photo(chat_id=update.effective_chat.id, photo=vLink)
    except Exception as error:
        update.message.reply_text(str(error))


def instaVideo(update,context):
    try:
        textInstaVideo = ' '.join(context.args)
        context.bot.send_chat_action(chat_id=update.effective_message.chat_id ,action=telegram.ChatAction.TYPING)
        update.message.reply_text("Fetching Video...\nMake Sure Account is not Private !")
        vidLink =textInstaVideo
        with urllib.request.urlopen(vidLink) as url:
            dataVid= url.read().decode()
            soup = BeautifulSoup(dataVid,features="lxml")
            j=soup.find(property="og:video:secure_url")
            vLink=j.get('content')
            context.bot.send_video(chat_id=update.effective_chat.id, video=vLink)
    except Exception as error:
        update.message.reply_text(str(error))



def main():
    
        """Start the bot."""
        # Create the Updater and pass it your bot's token.
        # Make sure to set use_context=True to use the new context based callbacks
        # Post version 12 this will no longer be necessary
        updater = Updater(token, use_context=True)

        # Get the dispatcher to register handlers
        dp = updater.dispatcher


        start_command_handler = CommandHandler('start', start)
        dp.add_handler(start_command_handler)

        help_command_handler = CommandHandler('help', help)
        dp.add_handler(help_command_handler)
       

        # on command /instaDp get dp from respective profile and send it On Telegram !
        insta_dp_handler = CommandHandler('instaDp', instaDp)
        dp.add_handler(insta_dp_handler)

        # on command /instaPhoto get image Post from instagram and send it On Telegram !
        insta_photo_handler = CommandHandler('instaPhoto', instaPhoto)
        dp.add_handler(insta_photo_handler)


        # on command /instaVideo get image Post from instagram and send it On Telegram !
        insta_video_handler = CommandHandler('instaVideo', instaVideo)
        dp.add_handler(insta_video_handler)

        # on different commands - answer in Telegram
    

        # on noncommand i.e message - echo the message on Telegram
        #dp.add_handler(MessageHandler(Filters.text, echo))

    

        # Start the Bot
        updater.start_polling()

        # Run the bot until you press Ctrl-C or the process receives SIGINT,
        # SIGTERM or SIGABRT. This should be used most of the time, since
        # start_polling() is non-blocking and will stop the bot gracefully.
        updater.idle()
    
if __name__ == '__main__':
    main()
