from selenium import webdriver
import time
a=input("enter email:")
b=input("enter password:")
browser=webdriver.Chrome()
browser.get("http://www.facebook.com")

username = browser.find_element_by_id("email")
password = browser.find_element_by_id("pass")
submit   = browser.find_element_by_id("loginbutton")

username.send_keys(a)
password.send_keys(b)

submit.click()
time.sleep(4)
page_title = browser.title
assert page_title == "Facebook"