# Modules required for web crawling
import requests
from bs4 import BeautifulSoup
import telegram
from apscheduler.schedulers.blocking import BlockingScheduler

bot = telegram.Bot(token = '1124727009:AAEensfrJYML4y6-ebvHRe-F6KMpAS1BIoE')

url = 'https://www.cinemark.com/north-texas/cinemark-legacy-and-xd?showDate=2020-03-17'

def job_function():
    html = requests.get(url)
    bs = BeautifulSoup(html.text, 'html.parser')
    xd_list = bs.select('img.xd')
    title = []

    if (xd_list):
        for i in xd_list:
            i = i.find_parent('div', class_ = 'col-xs-12 col-sm-10')
            title.append(i.select_one('a > h3').text.strip())
        bot.sendMessage(chat_id = 1035524947, text = '{} xd advance tickets have been opened.'.format(', '.join(map(str, title))))
        s.pause()
    else:
        print('There is no xd advanced ticket')
        bot.sendMessage(chat_id = 1035524947, text = 'There is no xd advanced ticket')

s = BlockingScheduler()
s.add_job(job_function, 'interval', seconds = 30)
s.start()
