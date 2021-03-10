import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import pandas as pd
import json

usernameStr = 'username'
passwordStr = 'password'

browser = webdriver.Chrome('chromedriver')
browser.get(('you url'))
all_cookies = browser.get_cookies()
file = open('cookies.txt', 'w')
cookies = str(all_cookies)
file.write(cookies)
file.close()
# print(all_cookies)

username = browser.find_element_by_id('username')
username.send_keys(usernameStr)

nextButton = browser.find_element_by_id('signIn')
nextButton.click()

password = WebDriverWait(browser, 10).until(
    expected_conditions.element_to_be_clickable((By.NAME, "password")))
password.click()
password.send_keys(passwordStr)

signInButton = browser.find_element_by_id('signIn')
signInButton.click()
time.sleep(10)

# gotItButton = WebDriverWait(browser, 15).until(
#     expected_conditions.element_to_be_clickable((By.ID, "ed8a0b24-aad6-30ff-4a0a-fb8948de5007")))
# gotItButton.click()
'''parsing site'''
browser.get(('your url to parse'))
# Wait 20 seconds for page to load
try:
    WebDriverWait(browser, 20).until(expected_conditions.visibility_of_element_located((By.XPATH, "//img[@class='imageset-thumb']")))
except TimeoutException:
    print("Timed out waiting for page to load")
    browser.quit()

page = browser.find_elements_by_id("ext-comp-1007")
page_numb = 0
for i in page:
    # print(i.text)
    a = i.text.split()
    page_numb = int(a[1])
# print(1, page_numb)

dealers = []
last_changes = []
years = []
lifetimes = []
moneys = []
models = []
rangs = []
percents = []
percents_of_mkt = []
amounts = []
tags = []
sites = []
ss = []
makes = []

try:
    WebDriverWait(browser, 15).until(
        expected_conditions.visibility_of_element_located((By.XPATH, "//img[@class='imageset-thumb']")))
except TimeoutException:
    print("Timed out waiting for page to load")
    browser.quit()
time.sleep(20)
for number in range(page_numb):
    time.sleep(15)
    dlr_name = browser.find_elements_by_xpath("//div[@class='x-grid3-cell-inner x-grid3-col-2']")
    # dealer = [x.text for x in dlr_name]
    for i in dlr_name:
        dealers.append(i.text)
    # print('dealer name:', dealer)

    last_money_change = browser.find_elements_by_xpath("//div[@class='x-grid3-cell-inner x-grid3-col-3']")
    # change = [x.text for x in last_money_change]
    # print('last $ change:', change)
    for i in last_money_change:
        last_changes.append(i.text)

    year_element = browser.find_elements_by_xpath("//div[@class='YearMakeModel']")
    # year = [x.text for x in year_element]
    # print('year:', year)
    for i in year_element:
        years.append(i.text)

    ae = browser.find_elements_by_xpath("//div[@class='x-grid3-cell-inner x-grid3-col-5']")
    # lifetime = [x.text for x in ae]
    # print('age:', lifetime)
    for i in ae:
        lifetimes.append(i.text)

    pr = browser.find_elements_by_xpath("//div[@class='Price']")
    # money = [x.text for x in pr]
    # print('price:', money)
    for i in pr:
        moneys.append(i.text)

    make = browser.find_elements_by_xpath("//div[@class='x-grid3-cell-inner x-grid3-col-7']")
    # model = [x.text for x in make]
    # print('make/model:', model)
    for i in make:
        models.append(i.text)

    mkt_days_supply = browser.find_elements_by_xpath("//div[@class='x-grid3-cell-inner x-grid3-col-8']")
    # rang = [x.text for x in mkt_days_supply]
    # print('mkt days supply/rank:', rang)
    for i in mkt_days_supply:
        rangs.append(i.text)

    adjusted_percent = browser.find_elements_by_xpath("//div[@class='x-grid3-cell-inner x-grid3-col-9']")
    # percent = [x.text for x in adjusted_percent]
    # print('adjusted % of market:', percent)
    for i in adjusted_percent:
        percents.append(i.text)

    price = browser.find_elements_by_xpath("//div[@class='x-grid3-cell-inner x-grid3-col-10']")
    # percent_of_mkt = [x.text for x in price]
    # print('price/% of mkt:', percent_of_mkt)
    for i in price:
        percents_of_mkt.append(i.text)

    amount = browser.find_elements_by_xpath("//div[@class='x-grid3-cell-inner x-grid3-col-11']")
    # amnt = [x.text for x in amount]
    # print('amount:', amnt)
    for i in amount:
        amounts.append(i.text)

    tg = browser.find_elements_by_xpath("//div[@class='x-grid3-cell-inner x-grid3-col-12']")
    # tag = [x.text for x in tg]
    # print('tags:', tag)
    for i in tg:
        tags.append(i.text)

    autotrader = browser.find_elements_by_xpath("//div[@class='x-grid3-cell-inner x-grid3-col-13']")
    # site = [x.text for x in autotrader]
    # print('AutoTrader.com:', site)
    for i in autotrader:
        sites.append(i.text)

    carscom = browser.find_elements_by_xpath("//div[@class='x-grid3-cell-inner x-grid3-col-14']")
    # s = [x.text for x in carscom]
    # print('Cars.com:', s)
    for i in carscom:
        ss.append(i.text)

    make = browser.find_elements_by_xpath("//div[@class='x-grid3-cell-inner x-grid3-col-15']")
    # mk = [x.text for x in make]
    # print('make:', mk)
    for i in make:
        makes.append(i.text)

    next = browser.find_element_by_xpath("//button[@id='ext-gen41']").click()
    time.sleep(15)

    data_array = []

    for dlr_name, money_change, car_year, lifetime_car, price, model, mkt, adj_perc, perc, amnt, tg, atdotcom, carsdotcom, mk in zip(dealers, last_changes, years, lifetimes, moneys, models, rangs, percents, percents_of_mkt, amounts, tags, sites, ss, makes):
        data_array.append({
            'dealer_name': dlr_name,
            'last $ change': money_change,
            'year': car_year,
            'age': lifetime_car,
            'price': price,
            'make/model': model,
            'mkt days supply/rank': mkt,
            'adjusted % of market': adj_perc,
            'price/% of mkt': perc,
            'amount': amnt,
            'tags': tg,
            'AutoTrader.com': atdotcom,
            'Cars.com': carsdotcom,
            'make': mk
        })
data = pd.DataFrame(data_array)
print(data.info())
data.to_json("result.json", index=True)

