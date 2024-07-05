import logging
import requests
from requests.exceptions import RequestException

#logging.basicConfig(filename='output.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s: %(message)s')

websites = ['https://www.youtube.com/', 'https://wikipedia.org', 'https://yahoo.com', 'https://yandex.ru',
            'https://whatsapp.com', 'https://amazon.com', 'https://www.ozon.ru', 'https://instagram.com',
            'https://twitter.com']


def check_websites(websites):
    for website in websites:
        try:
            response = requests.get(website)
            if response.status_code == 200:
                logging.info(f'{website}, response - {response.status_code}')
                with open('success_responses.log', 'a') as file:
                    file.write(f'INFO: {website}, response - {response.status_code}\n')
            else:
                logging.warning(f'{website}, response - {response.status_code}')
                with open('bad_responses.log', 'a') as file:
                    file.write(f'WARNING: {website}, response - {response.status_code}\n')
        except RequestException:
            logging.error(f'{website}, NO CONNECTION')
            with open('blocked_responses.log', 'a') as file:
                file.write(f'ERROR: {website}, NO CONNECTION\n')


check_websites(websites)
