import os
import pickle
import random
import requests
from bs4 import BeautifulSoup
import time


class Bot:
    HEADERS = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:104.0) Gecko/20100101 Firefox/104.0",
    }

    def __init__(self, login, password):
        self.session = requests.Session()
        self.__login = login
        self.__password = password
        if not os.path.exists('cookies'):
            os.makedirs('cookies')
        try:
            self.__load_session()
        except FileNotFoundError:
            self.login()

    def __save_session(self):
        with open(f'cookies/{self.__login}.pkl', 'wb') as f:
            pickle.dump(self.session.cookies, f)

    def __load_session(self):
        print('Loading session...')
        with open(f'cookies/{self.__login}.pkl', 'rb') as f:
            self.session.cookies.update(pickle.load(f))

    def login(self):
        response = self.session.post(
            url="https://elem.mobi/",
            data={"plogin": self.__login, "ppass": self.__password},
            headers=Bot.HEADERS,
        )
        if response.status_code == 200:
            self.__save_session()
        else:
            print("Failed to login")

    def donate(self):
        response = self.session.post(
            url="https://elem.mobi/guild/treasury/",
            data={"donate_gold": "10"},
            headers=Bot.HEADERS,
        )
        if response.status_code == 200:
            print("Donation successful")
        else:
            print("Donation failed")

    def do_duels(self):
        for i in range(11):
            time.sleep(random.randint(3, 5))
            self.session.get(url="https://elem.mobi/duel/", headers=Bot.HEADERS)
            duel_page = self.session.get(url="https://elem.mobi/duel/tobattle/", headers=Bot.HEADERS)
            time.sleep(random.randint(3, 5))
            for j in range(20):
                try:
                    soup = BeautifulSoup(duel_page.text, "html.parser")
                    card = soup.find("a", {"class": "chide66"})
                    if card:
                        time.sleep(random.randint(1, 3))
                        duel_page = self.session.get(
                            url=f"https://elem.mobi/{card['href']}", headers=Bot.HEADERS
                        )
                    else:
                        break
                except Exception as e:
                    print(f"An error occurred: {e}")
                    break

# Example usage:
# bot = Bot("your_login", "your_password")
# bot.donate()
# bot.do_duels()
