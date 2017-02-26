import time
from selenium import webdriver
#executable_path="/opt/google/chrome/google-chrome"
browser = webdriver.Chrome()
browser.get('http://10.10.54.4:8090/')
emailElem = browser.find_element_by_xpath('//*[@id="usernametxt"]/td/input')
emailElem.send_keys()#enter user name
passwordElem = browser.find_element_by_xpath('/html/body/form/div[1]/div[2]/div[2]/table/tbody/tr[4]/td/input')
passwordElem.send_keys()#enter password
passwordElem.submit()