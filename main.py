import os
from dotenv import load_dotenv
import telegram
import time
from os import listdir


load_dotenv()

TG_TOKEN = os.getenv('TG_TOKEN')
bot = telegram.Bot(token=TG_TOKEN)
chat_id = os.getenv('CHAT_ID')
nasa_path = 'NASA_images/'
nasa_images_for_sending = listdir(nasa_path)
spacex_path = 'Spacex_images/'
spacex_images_for_sending = listdir(spacex_path)
epic_path = 'Epic_images/'
epic_images_for_sending = listdir(epic_path)


def send_nasa_images(nasa_images_for_sending, chat_id):
    for image in nasa_images_for_sending:
        bot.send_photo(chat_id=chat_id, photo=open('NASA_images/{}'.format(image), 'rb'))
        time.sleep(86400)


def send_epic_images(epic_images_for_sending, chat_id):
    for image in epic_images_for_sending:
        bot.send_photo(chat_id=chat_id, photo=open('Epic_images/{}'.format(image), 'rb'))
        time.sleep(86400)


def send_spacex_images(spacex_images_for_sending, chat_id):
    for image in spacex_images_for_sending:
        bot.send_photo(chat_id=chat_id, photo=open('Spacex_images/{}'.format(image), 'rb'))
        time.sleep(86400)


if __name__ == '__main__':
    while True:
        send_nasa_images(nasa_images_for_sending, chat_id)
        send_spacex_images(spacex_images_for_sending, chat_id)
        send_epic_images(epic_images_for_sending, chat_id)