import os
import requests
from urllib.parse import urlparse
from image_downloading import download_image
from dotenv import load_dotenv
import time


def fetch_file(nasa_link_image):
    path_from_link = urlparse(nasa_link_image).path
    file_name = os.path.split(path_from_link)[1]
    name, file_format = os.path.splitext(file_name)
    return file_format, name


def fetch_nasa_images(nasa_token):
    payload = {'count': '30', 'api_key': nasa_token}
    nasa_links_response = requests.get(
        'https://api.nasa.gov/planetary/apod', params=payload)
    nasa_links_response.raise_for_status()
    nasa_links = nasa_links_response.json()
    for nasa_link in nasa_links:
        nasa_link_image = nasa_link['hdurl']
        file_format, name = fetch_file(nasa_link_image)
        path = 'NASA_images/{}{}'.format(name, file_format)
        download_image(nasa_link_image, path)


def fetch_epic_images(nasa_token):
    payload = {'api_key': nasa_token}
    epic_links_response = requests.get(
        'https://api.nasa.gov/EPIC/api/natural', params=payload)
    epic_links_response.raise_for_status()
    epic_images = epic_links_response.json()[:5]
    for epic_image in epic_images:
        date = epic_image['formatted_date'].split(' ')[0]
        formatted_date = time.strftime('%Y/%m/%d', time.strptime(date, '%Y-%m-%d'))
        epic_image_link = 'https://api.nasa.gov/EPIC/archive/natural/{}/png/{}.png'.format(
            formatted_date, epic_image['image'])
        path = 'Epic_images/{}.png'.format(epic_image['image'])
        download_image(epic_image_link, path, payload=payload)


def main():
    load_dotenv()
    nasa_token = os.getenv('NASA_TOKEN')
    fetch_nasa_images(nasa_token)
    fetch_epic_images(nasa_token)


if __name__ == '__main__':
    main()
