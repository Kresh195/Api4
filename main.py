import os
from dotenv import load_dotenv
import telegram
import time
from os import listdir


def send_images(images, path):
    for image in images:
        with open('{}/{}'.format(path, image), 'rb') as photo:
            bot.send_photo(chat_id=chat_id, photo=photo)
        time.sleep(86400)


if __name__ == '__main__':
    load_dotenv()
    tg_token = os.getenv('TG_TOKEN')
    bot = telegram.Bot(token=tg_token)
    chat_id = os.getenv('CHAT_ID')
    nasa_path = 'NASA_images/'
    nasa_images_for_sending = listdir(nasa_path)
    spacex_path = 'Spacex_images/'
    spacex_images_for_sending = listdir(spacex_path)
    epic_path = 'Epic_images/'
    epic_images_for_sending = listdir(epic_path)
    while True:
        send_images(nasa_images_for_sending, nasa_path)
        send_images(spacex_images_for_sending, spacex_path)
        send_images(epic_images_for_sending, epic_path)