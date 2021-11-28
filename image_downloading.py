import requests


def download_image(link, path, payload=None):
    response = requests.get(link, params=payload)
    response.raise_for_status()
    with open(path, 'wb') as file:
        file.write(response.content)