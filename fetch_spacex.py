import requests


def download_image(link, path, payload=None):
    if payload is None:
        payload = {}
    response = requests.get(link, params=payload)
    response.raise_for_status()
    with open(path, 'wb') as file:
        file.write(response.content)


def fetch_spacex_last_launch():
    spacex_request = requests.get('https://api.spacexdata.com/v4/launches/latest')
    spacex_request.raise_for_status()
    spacex_links = spacex_request.json()['links']['flickr']['original']
    for link_number, link in enumerate(spacex_links):
        path = 'Spacex_images/spacex{}.jpg'.format(link_number)
        download_image(link, path)


def main():
    fetch_spacex_last_launch()


if __name__ == '__main__':
    main()
