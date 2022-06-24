from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome('C:/chromedriver.exe')


browser.get('https://www.naver.com')
browser.implicitly_wait(10)
browser.find_element_by_css_selector('a.nav.shop').click()
browser.implicitly_wait(2)

search = browser.find_element_by_css_selector('input._searchInput_search_input_QXUFf')
search.click()
search.send_keys('아이폰 13')
search.send_keys(Keys.ENTER)
