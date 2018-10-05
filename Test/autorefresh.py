from selenium import webdriver
import time
import urllib
import urllib2

x=raw_input("www.google.com")
refreshrate=raw_input("Enter the number of seconds")
refreshrate=int(refreshrate)
driver = webdriver.Chrome()
driver.get("http://"+x)
while True:
   time.sleep(refreshrate)
   driver.refresh()
