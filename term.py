import paramiko
from telegram.ext import Updater, MessageHandler, Filters

def run_command_on_server(command):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect('SERVER_ADDRESS', username='SSH_USERNAME', password='SSH_PASSWORD')
    stdin, stdout, stderr = ssh.exec_command(command)
    output = stdout.read()
    ssh.close()
    return output

def handle_message(update, context):
    text = update.message.text
    output = run_command_on_server(text)
    update.message.reply_text(output.decode())

updater = Updater('BOT_TOKEN', use_context=True)
updater.dispatcher.add_handler(MessageHandler(Filters.text, handle_message))
updater.start_polling()
updater.idle()
