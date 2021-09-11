import os
from telegram.ext import Updater, MessageHandler, Filters
from Adafruit_IO import Client
user = os.getenv('user')
api = os.getenv('api')
aio = Client('user', 'api')
light = aio.feeds('light')
fan = aio.feeds('fan')
def help1(bot,update):
  chat_id=bot.message.chat_id
  bot.message.reply_text('COMMANDS\n\tTurn on light\n\tTurn off light\n\tTurn on fan\n\tTurn off fan\n\t')
def start(bot,update):
  chat_id=bot.message.chat_id
  bot.message.reply_text('Use /help for commands')
def l1(bot,update):
  chat_id=bot.message.chat_id
  aio.send_data(light.key,1)
  bot.message.reply_text('LIGHT TURNED ON')
def l0(bot,update):
  chat_id=bot.message.chat_id
  aio.send_data(light.key,0)
  bot.message.reply_text('LIGHT TURNED OFF')
def f1(bot,update):
  chat_id=bot.message.chat_id
  aio.send_data(fan.key,1)
  bot.message.reply_text('FAN TURNED ON')
def f0(bot,update):
  chat_id=bot.message.chat_id
  aio.send_data(fan.key,0)
  bot.message.reply_text('FAN TURNED OFF')
def main(bot,update):
  a = bot.message.text
  if (a == "/start" ):
    start(bot,update)
  elif (a == "/help" ):
    help1(bot,update)
  elif (a == "Turn on light" ):
    l1(bot,update)
  elif (a == "Turn off light"):
    l0(bot,update)
  elif (a == "Turn on fan" ):
    f1(bot,update)
  elif (a == "Turn off fan" ):
    f0(bot,update)
  else :
    bot.message.reply_text('Invalid input Use /help for commands')
bot_token = '1989461961:AAHPC0F3thD4SpiBZYwfVHOSh6uPAV5wDJ8'
u = Updater(bot_token,use_context=True)
dp = u.dispatcher
dp.add_handler(MessageHandler(Filters.text,main))
u.start_polling()
u.idle()
