import requests


links_spacex = requests.get('https://api.spacexdata.com/v4/launches/latest').json()['links']['flickr']['original']
spacex_path = 'Spacex_images/'


def fetch_spacex_last_launch(link, spacex_path, link_number):
    response = requests.get(link)
    response.raise_for_status()
    with open(spacex_path + 'spacex' + str(link_number) + '.jpg', 'wb') as file:
        file.write(response.content)


if __name__ == '__main__':
    for link_number, link in enumerate(links_spacex):
        fetch_spacex_last_launch(link, spacex_path, link_number)