# Telegram terminal bot
This is a Telegram bot that allows users to send commands to a remote server via SSH and receive the output back through the bot.

## Prerequisites
To run the bot, you need to have the following software installed on your machine:

- Python 3.6 or later
- The `paramiko library` (`pip install paramiko`)
- The `python-telegram-bot` library (`pip install python-telegram-bot==13.7`)

You also need to have a Telegram account and a Telegram bot token. You can obtain a bot token by talking to the BotFather and following the instructions.

## Usage
To run the bot, first edit the bot.py file and replace the following values with your own:

- `SERVER_ADDRESS`: the IP address or hostname of the remote server
- `SSH_USERNAME`: the username to use for SSH authentication
- `SSH_PASSWORD`: the password to use for SSH authentication
- `BOT_TOKEN`: the token of your Telegram bot

Then, run the following command:

``python bot.py``



https://user-images.githubusercontent.com/106667410/224030603-2cc600b0-de10-4e41-ac4c-eab4a4b87d41.mov



This will start the bot and make it available to receive messages from users. To send a command to the remote server, simply send a text message to the bot with the command as the message text. The bot will execute the command on the server and send the output back to you as a reply message.

### License
This bot is released under the MIT License. See the LICENSE file for details.

https://user-images.githubusercontent.com/106667410/224031276-d3214e9b-ebfc-441c-9a0e-56fdcdad5782.mov


