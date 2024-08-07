from bot.bot import  Bot
import random, time

current_day = 19

bots = []


with open('database/accounts.txt', 'r') as file:
    for line in file:
        login = line.split(':')[0]
        password = line.replace(login+':', '')
        bots.append(Bot(login, password))



while True:
    current_time = time.localtime()
    if current_day == 0:
        for bot in bots:
           bot.donate()
        current_day = current_time.tm_mday
    if current_day != current_time.tm_mday:
        for bot in bots:
            bot.donate()
        current_time = time.localtime()
        current_day = current_time.tm_mday
    time.sleep(random.randrange(6000, 7000))
    for bot in bots:
        bot.do_duels()