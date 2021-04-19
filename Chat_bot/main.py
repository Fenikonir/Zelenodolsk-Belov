import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
import random
from vk_bot import VkBot
from currency_converter import CurrencyConverter
import val_name
import time


def write_msg(user_id, message, var_1):
    random_id = random.randint(0, 100000000)
    if var_1:
        if message == "Не понимаю о чем вы...":
            vk.method('messages.send', {'user_id': user_id, 'sticker_id': 13897, "random_id": random_id})
            return None
        elif message == "конвертер":
            message = "Укажите валюту, потом сколько ее у вас и в какую валюту вы хотите преобразовать," \
                      " одним сообщением через пробел"
            vk.method('messages.send', {'user_id': user_id, 'message': message, "random_id": random_id})
            return "Конвертация"

        else:
            vk.method('messages.send', {'user_id': user_id, 'message': message, "random_id": random_id})
            return None
    else:
        if "отмен" in message.lower():
            vk.method('messages.send',
                      {'user_id': user_id, 'message': "Отменяю", "random_id": random_id})
            return False
        elif len(message.split()) == 3:
            random_id = random.randint(0, 100000000)
            s = event.text.split()
            val = val_name.chek(s[0].upper())
            kol = s[1]
            val_2 = val_name.chek(s[2].upper())
            try:
                mes = str(round(c.convert(int(kol), val, val_2), 2)) + " " + val_2
            except ValueError:
                mes = "Извините, произошла ошибка, попробуйте еще раз"
            vk.method('messages.send',
                      {'user_id': user_id, 'message': str(mes), "random_id": random_id})
        else:
            vk.method('messages.send',
                      {'user_id': user_id, 'sticker_id': 13897, "random_id": random_id})
        return True


# API-ключ созданный ранее
token = "3a6526170689978832e8e8ce8d134853a3a3190b704bff875fc0e317c6662cec74662cbcc44c9620e6071"
c = CurrencyConverter()
# Авторизуемся как сообщество
vk = vk_api.VkApi(token=token)

# Работа с сообщениями
longpoll = VkLongPoll(vk)

# Основной цикл
print("Server started")
for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        if event.to_me:
            print('New message:')
            print(f'For me by: {event.user_id}', end='')

            bot = VkBot(event.user_id)
            result = write_msg(event.user_id, bot.new_message(event.text), True)
            if result == "Конвертация":
                timing = time.time()
                for event in longpoll.listen():
                    if time.time() - timing > 100:
                        break
                    elif event.type == VkEventType.MESSAGE_NEW:
                        if event.to_me:
                            timing = time.time()
                            if not write_msg(event.user_id, event.text, False):
                                break



