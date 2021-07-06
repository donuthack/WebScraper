# from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
# import time
# from selenium.webdriver.common.keys import Keys
#
# driver = webdriver.Chrome('/Users/workplace/Downloads/chromedriver')
# driver.get('https://www.lambdatest.com/')
# time.sleep(5)
# # locates a link element on the loaded url using xpath
# new_tab_link = driver.find_element_by_xpath('//a[contains(@class,"nav-link") and contains(@href,"selenium-automation")]')
# time.sleep(5)
# # instantiates ActionChains class of selenium webDriver
# action = ActionChains(driver)
# # clicks on located kink element with CONTROL button in pressed state using actionChains class. This opens the link in new tab
# action.key_down(Keys.CONTROL).click(new_tab_link).key_up(Keys.CONTROL).perform()
# time.sleep(3)
# driver.quit()

# from selenium import webdriver
# import time
#
# driver = webdriver.Chrome('/Users/workplace/Downloads/chromedriver')
# driver.get('https://www.google.com')
# time.sleep(15)
#
# driver.execute_script("window.open('');")
# time.sleep(15)
#
# driver.switch_to.window(driver.window_handles[1])
# driver.get("https://facebook.com")
# time.sleep(15)
#
# driver.close()
# time.sleep(15)
#
# driver.switch_to.window(driver.window_handles[0])
# driver.get("https://www.yahoo.com")
# time.sleep(15)

from selenium import webdriver
import time

driver = webdriver.Chrome('/Users/workplace/Downloads/chromedriver')
driver.get('https://www.google.com/')

# Open a new window
driver.execute_script("window.open('');")
# Switch to the new window
driver.switch_to.window(driver.window_handles[1])
driver.get("http://stackoverflow.com")
time.sleep(3)

# Open a new window
driver.execute_script("window.open('');")
# Switch to the new window
driver.switch_to.window(driver.window_handles[2])
driver.get("https://www.reddit.com/")
time.sleep(3)
# close the active tab
driver.close()
time.sleep(3)

# Switch back to the first tab
driver.switch_to.window(driver.window_handles[0])
driver.get("https://bing.com")
time.sleep(3)

# Close the only tab, will also close the browser.
driver.close()
