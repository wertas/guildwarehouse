# -*- coding: utf-8 -*-
import config
import telebot
import time

bot = telebot.TeleBot(config.token)



# @bot.message_handler(content_types=["text"])
# def repeat_all_messages(message): # Название функции не играет никакой роли, в принципе
	# print(message.chat.id ,' >> ' , message.text)
	# if message.text.find('+') != -1:
		# a,b = message.text.split('+')
		# try:
			# a = float(a)
			# b = float(b)
			# bot.send_message(message.chat.id, float(a)+float(b))
			# print(message.chat.id ,' << ' , float(a)+float(b))
		# except ValueError:
			# bot.send_message(message.chat.id, 'Not float numbers')
	# elif message.text.find('-') != -1:
		# a,b = message.text.split('-')
		# try:
			# a = float(a)
			# b = float(b)
			# bot.send_message(message.chat.id, float(a)-float(b))
			# print(message.chat.id ,' << ' , float(a)-float(b))
		# except ValueError:
			# bot.send_message(message.chat.id, 'Not float numbers')
	# elif message.text.find('*') != -1:
		# a,b = message.text.split('*')
		# try:
			# a = float(a)
			# b = float(b)
			# bot.send_message(message.chat.id, float(a)*float(b))
			# print(message.chat.id ,' << ' , float(a)*float(b))
		# except ValueError:
			# bot.send_message(message.chat.id, 'Not float numbers')
	# elif message.text.find('/') != -1:
		# a,b = message.text.split('/')
		# try:
			# a = float(a)
			# b = float(b)
			# bot.send_message(message.chat.id, float(a)/float(b))
			# print(message.chat.id ,' << ' , float(a)/float(b))
		# except ValueError:
			# bot.send_message(message.chat.id, 'Not float numbers')
	# bot.send_message(message.chat.id, input())
	

@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
	bot.send_message(message.chat.id, 'I can calculate every two numbers, try it (example: 2+2)')
	
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.send_message(message.chat.id, message.text)

if __name__ == '__main__':
	while True:
		try:
			bot.polling(none_stop=True)
			print('poll')
		except Exception as err:
			print('---Internet error!---\n\n')
			print(err)
			print('\n\n---------------------')
			time.sleep(5)
# if __name__ == '__main__':	 
	# while True:
		# bot.send_message('279051888', input())