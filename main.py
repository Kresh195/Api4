import os
from dotenv import load_dotenv
import telegram
import time
from os import listdir


def send_images(images, path, bot, tg_chat_id):
    for image in images:
        with open('{}/{}'.format(path, image), 'rb') as photo:
            bot.send_photo(chat_id=tg_chat_id, photo=photo)
        time.sleep(86400)


def main():
    load_dotenv()
    tg_token = os.getenv('TG_TOKEN')
    bot = telegram.Bot(token=tg_token)
    tg_chat_id = os.getenv('TG_CHAT_ID')

    nasa_path = 'NASA_images/'
    nasa_images = listdir(nasa_path)

    spacex_path = 'Spacex_images/'
    spacex_images = listdir(spacex_path)

    epic_path = 'Epic_images/'
    epic_images = listdir(epic_path)

    while True:
        send_images(nasa_images, nasa_path, bot, tg_chat_id)
        send_images(spacex_images, spacex_path, bot, tg_chat_id)
        send_images(epic_images, epic_path, bot, tg_chat_id)


if __name__ == '__main__':
    main()
