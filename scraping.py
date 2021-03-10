import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import TimeoutException
import pandas as pd


usernameStr = 'username'
passwordStr = 'password'

browser = webdriver.Chrome('chromedriver')
browser.get(('url'))
all_cookies = browser.get_cookies()
file = open('cookies.txt', 'w')
cookies = str(all_cookies)
file.write(cookies)
file.close()

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

""""""
# gotItButton = WebDriverWait(browser, 15).until(
#     expected_conditions.element_to_be_clickable((By.ID, "ed8a0b24-aad6-30ff-4a0a-fb8948de5007")))
# gotItButton.click()

'''parsing site'''
browser.get(('url'))
# Wait 20 seconds for page to load
timeout = 10
try:
    WebDriverWait(browser, timeout).until(expected_conditions.visibility_of_element_located((By.XPATH, "//img[@class='imageset-thumb']")))
except TimeoutException:
    print("Timed out waiting for page to load")
    browser.quit()

page = browser.find_elements_by_id("ext-comp-1007")
page_numb = 0
for i in page:
    # print(i.text)
    a = i.text.split()
    page_numb = int(a[1])
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
    dealer = [x.text for x in dlr_name]
    # print('dealer name:', dealer)

    last_money_change = browser.find_elements_by_xpath("//div[@class='x-grid3-cell-inner x-grid3-col-3']")
    change = [x.text for x in last_money_change]
    # print('last $ change:', change)

    year_element = browser.find_elements_by_xpath("//div[@class='YearMakeModel']")
    year = [x.text for x in year_element]
    # print('year:', year)

    ae = browser.find_elements_by_xpath("//div[@class='x-grid3-cell-inner x-grid3-col-5']")
    lifetime = [x.text for x in ae]
    # print('age:', lifetime)

    pr = browser.find_elements_by_xpath("//div[@class='Price']")
    money = [x.text for x in pr]
        # print('price:', money)

    make = browser.find_elements_by_xpath("//div[@class='x-grid3-cell-inner x-grid3-col-7']")
    model = [x.text for x in make]
        # print('make/model:', model)

    mkt_days_supply = browser.find_elements_by_xpath("//div[@class='x-grid3-cell-inner x-grid3-col-8']")
    rang = [x.text for x in mkt_days_supply]
        # print('mkt days supply/rank:', rang)

    adjusted_percent = browser.find_elements_by_xpath("//div[@class='x-grid3-cell-inner x-grid3-col-9']")
    percent = [x.text for x in adjusted_percent]
        # print('adjusted % of market:', percent)

    price = browser.find_elements_by_xpath("//div[@class='x-grid3-cell-inner x-grid3-col-10']")
    percent_of_mkt = [x.text for x in price]
        # print('price/% of mkt:', percent_of_mkt)

    amount = browser.find_elements_by_xpath("//div[@class='x-grid3-cell-inner x-grid3-col-11']")
    amnt = [x.text for x in amount]
        # print('amount:', amnt)

    tg = browser.find_elements_by_xpath("//div[@class='x-grid3-cell-inner x-grid3-col-12']")
    tag = [x.text for x in tg]
            # print('tags:', tag)

    autotrader = browser.find_elements_by_xpath("//div[@class='x-grid3-cell-inner x-grid3-col-13']")
    site = [x.text for x in autotrader]
        # print('AutoTrader.com:', site)

    carscom = browser.find_elements_by_xpath("//div[@class='x-grid3-cell-inner x-grid3-col-14']")
    s = [x.text for x in carscom]
        # print('Cars.com:', s)

    make = browser.find_elements_by_xpath("//div[@class='x-grid3-cell-inner x-grid3-col-15']")
    mk = [x.text for x in make]
        # print('make:', mk)

    df = pd.DataFrame({
        'dealer name': dealer,
        'last $ change': change,
        'year': year,
        'age': lifetime,
        'price': model,
        'make/model': model,
        'mkt days supply/rank': rang,
        'adjusted % of market': percent,
        'price/% of mkt': percent_of_mkt,
        'amount': amnt,
        'tags': tag,
        'AutoTrader.com': site,
        'Cars.com': s,
        'make': mk,
    })
    print(df.info())
    file_name = "page" + str(number+1) + ".json"
    df.to_json(file_name, index=True)
    next = browser.find_element_by_xpath("//button[@id='ext-gen41']").click()
    time.sleep(15)
