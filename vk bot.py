from translate import Translator

# working with images
import imageio
import glob

import requests, vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.upload import VkUpload
from datetime import datetime
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
import time
import  sys


import random


# collecting images into an array
image_list = []
for image_path in glob.glob("C:\\Users\\Артур\\Downloads\\Flags\\*.png"):
    im = imageio.imread(image_path)
    image_list.append(image_path)
    print (image_path)
    print (im.dtype)
print(image_list[0])

# translater
translator = Translator(from_lang="English", to_lang="Russian")
result = translator.translate("Tokelau")
print(result)
#

token = 'dbfd8caa3a154800a5799603dce97730179d2069e91307b69bb5e616719e47ec808c53cb20d238d2127a4'
vk_session = vk_api.VkApi(token= token)
session = vk_session.get_api()
load = VkUpload(session)
longpoll = VkLongPoll(vk_session)
s = ''
timef = time.time()
timemin = sys.maxsize
file = open('game.txt', 'r')
writing = ''



def load_photo(upload, photo):
    response = upload.photo_messages(photo)[0]

    owner_id = response['owner_id']
    photo_id = response['id']
    access_key = response['access_key']

    return owner_id, photo_id, access_key

def send_photo(session, peer_id, owner_id, photo_id, access_key):
    attachment = f'photo{owner_id}_{photo_id}_{access_key}'
    session.messages.send(
        random_id = 0,
        peer_id=peer_id,
        attachment=attachment
    )

def create_keyboard(response):
    keyboard = VkKeyboard(one_time=True)
    if response == '/menu':
        keyboard.add_button('ИГРЫ',color=VkKeyboardColor.DEFAULT)
        keyboard.add_button('КОМАНДЫ', color=VkKeyboardColor.PRIMARY)
    elif response == '[club159274465|@arrkhange1] игры' or response == '[club159274465|arrkhange1 - just a personality] игры':
        keyboard.add_button('CASINO', color=VkKeyboardColor.NEGATIVE)
        keyboard.add_button('CAPTCHA TRAINER', color=VkKeyboardColor.POSITIVE)
        keyboard.add_button('FLAGS', color=VkKeyboardColor.PRIMARY)
    elif response == '[club159274465|@arrkhange1] команды':
        keyboard.add_button('УЧАСТНИКИ', color=VkKeyboardColor.NEGATIVE)
    elif response == '[club159274465|@arrkhange1] casino':
        keyboard = VkKeyboard(one_time=False)
        keyboard.add_button('1', color=VkKeyboardColor.NEGATIVE)
        keyboard.add_button('2', color=VkKeyboardColor.POSITIVE)
        keyboard.add_button('3', color=VkKeyboardColor.POSITIVE)
        keyboard.add_button('4', color=VkKeyboardColor.NEGATIVE)
        keyboard.add_line()
        keyboard.add_button('5', color=VkKeyboardColor.POSITIVE)
        keyboard.add_button('6', color=VkKeyboardColor.NEGATIVE)



    elif response == '/close':
         return keyboard.get_empty_keyboard()
    keyboard = keyboard.get_keyboard()
    return keyboard


game_flags = False
game_capcha = False
named_flag = 0

for event in longpoll.listen():

    if event.type == VkEventType.MESSAGE_NEW:
        response = event.text.lower()
        print(response)
        keyboard = create_keyboard(response)

        #game_flags = True    maybe delete
        #game_capcha = False

        # СООБЩЕНИЕ В ГРУППУ
        if event.from_user and not event.from_me :

            if response == '/commands':
                session.messages.send(user_id= event.user_id, message = 'opening commands', random_id = 0, keyboard = keyboard)

            elif response == '/ban':
                vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'The user has been banned!', 'random_id': 0})

            elif response == '/close':
                vk_session.method('messages.send',
                                                  {'user_id': event.user_id, 'message': 'closing a keyboard', 'random_id': 0, 'keyboard': keyboard})


        # СООБЩЕНИЕ ИЗ БЕСЕДЫ
        elif event.from_chat:
            n = 0
            if response == '[club159274465|@arrkhange1] команды':
              session.messages.send(chat_id = event.chat_id, message = 'Список доступных команд: ', random_id = 0, keyboard = keyboard)

           # ВЫВОД УЧАСТНИКОВ БЕСЕДЫ

            elif response == '[club159274465|@arrkhange1] участники':
                chat = vk_session.method('messages.getConversationMembers', {'chat_id': event.chat_id, 'peer_id': event.peer_id})
                count = chat['count']
                while n < count-1:
                    member = chat['profiles'][n]['first_name']
                    member1 = chat['profiles'][n]['last_name']
                    session.messages.send(chat_id = event.chat_id, message = member + ' ' + member1, random_id = 0)
                    n += 1
                n = 0
            #######################
            elif response == '/menu':
                session.messages.send(chat_id = event.chat_id, message = 'Список моих возможностей: ', random_id = 0, keyboard= keyboard)

            elif response == '[club159274465|@arrkhange1] игры' or response == '[club159274465|arrkhange1 - just a personality] игры':
                session.messages.send(chat_id=event.chat_id, message='Список доступных игр с ботом: ', random_id=0,
                                      keyboard=keyboard)

            elif response == '/close':
                session.messages.send(chat_id=event.chat_id, message= 'closing a keyboard', random_id=0, keyboard = keyboard)

        # CAPTCHA TRAINER
            elif response == 'rand' or response == '[club159274465|@arrkhange1] captcha trainer' or response == '[club159274465|arrkhange1 - just a personality] captcha trainer':
                game_capcha = True
                session.messages.send(chat_id=event.chat_id, message='Инструкция к игре "Капча-тренер": \n \n Поступает рандомная последовательность из латинских букв и цифр, Вы должны успеть напечатать ее за 4 секунды! \n \n Игра начнется через 10 секунд!', random_id=0)
                time.sleep(10)
                #timef = time.time()
                p = 0
                s = ''

                b = []
                a = ['a', 'b', 'c', 'd', 'e', 'f', '2', '5','1', '3','4', '6', '7', '8', '9', '0', 'g', 'h', 'i', 'j', 'i','k', 'l', 'm', 'n','o', 'p', 'r','s', 't', 'u', 'v', 'x', 'y', 'w', 'z']
                while p < 5: # 6 symbols
                    b.append(random.choice(a))
                    p += 1
                s = s.join(b)
                session.messages.send(chat_id=event.chat_id, message=s + '\n \n Время пошло!', random_id=0)
                timef = time.time()
            elif response == s and game_capcha:
                game_capcha = False
                timelast = time.time() - timef
                if timelast <= 4:
                    session.messages.send(chat_id=event.chat_id, message='Ваше время: ' + str(timelast) + '\n \n Вы выиграли! \n \n Хочешь еще? Пиши "хочу" или "+"!', random_id=0)
                else:
                    session.messages.send(chat_id=event.chat_id, message='Ваше время: ' + str(timelast) + '\n \n Вы проиграли! \n \n Хочешь еще? Пиши "хочу" или "+"!', random_id=0)



            elif response == 'хочу' or response == '+':
                game_capcha = True
                session.messages.send(chat_id=event.chat_id, message='Приготовься!! \n \n  Игра начнется через 5 секунд!', random_id=0)
                time.sleep(5)
                timef = time.time()
                p = 0
                s = ''
                b = []
                a = ['a', 'b', 'c', 'd', 'e', 'f', '2', '5','1', '3','4', '6', '7', '8', '9', '0', 'g', 'h', 'i', 'j', 'i', 'k', 'l', 'm', 'n','o', 'p', 'r','s', 't', 'u', 'v', 'x', 'y', 'w', 'z']
                while p < 6:
                    b.append(random.choice(a))
                    p += 1
                s = s.join(b)


                session.messages.send(chat_id=event.chat_id, message=s + '\n \n Время пошло!', random_id=0)
                timef = time.time()
            elif response == s and game_capcha:
                game_capcha = False
                timelast = time.time() - timef
                if timelast <= 4:
                    session.messages.send(chat_id=event.chat_id, message='Ваше время: ' + str(timelast) + ' \n \n Вы выиграли! \n \n Хочешь еще? Пиши "хочу" или "+"!', random_id=0)
                else:
                    session.messages.send(chat_id=event.chat_id, message='Ваше время: ' + str(timelast) + '\n \n  Вы проиграли! \n \n Хочешь еще? Пиши "хочу" или "+"!', random_id=0)








         # CASINO
            elif response == '[club159274465|@arrkhange1] casino' or response == '[club159274465|arrkhange1 - just a personality] casino':
                session.messages.send(chat_id=event.chat_id, message='Инструкция к игре "Казино": \n \n Вы кидаете кубик. Если Ваше число совпало с числом бота - Вы выиграли! \n \n Перестать играть - /close \n \n Через 10 секунд игра начнется!', random_id=0)

                time.sleep(10)

                session.messages.send(chat_id=event.chat_id, message='Кидай кубик!', random_id=0, keyboard = keyboard)




            elif response == '[club159274465|@arrkhange1] 1' or response == '[club159274465|@arrkhange1] 2' or response == '[club159274465|@arrkhange1] 3' or response == '[club159274465|@arrkhange1] 4' or response == '[club159274465|@arrkhange1] 5' or response == '[club159274465|@arrkhange1] 6':
                botnum = random.randint(1,6)
                session.messages.send(chat_id=event.chat_id, message='Мое число: ' + str(botnum), random_id=0)
                print(botnum)
                if '[club159274465|@arrkhange1] ' + str(botnum) == response:
                    keyboard = VkKeyboard.get_empty_keyboard()
                    session.messages.send(chat_id=event.chat_id, message='WIN!' + '\n \n Продолжим?', random_id=0, keyboard = keyboard)

            elif response == 'да' or response == 'lf' or response == 'da':
                da = create_keyboard('[club159274465|@arrkhange1] casino')
                session.messages.send(chat_id=event.chat_id, message='Погнали!', random_id=0,
                                      keyboard=da)


            # FLAGS

            elif response == '[club159274465|@arrkhange1] flags' or response == '[club159274465|arrkhange1 - just a personality] flags'  :
                game_flags = True
                session.messages.send(chat_id=event.chat_id, message="Добро пожаловать в игру Флаги!\n\nНачинаем через 3 секунды!\n\n", random_id=0)
                time.sleep(3)

                flag_cnt = 0
                allright = True

                session.messages.send(chat_id=event.chat_id, message="Назовите эту страну:\n\n", random_id=0)

            elif game_flags:
                rand_gen = random.randint(0, 259)
                send_photo(session, event.peer_id, *load_photo(load, image_list[rand_gen]))
                flag_name = image_list[rand_gen][::-1][:image_list[rand_gen][::-1].find('\\')][4:][::-1]       # extractring a country name from a path: turning around the path, finding the first backslash, getting a slice til the backslash, skipping .png, reversing again into normal country


                if translator.translate(flag_name) == response:
                    session.messages.send(chat_id=event.chat_id,
                                          message="Правильно! Ваш счет " +  " / 5", random_id=0)
                    named_flag += 1
                    if named_flag == 5:
                        session.messages.send(chat_id=event.chat_id, message="Поздравляю, Вы - гений географии!", random_id=0, keyboard = create_keyboard("/menu"))

                else:
                    session.messages.send(chat_id=event.chat_id, message="Неверно! Вы проиграли!", random_id=0,keyboard=create_keyboard("/menu"))


















































