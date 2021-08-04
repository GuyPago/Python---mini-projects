from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import selenium.common.exceptions as selexcept

import pandas as pd
from datetime import datetime as dt
import os.path
import re
import sys
import glob

import time

chromedriver_path = 'C:\\Users\\guypa\\Desktop\\Data\\Chromedriver.exe'

# This will open a chrome window
browser = webdriver.Chrome(executable_path=chromedriver_path)


# def ticket_chooser(ticket):
#     try:
#         ticket_type = browser.find_element_by_xpath(ticket)
#         ticket_type.click()
#     except Exception as e:
#         pass


def more_details(details):
    try:
        details_type = browser.find_element_by_xpath(details)
        details_type.click()
    except Exception as e:
        pass


def dep_country_chooser(dep_country):
    browser.find_element(By.XPATH, "//*[@id='wizard-flight-tab-oneway']/div[2]/div[1]/div/div[1]/div/div/div/button").click()
    fly_from = browser.find_element(By.XPATH, "//*[@id='app-layer-location-field-leg1-origin-ta-dialog']/div[2]/div/div[1]/section/div/input")
    print('hey')
    #fly_from.send_keys('  ' + dep_country)
    fly_from.send_keys('BLR' + Keys.RETURN)
    time.sleep(3)
    first_item = browser.find_element_by_xpath("//a[@id='aria-option-0']")
    time.sleep(3)
    first_item.click()


def arrival_country_chooser(arrival_country):
    fly_to = browser.find_element_by_xpath("//input[@id='flight-destination-hp-flight']")
    time.sleep(3)
    fly_to.clear()
    time.sleep(3)
    fly_to.send_keys('  ' + arrival_country)
    time.sleep(3)
    first_item = browser.find_element_by_xpath("//a[@id='aria-option-0']")
    time.sleep(3)
    first_item.click()


def dep_date_chooser(month, day, year):
    dep_date_button = browser.find_element_by_xpath("//input[@id='flight-departing-hp-flight']")
    dep_date_button.clear()
    dep_date_button.send_keys(str(month) + "/" + str(day) + "/" + str(year))


def return_date_chooser(month, day, year):
    return_date_button = browser.find_element_by_xpath("//input[@id='flight-returning-hp-flight']")
    for i in range(11):
        return_date_button.send_keys(Keys.BACKSPACE)
    return_date_button.send_keys(str(month) + "/" + str(day) + "/" + str(year))


def search():
    search = browser.find_element_by_xpath("//button[@class='btn-primary btn-action gcw-submit']")
    time.sleep(5)
    browser.execute_script("arguments[0].click();", search)
    time.sleep(20)


def CheckLastFlightIndexByPrice(price_list, factor):
    price_list_size = len(price_list)
    if price_list_size == 0:
        return 0
    price_list_ = ''.join(price_list)
    price_list_as_numbers = re.findall(r'[0-9][0-9,]+', price_list_)
    for i in range(price_list_size):
        price_list_as_numbers[i] = int(price_list_as_numbers[i].replace(',', ''))
    min_price = min(price_list_as_numbers)
    for i in range(price_list_size):
        if int(price_list_as_numbers[i]) > factor*int(min_price):
            return i
    return i


def GenerateBadIndex(dep_times_list, last_flight_index):
    # hide unnecessary buttons
    bad_indexes = []
    expand_button = browser.find_elements_by_xpath("//span[@class='show-flight-details']")
    expand_button_list = [value.text for value in expand_button]

    for i in range(last_flight_index):
        if str(expand_button_list[i]) == 'Flight details and baggage fees':
            bad_indexes.append(i)
    return bad_indexes


def RevealNFlight(n):
    try:
        air_type_details = "(//a[@class='flight-details-link toggle-trigger'])[" + str(n) + "]"
        more_details(air_type_details)
    except Exception as e:
        pass


def HideNFlight(n):
    try:
        air_type_details_hide = "(//a[@class='flight-details-link toggle-trigger open'])[" + str(n) + "]"
        more_details(air_type_details_hide)
    except Exception as e:
        pass


def AddingFlightDetails(i, stops_list, bad_indexes, number_element_to_ignore):
    while True:
        if (len(bad_indexes) > 0):
            first_element = int(bad_indexes[0])
            if (first_element == i + number_element_to_ignore):
                number_element_to_ignore = number_element_to_ignore + 1
                bad_indexes_length = bad_indexes_length - 1
                bad_indexes.pop(0)
                continue
        break
    # preper the web page for our desire flight (with the consideration of revael just one flight each iteration)
    RevealNFlight(1 + i + number_element_to_ignore)

    # Airplan type
    air_type = browser.find_elements_by_xpath("//li[@data-test-id='aircraft-in-details']")
    air_type_list = [value.text for value in air_type]

    # details-departure-localName
    dep_local_name = browser.find_elements_by_xpath("//span[@data-test-id='details-departure-localName']")
    dep_local_name_list = [value.text for value in dep_local_name]

    # details-arrival-localName
    arr_local_name = browser.find_elements_by_xpath("//span[@data-test-id='details-arrival-localName']")
    arr_local_name_list = [value.text for value in arr_local_name]

    # details-airline-data
    details_airline_data = browser.find_elements_by_xpath("//li[@data-test-id='details-airline-data']")
    details_airline_data_list = [value.text for value in details_airline_data]

    # details-airline-data
    class_type = browser.find_elements_by_xpath("//li[@data-test-id='details-class-type']")
    class_type_list = [value.text for value in class_type]

    j = 0
    # Insert flight details to our DF
    try:
        df.loc[i, 'dep_airType'] = air_type_list[j]
        df.loc[i, 'dep_Coach'] = class_type_list[j]
    except Exception as e:
        pass
    try:
        df.loc[i, 'departure_localName'] = dep_local_name_list[j]
        df.loc[i, 'departure_details_airline_data'] = details_airline_data_list[j]
        stops_number_at_row_i = re.findall("\d+", stops_list[i])
        k = 1
        if (len(stops_number_at_row_i) > 0):
            while (int(stops_number_at_row_i[0]) > 0):
                stops_number_at_row_i[0] = int(stops_number_at_row_i[0]) - 1
                j = j + 1
                df.loc[i, 'Connection_%s' % k] = dep_local_name_list[j]
                df.loc[i, 'Connection_details_airline_data_%s' % k] = details_airline_data_list[j]
                df.loc[i, 'Connection_airType_%s' % k] = air_type_list[j]
                df.loc[i, 'Connection_Coach_%s' % k] = class_type_list[j]
                k = k + 1
    except Exception as e:
        pass
    try:
        df.loc[i, 'arrival_localName'] = arr_local_name_list[j]
        df.loc[i, 'arrival_details_airline_data'] = details_airline_data_list[j]
    except Exception as e:
        pass
    HideNFlight(1)
    time.sleep(1)
    return number_element_to_ignore


def DataProcessing():
    global df
    df = df[0:0]
    number_element_to_ignore = 0

    # departure times
    dep_times = browser.find_elements_by_xpath("//span[@data-test-id='departure-time']")
    dep_times_list = [value.text for value in dep_times]

    # arrival times
    arr_times = browser.find_elements_by_xpath("//span[@data-test-id='arrival-time']")
    arr_times_list = [value.text for value in arr_times]

    # airline name
    airlines = browser.find_elements_by_xpath("//span[@data-test-id='airline-name']")
    airlines_list = [value.text for value in airlines]

    # durations
    durations = browser.find_elements_by_xpath("//span[@data-test-id='duration']")
    durations_list = [value.text for value in durations]

    # stops
    stops = browser.find_elements_by_xpath("//span[@class='number-stops']")
    stops_list = [value.text for value in stops]

    # layovers
    layovers = browser.find_elements_by_xpath("//span[@data-test-id='layover-airport-stops']")
    layovers_list = [value.text for value in layovers]

    # prices
    prices = browser.find_elements_by_xpath("//span[@data-test-id='listing-price-dollars']")
    price_list = [value.text for value in prices]

    # last flight to scrape according to the price differences (here we choose multiply by 2)
    last_flight_index = CheckLastFlightIndexByPrice(price_list, 2)

    # Genrate flight to igonre according to the last_flight_index
    bad_indexes = GenerateBadIndex(dep_times_list, last_flight_index)

    # delete the non relevant flights
    for i in range(len(bad_indexes)):
        dep_times_list.pop(int(bad_indexes[i]))
        arr_times_list.pop(int(bad_indexes[i]))

    # Insert data to our DF
    for i in range(last_flight_index):
        try:
            df.loc[i, 'departure_time'] = dep_times_list[i]
        except Exception as e:
            pass
        try:
            df.loc[i, 'arrival_time'] = arr_times_list[i]
        except Exception as e:
            pass
        try:
            df.loc[i, 'airline'] = airlines_list[i]
        except Exception as e:
            pass
        try:
            df.loc[i, 'duration'] = durations_list[i]
        except Exception as e:
            pass
        try:
            df.loc[i, 'stops'] = stops_list[i]
        except Exception as e:
            pass
        try:
            df.loc[i, 'layovers'] = layovers_list[i]
        except Exception as e:
            pass
        try:
            df.loc[i, 'price'] = price_list[i]
        except Exception as e:
            pass
        try:
            # Adding flight details data
            number_element_to_ignore = AddingFlightDetails(i, stops_list, bad_indexes, number_element_to_ignore)
        except Exception as e:
            pass


def GetPathForExcelsOutPut(journeyDetails,i):
    dep_arr_name = journeyDetails.at[i,'dep_country_chooser'] + "_" + journeyDetails.at[i,'arrival_country_chooser']
    sampleTime   = "sampleTime_" + str(pd.to_datetime('today').strftime("%d/%m/%Y")).replace("/", "_")
    dep_date     = str("%02d" % journeyDetails.at[i,'dep_month']) + "_" + str("%02d" % journeyDetails.at[i,'dep_day']) + "_" + str(journeyDetails.at[i,'dep_year'])
    arr_date     = str("%02d" % journeyDetails.at[i,'arr_month']) + "_" + str("%02d" % journeyDetails.at[i,'arr_day']) + "_" + str(journeyDetails.at[i,'arr_year'])
    conc_date    = "depDate_" + dep_date + "_arrDate_" + arr_date
    data_path = "C:\\Users\\guypa\\Desktop\\Output"
    folderPath   = os.path.join(data_path, dep_arr_name, conc_date, 'sampleTime\\')
    return [folderPath, conc_date]


def checkPathExist(journeyDetails,i):
    desirePath = GetPathForExcelsOutPut(journeyDetails,i) # get path or create one if it still doesn't exist
    newpath = desirePath[0]
    if not os.path.exists(newpath):
        os.makedirs(newpath)


def ChooseFlight(journeyDetails, i):
    link = 'https://www.expedia.com'
    browser.get(link)
    time.sleep(5)


    # Choose flights only mode
    flights_only = browser.find_element_by_xpath("//*[@id='uitk-tabs-button-container']/li[2]/a")
    flights_only.click()
    one_trip = browser.find_element(By.XPATH, "//*[@id='uitk-tabs-button-container']/div/li[2]")
    one_trip.click()

    # Scrape details according to journeyDetails df
    dep_country_chooser(journeyDetails.at[i, 'dep_country_chooser'])
    arrival_country_chooser(journeyDetails.at[i, 'arrival_country_chooser'])
    dep_date_chooser(("%02d" % journeyDetails.at[i, 'dep_month']), ("%02d" % journeyDetails.at[i, 'dep_day']),
                     journeyDetails.at[i, 'dep_year'])
    time.sleep(2)
    return_date_chooser(("%02d" % journeyDetails.at[i, 'arr_month']), ("%02d" % journeyDetails.at[i, 'arr_day']),
                        journeyDetails.at[i, 'arr_year'])
    time.sleep(5)
    #search()
    # This point we have the desire results on web, now we just need to gather the data.
    time.sleep(10)


def GetReturnDateUsingFolderName(text) :
    match = re.search(r'\d{2}_\d{2}_\d{4}$', text)
    print(match)
    date = dt.datetime.strptime(match.group(),  '%m_%d_%Y').date()
    return date


def GetDepartDateUsingFolderName(text) :
    match = re.search(r'\d{2}_\d{2}_\d{4}', text)
    date = dt.datetime.strptime(match.group(),  '%m_%d_%Y').date()
    return date


def AmendTimeAndDate():
    df['time'] = pd.to_datetime('today').strftime('%H:%M:%S')
    df['date'] = pd.to_datetime('today').strftime("%m/%d/%Y")


def SaveDfToCsv(journeyDetails,i):
    checkPathExist(journeyDetails,i)
    [pathForDepArrDate, nameOfFolder] = GetPathForExcelsOutPut(journeyDetails,i)
    df['departure_date'] = GetDepartDateUsingFolderName(nameOfFolder) # send file path to function
    df['arrival_date'] = GetReturnDateUsingFolderName(nameOfFolder) # send file path to function
    df.to_csv(str(GetPathForExcelsOutPut(journeyDetails,i)[0]) + "_" + dt.datetime.today().strftime('%y%m%d-%H%M%S')+ ".csv", index = False)


def ProcessJourney(journeyDetails, i):
    ChooseFlight(journeyDetails, i)
    DataProcessing()
    AmendTimeAndDate()
    SaveDfToCsv(journeyDetails,i)


journeys_path = "./scrap_input.csv"
df_journeys = pd.read_csv(journeys_path)
start_global_time = time.time()
for i, row in df_journeys.iterrows():
    start_time = time.time()
    try:
        ProcessJourney(df_journeys.loc[[i]],i)
    except (selexcept.NoSuchElementException, selexcept.StaleElementReferenceException) :
        # Handling internet connection issues
        pass
    time.sleep(5)