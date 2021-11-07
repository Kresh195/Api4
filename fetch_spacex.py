import requests


def download_image(link, path, payload=None):
    if payload is None:
        payload = {}
    response = requests.get(link, params=payload)
    response.raise_for_status()
    with open(path, 'wb') as file:
        file.write(response.content)


def fetch_spacex_last_launch():
    links_spacex = requests.get('https://api.spacexdata.com/v4/launches/latest').json()['links']['flickr']['original']
    links_spacex.raise_for_status()
    for link_number, link in enumerate(links_spacex):
        path = 'Spacex_images/spacex{}.jpg'.format(link_number)
        download_image(link, path)


def main():
    fetch_spacex_last_launch()


if __name__ == '__main__':
    main()
