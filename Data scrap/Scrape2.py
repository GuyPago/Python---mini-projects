import selenium.webdriver.support.wait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import selenium.common.exceptions as selexcept
from bs4 import BeautifulSoup
import csv

import pandas as pd
from datetime import datetime as dt
import os.path
import re
import sys
import glob


def begin_scrape(body):
    soup_body = BeautifulSoup(body)

    div_flight_id = soup_body.findAll('div', {'class': 'dErF-carrier-text'})
    # span_dep_city = soup_body.findAll('span', {'class': 'airport-name'})
    span_stops = soup_body.findAll('span', {'class': "stops-text"})
    span_price = soup_body.findAll('span', {'class': 'price-text'})
    span_duration = soup_body.findAll('span', {'class': 'dErF-leg-duration'})
    span_carrier = soup_body.findAll('span', {'class': 'codeshares-airline-names'})

    flights_data = []

    # Extracting data from tags

    for i in range(0, min(len(div_flight_id), len(span_duration), len(span_carrier))):
        flights_data.append([div_flight_id[i].text.strip(), span_stops[i].text.strip(), span_price[i].text.strip()[1:],
                             span_duration[i].text.strip(), span_carrier[i].text.strip()])
        print(flights_data)

    output_file = 'output.csv'
    # with open(output_file, 'w', newline='', encoding='utf-8') as f:
    #     csv_writer = csv.writer(f)
    #     csv_writer.writerows(flights_data)
    #     print('success')


with open('html.txt', 'r', encoding='utf8') as f:
    body = f.read()

begin_scrape(body)