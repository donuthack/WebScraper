import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

global cookies


def authorization():
    usernameStr = 'harperreed'
    passwordStr = '1qaz!QAZ'

    driver = webdriver.ChromeOptions()
    driver.add_argument('headless')
    browser = webdriver.Chrome('/Users/workplace/Downloads/chromedriver 2', options=driver)
    browser.get(('https://vauto.signin.coxautoinc.com/?solutionID=VAT_prod&clientId=68e5c360aa114799a67e94c4d587ff65'))

    username = browser.find_element_by_t('username')
    username.send_keys(usernameStr)
    print(1)
    time.sleep(5)

    nextButton = browser.find_element_by_id('signIn')
    nextButton.click()
    print(2)
    time.sleep(5)

    password = WebDriverWait(browser, 5).until(
        expected_conditions.element_to_be_clickable((By.NAME, "password")))
    password.click()
    print(3)
    password.send_keys(passwordStr)

    signInButton = browser.find_element_by_id('signIn')
    signInButton.click()
    print(4)
    time.sleep(20)

    remind_me_later = browser.find_element_by_xpath("/html/body/div/div/div/div/div[1]/div[3]/a")
    remind_me_later.click()
    time.sleep(10)

    all_cookies = browser.get_cookies()

    return all_cookies
