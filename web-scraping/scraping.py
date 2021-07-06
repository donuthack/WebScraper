import time
from selenium import webdriver, common
import traceback
import os
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions, wait
from selenium.common.exceptions import TimeoutException, ElementNotVisibleException, NoSuchElementException, \
    StaleElementReferenceException

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
time.sleep(15)

nextButton = browser.find_element_by_id('signIn')
nextButton.click()
time.sleep(15)

password = WebDriverWait(browser, 15).until(
    expected_conditions.element_to_be_clickable((By.NAME, "password")))
password.click()
password.send_keys(passwordStr)

signInButton = browser.find_element_by_id('signIn')
signInButton.click()
time.sleep(15)

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
    vehicle_attributes_and_description_without_footer = "x-tab-panel-body-top"
    pricing_div_container = "pricing"
    pricing_div_conatiner_inner = "ext-container-1144"
    competitive_criteria_div = "x-box-item"
    pricing_left_pannel = "pricingLeftPanel"
    left_panel_container_content = "pricingLeftPanel"
    pricing_active_button = "x-tab-strip-active"
    while True:
        print("START")
        try:
            i = 1
            while i < 20:
                try:
                    print("Search for machine")
                    machine = WebDriverWait(browser, 60).until(EC.visibility_of_element_located(
                        (By.XPATH, "//*[@id='ext-gen25']/div[" + str(i) + "]/table/tbody/tr/td[5]/div/div[1]/a/div")))
                    # machine = WebDriverWait(browser, 60).until(expected_conditions.visibility_of_element_located(
                    #     (By.XPATH, "//*[@id='ext-gen25']/div[78]/table/tbody/tr/td[5]/div/div[1]/a/div")))
                    print("Car", machine.text)
                except:
                    print("last car reached")
                    pass
                i += 1
                print("car ", i)
                time.sleep(15)
                machine.click()
                print("car clicked!")
                print("search for iframe")
                WebDriverWait(browser, 30).until(
                    expected_conditions.frame_to_be_available_and_switch_to_it(frame))
                print("Activate frame")
                time.sleep(10)
                try:
                    WebDriverWait(browser, 20).until(
                        expected_conditions.visibility_of_element_located((By.ID, outer_tabs)))
                    print("Activate outerTabs")
                except TimeoutException:
                    print("Timed out waiting for page to find outerTabs element")
                    browser.quit()
                except StaleElementReferenceException as e:
                    print(e.msg)
                time.sleep(10)

                try:
                    WebDriverWait(browser, 30).until(
                        expected_conditions.visibility_of_element_located((By.ID, gauge_page_main)))
                    print("Activate ext-comp-1002")
                except TimeoutException:
                    print("Timed out waiting for page to find ext-comp-1002")
                    browser.quit()
                time.sleep(10)

                try:
                    WebDriverWait(browser, 30).until(
                        expected_conditions.visibility_of_element_located((By.CLASS_NAME, wrap_of_iframe)))
                    print("Activate x-panel-bwrap")
                except TimeoutException:
                    print("Timed out waiting for page to find x-panel-bwrap")
                    browser.quit()
                time.sleep(10)

                try:
                    WebDriverWait(browser, 30).until(
                        expected_conditions.visibility_of_element_located((By.ID, panel_wrap_of_iframe)))
                    print("Activate ext-gen20")
                except TimeoutException:
                    print("Timed out waiting for page to find ext-gen20")
                    browser.quit()
                time.sleep(10)

                try:
                    WebDriverWait(browser, 30).until(
                        expected_conditions.visibility_of_element_located(
                            (By.ID, container_of_choices_and_description)))
                    print("Activate gauge-page-tabs")
                except TimeoutException:
                    print("Timed out waiting for page to find gauge-page-tabs")
                    browser.quit()
                time.sleep(10)

                try:
                    WebDriverWait(browser, 30).until(
                        expected_conditions.visibility_of_element_located(
                            (By.CLASS_NAME, "x-tab-strip-wrap")))
                    print("Activate x-tab-strip-wrap")
                except TimeoutException:
                    print("Timed out waiting for page to find x-tab-panel-bwrap")
                    browser.quit()
                time.sleep(10)

                try:
                    WebDriverWait(browser, 40).until(
                        expected_conditions.visibility_of_element_located(
                            (By.CLASS_NAME, "x-tab-strip-top")))
                    print("Activate x-tab-strip x-tab-strip-top")
                except TimeoutException:
                    print("Timed out waiting for page to find x-tab-panel-body-top")
                    browser.quit()
                time.sleep(10)
                try:
                    WebDriverWait(browser, 40).until(
                        expected_conditions.visibility_of_element_located(
                            (By.ID, "gauge-page-tabs__pricing"))).click()
                    print("Activate gauge-page-tabs__pricing")

                    try:
                        WebDriverWait(browser, 30).until(
                            expected_conditions.visibility_of_element_located(
                                (By.CLASS_NAME, "x-tab-right")))
                        print("Activate x-tab-right")
                    except TimeoutException:
                        print("Timed out waiting for page to find x-tab-panel-body-top")
                        browser.quit()
                    time.sleep(10)

                    try:
                        ext_container_1028 = WebDriverWait(browser, 30).until(
                            expected_conditions.visibility_of_element_located((By.LINK_TEXT, 'Competitive Set')))
                        print(1, ext_container_1028.text)
                        ext_container_1028.click()
                    except TimeoutException:
                        print("Timed out waiting for page to find Competitive Set")
                        browser.quit()
                    time.sleep(10)
                    try:
                        WebDriverWait(browser, 30).until(
                            expected_conditions.visibility_of_element_located((By.CLASS_NAME, wrap_of_iframe)))
                        print("Activate x-panel-bwrap")
                    except TimeoutException:
                        print("Timed out waiting for page to find x-panel-bwrap")
                        browser.quit()
                    time.sleep(10)
                    try:
                        WebDriverWait(browser, 30).until(
                            expected_conditions.visibility_of_element_located((By.ID, panel_wrap_of_iframe)))
                        print("Activate ext-gen20")
                    except TimeoutException:
                        print("Timed out waiting for page to find ext-gen20")
                        browser.quit()
                    time.sleep(10)
                    try:
                        WebDriverWait(browser, 30).until(
                            expected_conditions.visibility_of_element_located(
                                (By.ID, container_of_choices_and_description)))
                        print("Activate gauge-page-tabs")
                    except TimeoutException:
                        print("Timed out waiting for page to find gauge-page-tabs")
                        browser.quit()
                    time.sleep(10)
                    try:
                        WebDriverWait(browser, 30).until(
                            expected_conditions.visibility_of_element_located(
                                (By.CLASS_NAME, vehicle_attributes_and_description)))
                        print("Activate x-tab-panel-bwrap")
                    except TimeoutException:
                        print("Timed out waiting for page to find x-tab-panel-bwrap")
                        browser.quit()
                    time.sleep(10)
                    try:
                        WebDriverWait(browser, 30).until(
                            expected_conditions.visibility_of_element_located(
                                (By.CLASS_NAME, vehicle_attributes_and_description_without_footer)))
                        print("Activate x-tab-panel-body-top")
                    except TimeoutException:
                        print("Timed out waiting for page to find x-tab-panel-body-top")
                        browser.quit()
                    try:
                        WebDriverWait(browser, 30).until(
                            expected_conditions.visibility_of_element_located(
                                (By.CLASS_NAME, competitive_criteria_div)))
                        print("Activate x-box-item")
                    except TimeoutException:
                        print("Timed out waiting for page to find x-box-item")
                        browser.quit()

                    try:
                        WebDriverWait(browser, 30).until(
                            expected_conditions.visibility_of_element_located((By.ID, "pricingLeftPanel")))
                        print("Activate pricingLeftPanel")
                    except TimeoutException:
                        print("Timed out waiting for page to find pricingLeftPanel")
                        browser.quit()
                    time.sleep(20)
                    try:
                        WebDriverWait(browser, 30).until(
                            expected_conditions.visibility_of_element_located(
                                (By.CLASS_NAME, "rcp-content")))
                        print("Activate rcp-content")
                    except TimeoutException:
                        print("Timed out waiting for page to find rcp-content")
                        browser.quit()
                    time.sleep(20)
                    '''Left Sided pricing container'''
                    try:
                        WebDriverWait(browser, 30).until(
                            expected_conditions.visibility_of_element_located(
                                (By.ID, "RefineSetContainer")))
                        print("Activate RefineSetContainer")
                    # refine_set_container = browser.find_element_by_class_name("RefineSetContainer")
                    except TimeoutException:
                        print("Timed out waiting for page to find RefineSetContainer")
                        browser.quit()

                    time.sleep(20)

                    try:
                        '''Distance container div'''
                        WebDriverWait(browser, 30).until(
                            expected_conditions.visibility_of_element_located(
                                (By.CLASS_NAME, "DistanceSection")))
                        # distance_section = browser.find_element_by_class_name("DistanceSection")
                        time.sleep(20)
                    except TimeoutException:
                        print("Timed out waiting for page to find DistanceSection")
                        browser.quit()

                    '''Distance and miles reflection'''
                    WebDriverWait(browser, 30).until(
                        expected_conditions.visibility_of_element_located(
                            (By.CLASS_NAME, "DistanceSectionBody")))
                    # table = browser.find_element_by_class_name("DistanceSectionBody")
                    time.sleep(20)
                    '''Distance dropdown with values'''
                    distance_drop_down = WebDriverWait(browser, 30).until(
                        expected_conditions.visibility_of_element_located(
                            (By.CLASS_NAME, "DistanceDropDown")))
                    # distance_drop_down = browser.find_element_by_class_name("DistanceDropDown")
                    distance_drop_down.click()
                    time.sleep(20)
                    '''List with all values from imaginative dropdown'''
                    x_combo = WebDriverWait(browser, 30).until(
                        expected_conditions.visibility_of_element_located(
                            (By.XPATH, "//div[contains(text(), '(Auto)')]")))
                    x_combo.click()

                    ext_gen328 = browser.find_element_by_class_name("x-tab-panel-bwrap")

                    ext_gen329 = browser.find_element_by_class_name("x-tab-panel-body-top")

                    vechiclesTab = browser.find_element_by_class_name("va-competitivevehiclesgrid-renderTo")

                    ext_gen351 = browser.find_element_by_class_name("x-panel-bwrap")

                    ext_gen352 = browser.find_element_by_tag_name("em").click()
                    time.sleep(10)

                    # button = browser.find_element_by_tag_name("button")
                    # time.sleep(10)
                    # button.click()
                    # Alert(browser).accept()
                    # time.sleep(20)

                    div_1027 = browser.find_element_by_class_name("x-box-item")

                    pricing_left_panel = browser.find_element_by_class_name("MediumBlue")

                    vin = browser.find_element_by_id("VIN")
                    print(vin.text)
                    time.sleep(20)

                    stock = browser.find_element_by_id("StockNumber")
                    print(stock.text)
                    time.sleep(20)

                    filepath = '/Users/workplace/Downloads'
                    filename = max([filepath + "/" + f for f in os.listdir(filepath)], key=os.path.getctime)
                    new_filename = vin.text + stock.text + ".xls"
                    os.rename(os.path.join(filepath, filename), os.path.join(filepath, new_filename))
                    time.sleep(30)

                    close = WebDriverWait(browser, 30).until(expected_conditions.element_to_be_clickable(
                        (By.XPATH, "//a[contains(@onclick,'vauto.ranking.GaugePage.onCloseClick()')]")))
                    close.click()
                    print("you clicked")

                    x = WebDriverWait(browser, 50).until(expected_conditions.visibility_of_element_located(
                        (By.ID, "ext-gen3")))
                    print("Activated x")

                    cancel = WebDriverWait(browser, 50).until(expected_conditions.visibility_of_element_located(
                        (By.ID, "saveAndCloseWindow")))
                    print("Activating save changes, yay!")

                    no = WebDriverWait(browser, 50).until(expected_conditions.element_to_be_clickable(
                        (By.ID, "ext-gen1484")))
                    no.click()
                    print("yay! Your no choice is working!")


                # except
                except TimeoutException:
                    close = WebDriverWait(browser, 30).until(expected_conditions.element_to_be_clickable(
                        (By.XPATH, "//a[contains(@onclick,'vauto.ranking.GaugePage.onCloseClick()')]")))
                    close.click()
                    print("1, Wait for closing")
                    continue
                except common.exceptions.NoSuchElementException:
                    close = WebDriverWait(browser, 30).until(expected_conditions.element_to_be_clickable(
                        (By.XPATH, "//a[contains(@onclick,'vauto.ranking.GaugePage.onCloseClick()')]")))
                    close.click()
                    print("2 ,Wait for closing")
                    continue
                # close = WebDriverWait(browser, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, "//a[contains(@onclick,'vauto.ranking.GaugePage.onCloseClick()')]")))
                # close.click()
                print("Closed!")
            else:
                # close = WebDriverWait(browser, 30).until(expected_conditions.element_to_be_clickable(
                #     (By.XPATH, "//a[contains(@onclick,'vauto.ranking.GaugePage.onCloseClick()')]")))
                # close.click()
                continue

        except TimeoutException:
            print("Timed out waiting for")
            browser.quit()


parsing_loop()
