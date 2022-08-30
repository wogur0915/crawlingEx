from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Chrome('C:/chromedriver.exe')

browser.maximize_window()
browser.get('https://www.historyexam.go.kr/')
browser.implicitly_wait(6)
browser.find_element_by_css_selector('button#goHome.btn.btn-lg.btn-primary').click()
time.sleep(1)

loginClick = browser.find_element_by_xpath('//*[@id="wrapper"]/div/div[1]/a[1]').click()
myId = browser.find_element_by_xpath('//*[@id="j_username"]')
myId.click()
myId.send_keys('wogur0915')

myPw = browser.find_element_by_xpath('//*[@id="j_password"]')
myPw.click()
myPw.send_keys('im91464226*')
time.sleep(1)
myPw.send_keys(Keys.ENTER)

time.sleep(2)
browser.find_element_by_css_selector('button#goHome.btn.btn-lg.btn-primary').click()
browser.find_element_by_xpath('/html/body/div[3]/div/div/div[4]/div[1]/a/img').click()