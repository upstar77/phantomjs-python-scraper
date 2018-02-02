from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import base64
import time
from selenium.webdriver.common.by import By
from datetime import datetime
from json import dumps
from selenium.webdriver.common.keys import Keys
import os

IMAGE_PATH = os.path.abspath('./images')



capabilities = DesiredCapabilities.PHANTOMJS
capabilities["phantomjs.page.settings.userAgent"] = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_4) AppleWebKit/600.7.12 (KHTML, like Gecko) Version/8.0.7 Safari/600.7.12"
)	

driver = webdriver.PhantomJS(executable_path='./node_modules/phantomjs/bin/phantomjs',desired_capabilities=capabilities)
driver.implicitly_wait(5) # seconds
driver.set_window_size(1920,1080)

print 'trying to start browser'

print 'Trying to logging into superperfumerias'

driver.get("https://superperfumerias.com/")

driver.save_screenshot(IMAGE_PATH+'mainScreen.png')

driver.execute_script("document.querySelectorAll('.main-menu .root-item .is-children li a:not(.view-all)')[0].click()")

time.sleep(5)
# products = driver.find_elements_by_css_selector('.main-menu .root-item .is-children li a:not(.view-all)')
# if products is not None:
# 	print len(products)
# 	products[0].click()

driver.save_screenshot(IMAGE_PATH+'womens_perfumesSection.png')

time.sleep(5)

products = driver.find_elements_by_css_selector('#products .product-list-item a')

if products is not None :
	products[0].click()

driver.save_screenshot(IMAGE_PATH+'firstProduct.png')

driver.find_element_by_id('add-to-cart-button').submit()
driver.save_screenshot(IMAGE_PATH+'itemAdded.png')
time.sleep(5)

driver.get('https://superperfumerias.com/checkout/shipment')

time.sleep(5)
driver.save_screenshot(IMAGE_PATH+'checkout.png')



