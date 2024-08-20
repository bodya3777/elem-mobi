from bot.bot import  Bot
import time, schedule

current_day = 19

bots = []


with open('database/accounts.txt', 'r') as file:
    for line in file:
        login = line.split(':')[0]
        password = line.replace(login+':', '')
        bots.append(Bot(login, password))



if __name__ == '__main__':
    schedule.every().day.do(bots_donate)
    schedule.every(600).minutes.do(bots_donate)
    while True:
        schedule.run_pending()
        time.sleep(1)