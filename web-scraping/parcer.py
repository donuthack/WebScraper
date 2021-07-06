import time
from selenium import webdriver, common
import traceback
import os

from selenium.webdriver import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions, wait
from selenium.common.exceptions import TimeoutException, ElementNotVisibleException, NoSuchElementException, \
    StaleElementReferenceException, NoSuchWindowException, WebDriverException

usernameStr = 'eldar'
# usernameStr = 'harperreed'
passwordStr = '1qaz!QAZ'
# passwordStr = '1qaz!QAZ'

browser = webdriver.Chrome('/Users/workplace/Downloads/chromedriver')
browser.get(('https://vauto.signin.coxautoinc.com/?solutionID=VAT_prod&clientId=68e5c360aa114799a67e94c4d587ff65'))
all_cookies = browser.get_cookies()
file = open('cookies.txt', 'w')
cookies = str(all_cookies)
file.write(cookies)
file.close()

username = browser.find_element_by_id('username')
username.send_keys(usernameStr)
time.sleep(5)

nextButton = browser.find_element_by_id('signIn')
nextButton.click()
time.sleep(5)

password = WebDriverWait(browser, 5).until(
    expected_conditions.element_to_be_clickable((By.NAME, "password")))
password.click()
password.send_keys(passwordStr)

signInButton = browser.find_element_by_id('signIn')
signInButton.click()
time.sleep(10)

'''parsing site'''
browser.get(('https://www2.vauto.com/Va/Inventory/Default.aspx?uq=1'))


def parsing_loop():
    global machine
    frame = "GaugePageIFrame"
    outer_tabs = "outerTabs"
    gauge_page_main = "ext-comp-1002"
    wrap_of_iframe = "x-panel-bwrap"
    panel_wrap_of_iframe = "ext-gen20"
    container_of_choices_and_description = "gauge-page-tabs"
    vehicle_attributes_and_description = "x-tab-panel-bwrap"
    pricing_active_button = "x-tab-strip-active"

    ext_gen12 = browser.find_element_by_id("ext-gen12")
    vehicle_grid_container = browser.find_element_by_id("vehicle-grid-container")
    ext_gen13 = browser.find_element_by_id("ext-gen13")
    ext_gen16 = browser.find_element_by_class_name("x-panel-bbar-noborder")
    ext_comp_1003 = browser.find_element_by_id("ext-comp-1003")
    table = browser.find_element_by_tag_name("table")
    tbody = browser.find_element_by_tag_name("tbody")
    tr = browser.find_element_by_tag_name("tr")
    x_toolbar_left = browser.find_element_by_class_name("x-toolbar-left")
    table = browser.find_element_by_tag_name("table")
    tbody = browser.find_element_by_tag_name("tbody")
    x_toolbar_left_row = browser.find_element_by_class_name("x-toolbar-left-row")
    ext_gen37 = browser.find_element_by_id("ext-gen37")
    time.sleep(20)
    result = browser.find_element_by_id("ext-comp-1007")
    time.sleep(10)
    page_numb = 0
    for i in result.text:
        print(12, i)
        a = result.text.split()
        page_numb = int(a[1])
    print(62, page_numb)

    pageSizeSelect = browser.find_element_by_xpath(
        "/html/body/form/div[4]/div/div[1]/div/div[6]/div[1]/div[1]/div[3]/div/table/tbody/tr/td[1]/table/tbody/tr/td[12]/div/input")
    amount = int(pageSizeSelect.get_attribute('value'))
    ext_gen_25 = browser.find_element_by_class_name("x-grid3-body")
    time.sleep(10)
    x_grid3_row_first = browser.find_element_by_class_name("x-grid3-row-table")
    x_grid3_td_8 = browser.find_element_by_class_name("x-grid3-td-8")
    x_grid3_col_8 = browser.find_element_by_class_name("x-grid3-col-8")
    print(73, page_numb)
    for j in range(1, page_numb + 1):
        # time.sleep(20)
        for i in range(1, amount + 1):
            columnt_field = WebDriverWait(browser, 300).until(expected_conditions.visibility_of_element_located(
                (By.XPATH, "//*[@id='ext-gen25']/div[" + str(i) + "]/table/tbody/tr/td[9]/div/div[2]")))
            if columnt_field.text.split()[3] != "Unranked":
                try:
                    machine = WebDriverWait(browser, 300).until(expected_conditions.visibility_of_element_located(
                        (By.XPATH,
                         "//*[@id='ext-gen25']/div[" + str(i) + "]/table/tbody/tr/td[5]/div/div[1]")))
                    a = machine.find_element_by_tag_name("a").get_attribute("href")
                    print("A", a)
                    browser.execute_script("window.open('" + a + "');")
                    time.sleep(10)
                    # handles = browser.window_handles
                    print("CAR NAME", a)
                    print("Car", browser.title)
                    print(browser.window_handles)
                    browser.switch_to.window(browser.window_handles[1])

                # WebDriverWait(browser, 30).until(
                #     expected_conditions.frame_to_be_available_and_switch_to_it(frame))
                # print("Activate frame")
                # time.sleep(10)
                    try:
                        WebDriverWait(browser, 10).until(
                            expected_conditions.visibility_of_element_located((By.ID, outer_tabs)))
                        print("Activate outerTabs")
                    except TimeoutException:
                        print("Timed out waiting for page to find outerTabs element")
                        browser.quit()
                    except StaleElementReferenceException as e:
                        print(e.msg)
                    try:
                        WebDriverWait(browser, 5).until(
                            expected_conditions.visibility_of_element_located((By.ID, gauge_page_main)))
                        print("Activate ext-comp-1002")
                    except TimeoutException:
                        print("Timed out waiting for page to find ext-comp-1002")
                        browser.quit()

                    try:
                        WebDriverWait(browser, 5).until(
                            expected_conditions.visibility_of_element_located((By.ID, "ext-gen19")))
                        print("Activate x-panel-bwrap")
                    except TimeoutException:
                        print("Timed out waiting for page to find x-panel-bwrap")
                        browser.quit()
                    try:
                        WebDriverWait(browser, 20).until(
                            expected_conditions.visibility_of_element_located((By.CLASS_NAME, "x-panel-body-noborder")))
                        print("Activate ext-gen20")
                    except TimeoutException:
                        print("Timed out waiting for page to find ext-gen20")
                        browser.quit()

                    try:
                        WebDriverWait(browser, 20).until(
                            expected_conditions.visibility_of_element_located(
                                (By.ID, container_of_choices_and_description)))
                        print("Activate gauge-page-tabs")
                    except TimeoutException:
                        print("Timed out waiting for page to find gauge-page-tabs")
                        browser.quit()

                    try:
                        WebDriverWait(browser, 20).until(
                            expected_conditions.visibility_of_element_located(
                                (By.CLASS_NAME, vehicle_attributes_and_description)))
                        print("Activate x-tab-panel-bwrap")
                    except TimeoutException:
                        print("Timed out waiting for page to find x-tab-panel-bwrap")
                        browser.quit()

                    try:
                        WebDriverWait(browser, 20).until(
                            expected_conditions.visibility_of_element_located(
                                (By.ID, "ext-gen32")))
                        print("Activate ext-gen32")
                    except TimeoutException:
                        print("Timed out waiting for page to find gauge-page-tabs")
                        browser.quit()

                    try:
                        pricing = WebDriverWait(browser, 60).until(
                            expected_conditions.visibility_of_element_located(
                                (By.XPATH, "//*[@id='gauge-page-tabs__pricing']")))
                    except TimeoutException:
                        close = WebDriverWait(browser, 60).until(expected_conditions.element_to_be_clickable(
                            (By.XPATH, "//a[contains(@onclick,'vauto.ranking.GaugePage.onCloseClick()')]")))
                        close.click()
                        print("1, Wait for closing")
                        continue
                    except common.exceptions.NoSuchElementException:
                        close = WebDriverWait(browser, 60).until(expected_conditions.element_to_be_clickable(
                            (By.XPATH, "//a[contains(@onclick,'vauto.ranking.GaugePage.onCloseClick()')]")))
                        close.click()
                        print("2 ,Wait for closing")
                        continue
                    try:
                        pricing.click()
                    except WebDriverException:
                        continue

                    print("Activate gauge-page-tabs__pricing")
                    try:
                        WebDriverWait(browser, 5).until(
                            expected_conditions.visibility_of_element_located(
                                (By.CLASS_NAME, pricing_active_button)))
                    except TimeoutException:
                        print("Timed out waiting for page to find x-tab-strip-active")
                        browser.quit()

                    try:
                        ext_container_1028 = WebDriverWait(browser, 60).until(
                            expected_conditions.visibility_of_element_located((By.LINK_TEXT, 'Competitive Set')))
                        print(1, ext_container_1028.text)
                        ext_container_1028.click()
                    except TimeoutException:
                        print("Timed out waiting for page to find Competitive Set")
                        browser.quit()

                    time.sleep(5)

                    button = browser.find_element_by_xpath(
                        "/html/body/form/div[4]/div/div[1]/div/div/div/div/div/div[2]/div[2]/div[1]/div/div/div/div[2]/div/div[2]/div[2]/div/div[2]/div/div/div[1]/div/table/tbody/tr/td[2]/table/tbody/tr/td[1]/table/tbody/tr/td/table/tbody/tr[2]/td[2]/em/button")
                    time.sleep(5)
                    button.click()
                    Alert(browser).accept()
                    time.sleep(5)

                    div_1027 = browser.find_element_by_class_name("x-box-item")

                    pricing_left_panel = browser.find_element_by_class_name("MediumBlue")

                    vin = browser.find_element_by_id("VIN")
                    print(vin.text)
                    time.sleep(10)

                    stock = browser.find_element_by_id("StockNumber")
                    print(stock.text)
                    time.sleep(10)

                    filepath = '/Users/workplace/Downloads'
                    filename = max([filepath + "/" + f for f in os.listdir(filepath)], key=os.path.getctime)
                    new_filename = vin.text + stock.text + ".xls"
                    os.rename(os.path.join(filepath, filename), os.path.join(filepath, new_filename))
                    time.sleep(30)

                    close = WebDriverWait(browser, 60).until(expected_conditions.element_to_be_clickable(
                        (By.XPATH, "//a[contains(@onclick,'vauto.ranking.GaugePage.onCloseClick()')]")))
                    close.click()
                    print("you clicked")
                    time.sleep(10)

                    x = WebDriverWait(browser, 50).until(expected_conditions.visibility_of_element_located(
                        (By.ID, "ext-gen3")))
                    print("Activated x")

                    cancel = WebDriverWait(browser, 50).until(expected_conditions.visibility_of_element_located(
                        (By.ID, "saveAndCloseWindow")))
                    print("Activating save changes, yay!")

                    container_footer = WebDriverWait(browser, 50).until(
                        expected_conditions.visibility_of_element_located(
                            (By.XPATH, "//button[text()='No']"))).click()
                    print("Clicked No, yay!")
                    time.sleep(20)
                except NoSuchElementException:
                    pass

    ext_gen16 = browser.find_element_by_id("ext-gen16")
    ext_comp_1003 = browser.find_element_by_id("ext-comp-1003")
    x_toolbar_ct = browser.find_element_by_class_name("x-toolbar-ct")
    x_toolbar_left = browser.find_element_by_class_name("x-toolbar-left")
    x_toolbar_left_row = browser.find_element_by_class_name("x-toolbar-left-row")
    ext_gen40 = browser.find_element_by_id("ext-gen40")
    ext_comp_1008 = browser.find_element_by_id("ext-comp-1008")
    x_btn_icon_small_left = browser.find_element_by_class_name("x-btn-icon-small-left")
    tag = browser.find_element_by_tag_name("tr")
    x_btn_mc = browser.find_element_by_class_name("x-btn-mc")
    x_unselectable = browser.find_element_by_class_name("x-unselectable")
    time.sleep(20)
    ext_gen41 = browser.find_element_by_id("ext-gen41")
    time.sleep(10)
    ext_gen41.click()


parsing_loop()
