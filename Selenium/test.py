from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path='../Selenium/chromedriver')

driver.get('http://mbank.pl')
title = driver.title
print(title)
time.sleep(2)
login = driver.find_element_by_xpath('//*[@id="log-in"]/a[2]')
login.click()
driver.close()
