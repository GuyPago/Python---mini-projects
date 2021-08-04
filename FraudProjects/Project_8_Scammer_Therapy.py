import time
import requests
import random
import string
import threading
''
url_id = 'http://beuld.net/thermometrograph/spectrohelioscope/tephrochronology/quingentumvirate/thermometrograph/honorificabilitudinity/tetrakishexahedron/spectrohelioscope/hydrometeorology/pantochronometer/account.php'
url_card = 'http://beuld.net/thermometrograph/spectrohelioscope/tephrochronology/quingentumvirate/thermometrograph/honorificabilitudinity/tetrakishexahedron/spectrohelioscope/hydrometeorology/pantochronometer/ld3.php'

start_numbers = ['4580', '5326', '3755']
with open('data/israeli_names.csv', 'r', encoding='utf-8') as f:
    names = f.read().split()


def do_requests():
    while True:
        data = {
            'cardno': ''.join(random.choices(start_numbers, weights=(84, 10, 6), k=1)) + ''.join(random.choices(string.digits, k=16)),
            'exprDate': '0' + str(random.randint(1, 9)) + '2' + str(random.randint(2, 9)),
            'fullName': ' '.join(random.choices(names, k=2)),
            'cvv': ''.join(random.choices(string.digits, k=3)),
            'idno': str(random.randint(2, 3)) + ''.join(random.choices(string.digits, k=8))
        }

        # response = requests.post(url=url, data=data['idno'])
        # print(response, data['idno'])
        response_card = requests.post(url=url_card, data=data).text
        print(response_card, ' card no. ', data['cardno'], 'cvv =', data['cvv'], ', name =', data["fullName"], ',  id=', data['idno'])


threads = []
for i in range(50):
    t = threading.Thread(target=do_requests)
    t.daemon = True
    threads.append(t)

for i in range(50):
    threads[i].start()

for i in range(50):
    threads[i].join()
