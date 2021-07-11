# Telegrambot-for-Instagram

This telegram bot is used for downloading public posts from instagram and everyone's DP. (Private Profile pictures also)

# PS : Bot is Not Working!
##### Why?
- Instagram requries **_User_** to be signed in to view any profile or post.
#### What we can do?
- We need to first signIn to instagram using _urllib.request_
- We need to save our session
- Then bot can extract profile data.


### Before deploying to heroku Create your bot using Telegram:
    Note : BotFather is telegrams official bot to create other bots.
* Send /newbot command to [@BotFather](https://t.me/BotFather)
* Now send your bot name to botfather. eg InstaDownloaderBot
* Now send username for your bot it must ends with 'bot'. eg instascrapper_bot
* Congratulations ! Your bot is created successfully.
* Now copy HTTP API token and keep it secure.
* Download and unzip above source code.
* Open TelegramBotInsta.py and search line number 16 and replace 'YOUR_TOKEN_HERE' with your HTTP API token which we got from @BotFather and save it.
* Initialize git repository using git init command in current working directory.(Current working directory is above source code directory)
* Now login with heroku cli. Learn more about heroku installation [here](https://devcenter.heroku.com/articles/heroku-cli) .
* Create heroku app using heroku commands in cli -> heroku create instabotapp-example
* Push to heroku master !

## How to deploy on Heroku

Clone this Project or download as ZIP.
To clone use following command in Console :

```bash
git clone https://github.com/Vinayak-09/telegrambot-for-instagram.git
```
* Add your bot token in TelegramBotInsta.py file

Upload/Push this to your heroku account !

## Usage

#### How to get profile pic ?
  * Simply send this to bot -> /instadp username
  * Bot will send image in a while !
#### How to get posted pic ?
  * Simply send this to bot -> /instaphoto imageUrl
  * Bot will send image in a while if it is public !
#### How to get posted video ?
  * Simply send this to bot ->/instavideo videoUrl
  * Bot will send video in a while if it is public !

## Contributing
Pull requests are welcome.

# Contact
[<img src="media/telegram.webp" height=50 />](https://t.me/vinayak_09)

