import time
import requests
import random
import string
import threading

url = 'http://brk.biton.club/index.php'
emails = ['@yahoo.com', '@gmail.com', '@outlook.com', '@walla.co.il']
amount = ['עד 10,000 ₪', '20,000 ₪', '30,000 ₪', 'מ יותר 30,000 ₪']

with open('data/israeli_names.csv', 'r', encoding='utf-8') as f, open(
        'data/emails.csv', 'r', encoding='utf-8') as g:
    names = f.read().split()
    emails = g.read().split()
with open('data/proxies.txt', 'r') as f:
    proxies = f.read().split()

cities = ['צפון', 'השרון', 'מרכז', 'שפלה', 'ירושלים והסביבה', 'מודיעין והסביבה', 'צפון רחוק (אחרי חיפה)', 'דרום',
          'דרום רחוק (אחרי ב"ש)', 'אחר']
ages = ['מתחת ל-18', '18-24', '25-30', '31-55', '56-65', '66-70', 'מעל 70']

proxy = '190.152.5.126:53040'


def do_requests():
    i = 0
    flag = 0
    while True:
        proxy = proxies[i]
        data = {
            'page': 'landing.action',
            'id': '385787',
            'token': '8647c3f37568311f62e4e4f2722c60aa',
            'force': 'mobile',
            'elementId': '10102007',
            'elementAction': 'submit',
            'field[0]': random.choice(['דרך תלוש השכר שלי', 'כ.אשראי/הוראת קבע', 'לא זוכר/ת']),
            'field[1]': random.choice(cities),
            'field[2]': random.choice(ages),
            'field[3]': ' '.join(random.choices(names, k=2)),
            'field[4]': '05' + ''.join(random.choices(['2', '3', '4', '8'], weights=(71, 3, 20, 6), k=1)) +
                        ''.join(random.choices(string.digits, k=7)),
            'output': 'json'
        }
        try:
            # response = requests.get(url=url, proxies={'http': 'http' + proxy, 'https://': 'http://' + proxy}, timeout=3)
            # print(response.json())
            response = requests.post(url=url, data=data,
                                     proxies={'http': 'http://' + proxy, 'https:': 'https://' + proxy}, timeout=3)
            if 'true' in response.text:
                print(response, 'Sending details: ', [data[j] for j in data][6:])
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


# do_requests()

threads = []
for i in range(30):
    t = threading.Thread(target=do_requests)
    t.daemon = True
    threads.append(t)

for i in range(30):
    threads[i].start()

for i in range(30):
    threads[i].join()
