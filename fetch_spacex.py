import requests


def fetch_spacex_last_launch(link, link_number):
    response = requests.get(link)
    response.raise_for_status()
    with open('Spacex_images/spacex{}.jpg'.format(link_number), 'wb') as file:
        file.write(response.content)


def main():
    links_spacex = requests.get('https://api.spacexdata.com/v4/launches/latest').json()['links']['flickr']['original']
    for link_number, link in enumerate(links_spacex):
        print(link_number)
        fetch_spacex_last_launch(link, link_number)


if __name__ == '__main__':
    main()
