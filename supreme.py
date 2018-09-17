#!/usr/bin/python
__author__ = "Haonan Zhao"
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import webbrowser



#-------This part is load the Chrome Driver and Open the Webpage ---------------------
driver = webdriver.Chrome()
driver.get("https://www.supremenewyork.com/shop/accessories/hgnciep7l/evr2ecnmx")


twt = driver.find_elements_by_xpath("//*[contains(text(), 'Tagless')]")
print "Found Target Item"


#------------------------ Add to Cart ---------------------
addToCart = driver.find_element_by_name("commit")
addToCart.click()
print "Item has been added to cart"

#------------------------ Jump to Check out Page ---------------------
while(1):
    w = driver.find_element_by_xpath('//a[@href="https://www.supremenewyork.com/checkout"]')
    if w:
        print "Check Out Link Loaded, and Jump to Check out Page"
        w.click()
        break
    else:
        continue

#------------------------Fill in the form---------------------
print "Fill in the form"
driver.execute_script("document.getElementById('order_billing_name').value = 'Haonan Zhao';")
driver.execute_script("document.getElementById('order_email').value = 'haonanzhao92@gmail.com';")
driver.execute_script("document.getElementById('order_tel').value = '2409975223';")
driver.execute_script("document.getElementById('bo').value = '73 Bartlett st';")
driver.execute_script("document.getElementById('order_billing_zip').value = '02148';")
driver.execute_script("document.getElementById('order_billing_city').value = 'Malden';")
driver.execute_script("document.getElementById('order_billing_state').value = 'MA';")
driver.execute_script("document.getElementById('nnaerb').value = '4400998765433455';")
driver.execute_script("document.getElementById('credit_card_month').value = '08';")
driver.execute_script("document.getElementById('credit_card_year').value = '2020';")
driver.execute_script("document.getElementById('orcer').value = '987';")
driver.execute_script("document.getElementsByClassName('iCheck-helper')[1].click();")
driver.execute_script("document.getElementsByClassName('button ')[0].click();")












