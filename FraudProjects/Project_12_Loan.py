import time
import requests
import random
import string
import threading

url = 'https://api.lead.im/v2/submit'
emails = ['@yahoo.com', '@gmail.com', '@outlook.com', '@walla.co.il']
amount = ['עד 10,000 ₪', '20,000 ₪', '30,000 ₪', 'מ יותר 30,000 ₪']

with open('data/israeli_names.csv', 'r', encoding='utf-8') as f, open(
        'data/emails.csv', 'r', encoding='utf-8') as g:
    names = f.read().split()
    emails = g.read().split()
with open('data/proxies.txt', 'r') as f:
    proxies = f.read().split()
with open('data/israeli_cities.csv', 'r', encoding='utf-8') as f:
    cities = f.read().split(',\n')

proxy = '190.152.5.126:53040'


def do_requests():
    i = 0
    flag = 0
    while True:
        proxy = proxies[i]
        data = {
            'lm_form': '45120',
            'lm_key': '51bbdd2351',
            'lm_redirect': '{THANKYOU_PAGE_URL}',
            'lm_tyt': '{THANKYOU_PAGE_TEMPLATE}',

            'fname': ' '.join(random.choices(names, k=2)),
            'phone': '05' + ''.join(random.choices(['2', '3', '4', '8'], weights=(71, 3, 20, 6), k=1)) +
                     ''.join(random.choices(string.digits, k=7)),
            'id': str(random.randint(2, 3)) + ''.join(random.choices(string.digits, k=8)),
            'city': random.choice(cities),
            'fld_156169': random.choice(amount)
        }
        try:
            # response = requests.get(url=url, proxies={'http': 'http' + proxy, 'https://': 'http://' + proxy}, timeout=3)
            # print(response.json())
            response = requests.post(url=url, data=data,
                                     proxies={'http': 'http://' + proxy, 'https:': 'http://' + proxy}, timeout=3)
            if 'true' in response.text:
                print(response, 'Sending details: ', [data[j] for j in data][4:])
            else:
                flag += 1


        except:
            print("Skipping. Connnection error")
            i += 1
            flag = 0
            print('trying proxy - ', proxies[i + 1])

        if flag > 20:
            i += 1
            flag = 0
            print('reached 1000 flags, trying proxy - ', proxies[i + 1])


threads = []
for i in range(4):
    t = threading.Thread(target=do_requests)
    t.daemon = True
    threads.append(t)

for i in range(4):
    threads[i].start()

for i in range(4):
    threads[i].join()
