from bot.bot import  Bot
import time, schedule

bots = []


with open('database/accounts.txt', 'r') as file:
    for line in file:
        login = line.split(':')[0]
        password = line.replace(login+':', '')
        bots.append(Bot(login, password))

def bots_donate():
    for bot in bots:
        bot.donate()

def bots_do_duels():
    for bot in bots:
        bot.do_duels()

if __name__ == '__main__':
    schedule.every().day.do(bots_donate)
    schedule.every(600).minutes.do(bots_do_duels)
    while True:
        schedule.run_pending()
        time.sleep(1)