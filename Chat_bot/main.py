import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api import VkUpload
import random
from vk_bot import VkBot
from currency_converter import CurrencyConverter
import val_name
import time
import geo
import requests
from io import BytesIO


def write_msg(user_id, message, var_1):
    random_id = random.randint(0, 100000000)
    if var_1 == "Нет процесса":
        if message == "Не понимаю о чем вы...":
            vk.method('messages.send', {'user_id': user_id, 'sticker_id': 13897, "random_id": random_id})
            return None
        elif message == "конвертер":
            message = "Укажите валюту, потом сколько ее у вас и в какую валюту вы хотите преобразовать," \
                      " одним сообщением через пробел"
            vk.method('messages.send', {'user_id': user_id, 'message': message, "random_id": random_id})
            return "Конвертация"
        elif message == "банкомат":
            message = "Укажите свой адрес и через <</>> Фирму Банка"
            vk.method('messages.send', {'user_id': user_id, 'message': message, "random_id": random_id})
            return "Банкомат"
        else:
            vk.method('messages.send', {'user_id': user_id, 'message': message, "random_id": random_id})
            return None
    elif var_1 == "Конвертация":
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
    elif var_1 == "Банкомат":
        try:
            if "/" in message:
                message = message.split("/")
            else:
                message = [message, ""]
            mes = geo.get_coord(message[0]).split()
            adres, coord = geo.get_atm_adress(message)
            rast = abs((float(mes[0])**2 + float(mes[1])**2) - (float(coord[0])**2 + float(coord[1])**2))
            spn = rast/151
            image = f"https://static-maps.yandex.ru/1.x/?ll={mes[0]},{mes[1]}&spn={spn},{spn}&l=map&pt={str(coord[0])},{str(coord[1])},flag~{mes[0]},{mes[1]},comma"
            global upload
            upload_photo(upload, image)
            send_photo(vk, user_id, *upload_photo(upload, image), adres, message[1])

        except:
            mes = "Извините, произошла ошибка, попробуйте еще раз"
            vk.method('messages.send',
                      {'user_id': user_id, 'message': str(mes), "random_id": random_id})


def upload_photo(upload, url):
    img = requests.get(url).content
    f = BytesIO(img)

    response = upload.photo_messages(f)[0]

    owner_id = response['owner_id']
    photo_id = response['id']
    access_key = response['access_key']

    return owner_id, photo_id, access_key


def send_photo(vk, peer_id, owner_id, photo_id, access_key, adres, bank):
    attachment = f'photo{owner_id}_{photo_id}_{access_key}'
    vk.method('messages.send',
              {'user_id': peer_id, 'message': f"Ближайший банкомат {bank} находиться по адресу: {adres}", "random_id": random.randint(0, 100000000),
               "attachment": attachment})


# API-ключ созданный ранее
token = "3a6526170689978832e8e8ce8d134853a3a3190b704bff875fc0e317c6662cec74662cbcc44c9620e6071"
c = CurrencyConverter()
# Авторизуемся как сообщество
vk = vk_api.VkApi(token=token)

# Работа с сообщениями
longpoll = VkLongPoll(vk)
upload = VkUpload(vk)

# Основной цикл
print("Server started")
for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        if event.to_me:
            print('New message:')
            print(f'For me by: {event.user_id}', end='')

            bot = VkBot(event.user_id)
            result = write_msg(event.user_id, bot.new_message(event.text), "Нет процесса")
            if result == "Конвертация":
                timing = time.time()
                for event in longpoll.listen():
                    if time.time() - timing > 100:
                        break
                    elif event.type == VkEventType.MESSAGE_NEW:
                        if event.to_me:
                            timing = time.time()
                            if not write_msg(event.user_id, event.text, "Конвертация"):
                                break
            if result == "Банкомат":
                timing = time.time()
                for event in longpoll.listen():
                    if time.time() - timing > 100:
                        break
                    elif event.type == VkEventType.MESSAGE_NEW:
                        if event.to_me:
                            timing = time.time()
                            if not write_msg(event.user_id, event.text, "Банкомат"):
                                break
