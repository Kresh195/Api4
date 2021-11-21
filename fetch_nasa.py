import os
import requests
from urllib.parse import urlparse
from fetch_spacex import download_image
from dotenv import load_dotenv
import time


def fetch_file_format(nasa_link_image):
    path_from_link = urlparse(nasa_link_image).path
    file_name = os.path.split(path_from_link)[1]
    name, file_format = os.path.splitext(file_name)
    return file_format, name


def fetch_nasa_images(nasa_link_image):
    file_format, name = fetch_file_format(nasa_link_image)
    path = 'NASA_images/{}{}'.format(name, file_format)
    download_image(nasa_link_image, path)


def fetch_epic_images(epic_images_info, nasa_token):
    payload = {"api_key": nasa_token}
    for epic_image_info in epic_images_info:
        date = time.strftime('%Y/%m/%d', time.strptime(epic_image_info['date'].split(' ')[0], '%Y-%m-%d'))
        print(date)
        epic_image_link = 'https://api.nasa.gov/EPIC/archive/natural/{}/png/{}.png'.format(
            date, epic_image_info['image'])
        path = 'Epic_images/{}.png'.format(epic_image_info['image'])
        download_image(epic_image_link, path, payload=payload)


def main():
    load_dotenv()
    nasa_token = os.getenv('NASA_TOKEN')
    payload = {"count": "30", "api_key": nasa_token}
    nasa_links_response = requests.get(
        'https://api.nasa.gov/planetary/apod', params=payload)
    nasa_links_response.raise_for_status()
    payload = {"api_key": nasa_token}
    epic_links_response = requests.get(
        'https://api.nasa.gov/EPIC/api/natural', params=payload)
    epic_links_response.raise_for_status()
    nasa_links = nasa_links_response.json()
    epic_images_info = epic_links_response.json()[:5]
    for nasa_link in nasa_links:
        nasa_link_image = nasa_link['hdurl']
        fetch_nasa_images(nasa_link_image)
    fetch_epic_images(epic_images_info, nasa_token)


if __name__ == '__main__':
    main()
