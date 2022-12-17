from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import telegram
import json
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram.error import (
    TelegramError,
    Unauthorized,
    BadRequest,
    TimedOut,
    ChatMigrated,
    NetworkError,
)

token = "YOUR TOKEN HERE"
options = Options()

# options.add_argument("--headless")            Uncomment Code after loging to Your Instagram
# options.add_argument("--no-sandbox")          Uncomment Code after loging to Your Instagram
# options.add_argument("start-maximized")       Uncomment Code after loging to Your Instagram
# options.add_argument("disable-infobars")      Uncomment Code after loging to Your Instagram
# options.add_argument("--disable-extensions")  Uncomment Code after loging to Your Instagram

user_agent = "Mozilla/5.0 (X11; Linux x86_64; rv:89.0) Gecko/20100101 Firefox/89.0"
options.add_argument(f"user-agent={user_agent}")

# uncomment below Line to use on Linux
# driver = webdriver.Chrome(executable_path="./chromedriver", options=options)

# uncommnet below Line to use on Windows
# driver = webdriver.Chrome(executable_path=".\chromedriver", options=options)

driver.get("https://www.instagram.com")

time.sleep(3)
driver.find_element_by_name("username").send_keys("INSTAGRAM_USERNAME")
time.sleep(3)
driver.find_element_by_name("password").send_keys("INSTAGRAM_PASSWORD")
time.sleep(3)


# driver.find_element_by_class_name("sqdOP.L3NKy.y3zKF").send_keys(Keys.ENTER)
# time.sleep(5)
# saveLoginButton = driver.find_element_by_class_name("sqdOP.L3NKy.y3zKF")
# time.sleep(5)


driver.find_element_by_xpath("//button[@type='submit']").send_keys(Keys.ENTER)
time.sleep(5)


print("Your bot is Up and Running :)")

# if saveLoginButton.is_displayed():
#     saveLoginButton.send_keys(Keys.ENTER)
# else:
#     print("ERROR 5\nSolution :")
#     print(
#         "Step 1: Comment lines from 20 to 24\nStep 2: Rerun code\nStep 3: It will Open Chrome Window\nStep 4: Login to Your Instagram Account\nStep 5: After Loging try sending msg to BOT /instadp USERNME\n Step 6 :If it works uncomment the Code from line 20 to 24\nStep 7 :Rerun"
#     )


def start(update, context):
    name = update.message.from_user.first_name
    msg = (
        "Hello "
        + name
        + ".\nNice to meet you !\nI'm telegram bot written in Python by @vinayak_09\nFor more info type /help"
    )
    update.message.reply_text(msg)


def help(update, context):
    msg = "Use following commands to download content from Instagram !\n/instadp <username>\n/instaAllPhotos <username>"
    update.message.reply_text(msg)


def instaDp(update, context):
    try:
        textInstaProfileId = " ".join(context.args)
        context.bot.send_chat_action(
            chat_id=update.effective_message.chat_id,
            action=telegram.ChatAction.UPLOAD_PHOTO,
        )
        fullLink = "https://www.instagram.com/" + textInstaProfileId + +"/?__a=1&__d=dis"
        update.message.reply_text("Fetching Details.....")
        context.bot.send_chat_action(
            chat_id=update.effective_message.chat_id,
            action=telegram.ChatAction.UPLOAD_PHOTO,
        )
        driver.get(fullLink)
        time.sleep(5)
        source = driver.find_element_by_tag_name("pre").text
        data = json.loads(source)
        data2 = data["graphql"]
        data3 = data2["user"]
        profileUrl = data3["profile_pic_url_hd"]
        context.bot.send_photo(chat_id=update.effective_chat.id, photo=profileUrl)
    except Exception as error:
        update.message.reply_text(str(error))


def instaAllPhotos(update, context):
    try:
        textInstaProfileId = " ".join(context.args)
        context.bot.send_chat_action(
            chat_id=update.effective_message.chat_id,
            action=telegram.ChatAction.UPLOAD_PHOTO,
        )
        fullLink = "https://www.instagram.com/" + textInstaProfileId + +"/?__a=1&__d=dis"
        context.bot.send_chat_action(
            chat_id=update.effective_message.chat_id,
            action=telegram.ChatAction.UPLOAD_PHOTO,
        )
        driver.get(fullLink)
        time.sleep(5)
        source = driver.find_element_by_tag_name("pre").text
        data = json.loads(source)
        data2 = data["graphql"]
        data3 = data2["user"]
        is_privateAccount = data3["is_private"]
        update.message.reply_text("Please Hold On...\nFetching Details.....")
        fullLink = "https://www.instagram.com/" + textInstaProfileId
        driver.get(fullLink)
        time.sleep(5)
        images = driver.find_elements_by_class_name("FFVAD")
        if images == []:
            update.message.reply_text("No Posts Availalbe")
        else:
            for img in images:
                context.bot.send_photo(
                    chat_id=update.effective_chat.id, photo=img.get_attribute("src")
                )

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

    start_command_handler = CommandHandler("start", start)
    dp.add_handler(start_command_handler)

    help_command_handler = CommandHandler("help", help)
    dp.add_handler(help_command_handler)

    # on command /instaDp get dp from respective profile and send it On Telegram !
    insta_dp_handler = CommandHandler("instaDp", instaDp)
    dp.add_handler(insta_dp_handler)

    insta_dp_handler = CommandHandler("instaAllPhotos", instaAllPhotos)
    dp.add_handler(insta_dp_handler)

    # Start the Bot
    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()
