from telegram.ext import Updater
import logging
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
from telegram import ReplyKeyboardMarkup
import datetime
import os

tokenID = os.environ["TOKEN"]
updater = Updater(token=tokenID)

dispatcher = updater.dispatcher


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)
conexaoMenu = {
    0 : "Não sei",
    1 : "Não sei",
    2 : "Picanha com batata frita",
    3 : "Não sei",
    4 : "Não sei",
}

ibisMenu = {
    0 : "Detox",
    1 : "Festival de Massas",
    2 : "Não sei",
    3 : "Não sei",
    4 : "Feijoada",
}

def start(bot, update):
     bot.sendMessage(chat_id=update.message.chat_id, text="I'm a bot, please talk to me!")
     
     
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

def today(bot, update):
    custom_keyboard = [['/Conexão'],['/Ibis']]
    reply_markup = ReplyKeyboardMarkup(custom_keyboard, True, True)
    bot.sendMessage(chat_id=update.message.chat_id, 
                     text="Escolha o restaurante para ver o menu de hoje", 
                     reply_markup=reply_markup)

showkeyboard_handler = CommandHandler('today', today)
dispatcher.add_handler(showkeyboard_handler)

def pickDay(bot, update):
    custom_keyboard = [['/seg'],['/ter'],['/qua'],['/qui'],['/sex']]
    reply_markup = ReplyKeyboardMarkup(custom_keyboard, True, True)
    bot.sendMessage(chat_id=update.message.chat_id, 
                     text="Escolha o dia da semana para ver as opções do dia.", 
                     reply_markup=reply_markup)

showkeyboard_handler = CommandHandler('pickDay', pickDay)
dispatcher.add_handler(showkeyboard_handler)

def conexao(bot, update):
    today = datetime.datetime.today().weekday()
    bot.sendMessage(chat_id=update.message.chat_id, text="Hoje no Conexão: " + conexaoMenu[today])

showkeyboard_handler = CommandHandler('Conexão', conexao)
dispatcher.add_handler(showkeyboard_handler)


def ibis(bot, update):
    today = datetime.datetime.today().weekday()
    bot.sendMessage(chat_id=update.message.chat_id, text="Hoje no Ibis: " + ibisMenu[today])

showkeyboard_handler = CommandHandler('Ibis', ibis)
dispatcher.add_handler(showkeyboard_handler)

def seg(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text="Segunda no Ibis: " + ibisMenu[0] + "\n" + "Segunda no Conexão: " + conexaoMenu[0])

showkeyboard_handler = CommandHandler('seg', seg)
dispatcher.add_handler(showkeyboard_handler)

def ter(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text="Terça no Ibis: " + ibisMenu[1] + "\n" + "Terça no Conexão: " + conexaoMenu[1])

showkeyboard_handler = CommandHandler('ter', ter)
dispatcher.add_handler(showkeyboard_handler)

def qua(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text="Quarta no Ibis: " + ibisMenu[2] + "\n" + "Quarta no Conexão: " + conexaoMenu[2])

showkeyboard_handler = CommandHandler('qua', qua)
dispatcher.add_handler(showkeyboard_handler)

def qui(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text="Quinta no Ibis: " + ibisMenu[3] + "\n" + "Quinta no Conexão: " + conexaoMenu[3])

showkeyboard_handler = CommandHandler('qui', qui)
dispatcher.add_handler(showkeyboard_handler)

def sex(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text="Sexta no Ibis: " + ibisMenu[4] + "\n" + "Sexta no Conexão: " + conexaoMenu[4])

showkeyboard_handler = CommandHandler('sex', sex)
dispatcher.add_handler(showkeyboard_handler)
    



def unknown(bot, update):
     bot.sendMessage(chat_id=update.message.chat_id, text="Sorry, I didn't understand that command.")

unknown_handler = MessageHandler(Filters.command, unknown)
dispatcher.add_handler(unknown_handler)



updater.start_polling()

