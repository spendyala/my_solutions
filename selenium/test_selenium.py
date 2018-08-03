import selenium.webdriver.support.ui as UI

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.proxy import *
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException

import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")
chrome_options.add_argument("user-data-dir=/Users/vpendyala/Library/Application\ Support/Google/Chrome/Profile\ 3")

driver = webdriver.Chrome(
    '/usr/local/bin/chromedriver',
    chrome_options=chrome_options)
driver.get('https://google.com')

time.sleep(10)
all_button = driver.find_elements_by_xpath('//a')
# import ipdb; ipdb.set_trace()
sign_in_button = None
for each_a in all_button:
    if each_a.text.lower() == 'sign in':
        print(each_a.text)
        sign_in_button = each_a
        break
if not sign_in_button:
    print('Clicked')
    sign_in_button.click()
time.sleep(10)
all_button = driver.find_elements_by_xpath('//a')
for each_a in all_button:
    print(each_a.text)
