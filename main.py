import requests
import os
from urllib.parse import urlparse
from dotenv import load_dotenv
load_dotenv()

TOKEN = os.getenv('TOKEN')
links_spacex = requests.get('https://api.spacexdata.com/v4/launches/latest').json()['links']['flickr']['original']
path = 'images/'
response_links_nasa = requests.get(
    'https://api.nasa.gov/planetary/apod?count=30&api_key={}'.format(TOKEN))
response_links_epic = requests.get(
    'https://api.nasa.gov/EPIC/api/natural?api_key={}'.format(TOKEN))
nasa_path = 'NASA_images/'
epic_path = 'Epic_images/'
links_nasa = response_links_nasa.json()
epic_images_info = response_links_epic.json()[:5]


def fetch_spacex_last_launch(link, path, link_number):
    response = requests.get(link)
    response.raise_for_status()
    with open(path + 'spacex' + str(link_number) + '.jpg', 'wb') as file:
        file.write(response.content)


def fetch_file_format(link_nasa_image):
    path_from_link = urlparse(link_nasa_image).path
    file_format = os.path.splitext(path_from_link)[1]
    file_name = os.path.split(path_from_link)[1].split('.')[0]
    return file_format, file_name


def fetch_nasa_images(link_nasa_image):
    file_format, file_name = fetch_file_format(link_nasa_image)
    response = requests.get(link_nasa_image)
    response.raise_for_status()
    with open(nasa_path + file_name + file_format, 'wb') as file:
        file.write(response.content)


def fetch_epic_images(epic_images_info):
    for epic_image_info in epic_images_info:
        date = epic_image_info['date'].split(' ')[0].split('-')
        epic_image_link = 'https://api.nasa.gov/EPIC/archive/natural/{}/{}/{}/png/{}.png' \
                          '?api_key={}'.format(date[0], date[1], date[2],
                                               epic_image_info['image'], TOKEN)
        response = requests.get(epic_image_link)
        response.raise_for_status()
        with open(epic_path + epic_image_info['image'] + '.png', 'wb') as file:
            file.write(response.content)


if __name__ == '__main__':
    for link_number, link in enumerate(links_spacex):
        fetch_spacex_last_launch(link, path, link_number)
    for link_nasa in links_nasa:
        link_nasa_image = link_nasa['hdurl']
        fetch_nasa_images(link_nasa_image)
    fetch_epic_images(epic_images_info)