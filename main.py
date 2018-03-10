
# -*- coding: utf-8 -*-
import telebot
import constants
import  time
import BotMessages
import smtplib
from email.mime.text import MIMEText
from email.header import Header
import emailSend
arr=[]
k =0
j = 0


bot = telebot.TeleBot('554039664:AAG2PsxQrTmx4d_mG_UBgmzY1w6pR-DNeaI')

user_markupStart = telebot.types.ReplyKeyboardMarkup(True, False)
user_markupStart.row('Запись на тренировку', 'Задать вопрос')
user_markupStart.row('Наши тренера', 'Wod')
user_markupStart.row('Питание', 'Рассписание')
user_markupStart.row('Отчет по своим показателям', 'О нас')

def myupd(bot,text,text2):
    while text == text2 :
        text = bot.last_update_id
        time.sleep(0.3)
        print(text)
        print(text2)

def log(text,arr):
    if text !='Отчет по своим показателям':

        arr.append(text)


def messBoss(bot,arr):
    bot.send_message(constants.boss,str(arr))

#----------------------------------------------------------------Запись на тренировку---------------------------------

def ZapT(message):
    hide_markup = telebot.types.ReplyKeyboardRemove()
    bot.send_message(message.chat.id,'Заполнить как можно точнее!!!',reply_markup=hide_markup)

    bot.send_message(message.chat.id,'Время:')
    text = bot.last_update_id
    text2 = bot.last_update_id
    myupd(bot, text, text2)
    bot.send_message(message.chat.id,'Тренер:')
    text = bot.last_update_id
    text2 = bot.last_update_id
    myupd(bot, text, text2)
    bot.send_message(message.chat.id,'Дни недели:')
    text = bot.last_update_id
    text2 = bot.last_update_id
    myupd(bot, text, text2)
    bot.send_message(message.chat.id, 'Номер телефона:')
    text = bot.last_update_id
    text2 = bot.last_update_id
    myupd(bot, text, text2)
    bot.send_message(message.chat.id,'Вы записаны',reply_markup=user_markupStart)

def Opr(message):
    hide_markup = telebot.types.ReplyKeyboardRemove()


    text = bot.last_update_id
    bot.send_message(message.chat.id, BotMessages.AnswersOpe[0],reply_markup=hide_markup)

    text2 = bot.last_update_id
    myupd(bot,text,text2)
    text = bot.last_update_id
    bot.send_message(message.chat.id,BotMessages.AnswersOpe[1])

    text2 = bot.last_update_id
    myupd(bot,text,text2)
    text = bot.last_update_id
    bot.send_message(message.chat.id,BotMessages.AnswersOpe[2])
    text2 = bot.last_update_id
    myupd(bot,text,text2)
    text = bot.last_update_id
    bot.send_message(message.chat.id,BotMessages.AnswersOpe[3])
    text2 = bot.last_update_id
    myupd(bot,text,text2)

    bot.send_message(message.chat.id,'Отлично',reply_markup=user_markupStart)

#-----------------------------------Функции по разделу питания-----------------------------------
def Pit(message):

    user_markupPit = telebot.types.ReplyKeyboardMarkup(True,False)
    user_markupPit.row('Набор массы','Похудение')
    user_markupPit.row('Палео диета','Рецепты' )
    text = bot.last_update_id
    bot.send_message(message.chat.id,"Используйте команду '/start' для возвращения в главное меню",reply_markup=user_markupPit)
    text2 = bot.last_update_id
    myupd(bot,text,text2)

def PitM(message):

    bot.send_message(message.chat.id,'Ссылка на пост в телеграф о наборе массы')

def PitP(message):
    bot.send_message(message.chat.id,'Ссылка на пост в телеграф о похудении')
def PitPal(message):
    bot.send_message(message.chat.id,'Описание палео')
def PitRec(message):
    bot.send_message(message.chat.id,'Описание рецептов')
#-----------------------------------Функции по разделу питания-----------------------------------


@bot.message_handler(commands=['start'])
def handele_commands(message):

    bot.send_message(message.chat.id, 'Выберите команду', reply_markup=user_markupStart)


@bot.message_handler(content_types=['text'])
def handle_text(message):
    if message.text == 'Отчет по своим показателям':
        global k
        k=1
        Opr(message)

        mail_sender = 'emailgymbot@gmail.com'
        mail_receiver = 'adiskahovsky@gmail.com'
        username = 'emailgymbot@gmail.com'
        password = 'Bot12345678'
        server = smtplib.SMTP('smtp.gmail.com:587')

        f = open('myfile.txt', 'r')
        subject = 'Отчеты по показателям'
        body = f.read()
        f.close()
        msg = MIMEText(body, 'plain', 'UTF-8')
        msg['Subject'] = Header(subject, 'UTF-8')

        server.starttls()
        server.ehlo()
        server.login(username, password)
        server.sendmail(mail_sender, mail_receiver, msg.as_string())
        server.quit()
        f = open('myfile.txt', 'w')
        f.write(' ')
        f.close()
        k=0
    first_name = str(message.from_user.first_name)
    last_name = str(message.from_user.last_name)
    OldMess = message.text
   # log(OldMess, arr)




    if message.text == 'Питание':

        Pit(message)

    if message.text == 'Набор массы':
        PitM(message)

    if message.text == 'Похудение':
        PitP(message)

    if message.text == 'Палео диета':
        PitPal(message)
    if message.text =='Рецепты':
        PitRec(message)


    if message.text == 'Запись на тренировку':

        global j
        j=2
        ZapT(message)
        mail_sender = 'emailgymbot@gmail.com'
        mail_receiver = 'adiskahovsky@gmail.com'
        username = 'emailgymbot@gmail.com'
        password = 'Bot12345678'
        server = smtplib.SMTP('smtp.gmail.com:587')

        f = open('ZapT.txt', 'r')
        subject = 'Запись на тренировку'
        body = f.read()
        f.close()
        msg = MIMEText(body, 'plain', 'UTF-8')
        msg['Subject'] = Header(subject, 'UTF-8')

        server.starttls()
        server.ehlo()
        server.login(username, password)
        server.sendmail(mail_sender, mail_receiver, msg.as_string())
        server.quit()
        f = open('ZapT.txt', 'w')
        f.write(' ')
        f.close()
        j=0

    OldMess2 = str(message.text)

    if  k == 1:

        f =open('myfile.txt','a')
        f.write(first_name + ' '+last_name +':'+ ' '+str(OldMess2)+'\n')
        print('k работает')
        print(OldMess2)
        f.close()




    if j == 2:
        f = open('ZapT.txt', 'a')
        f.write(first_name + ' ' + last_name + ':' + ' ' + str(OldMess) + '\n')
        print(OldMess2)
        print('Ты гений')

        f.close()





bot.polling(none_stop=True,interval=0)