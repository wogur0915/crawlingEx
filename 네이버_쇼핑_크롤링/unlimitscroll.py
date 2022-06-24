from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import csv

browser = webdriver.Chrome('C:/chromedriver.exe')


browser.get('https://www.naver.com')
browser.implicitly_wait(10)
browser.find_element_by_css_selector('a.nav.shop').click()
time.sleep(2)

search = browser.find_element_by_css_selector('input._searchInput_search_input_QXUFf')
search.click()
search.send_keys('아이폰 13')
search.send_keys(Keys.ENTER)

# 스크롤 전 높이
before_h = browser.execute_script("return window.scrollY")
# # 맨 아래로 스크롤을 내린다.
# browser.find_element_by_css_selector("body").send_keys(Keys.END)

while True :
    # 맨 아래로 스크롤을 내린다.
    browser.find_element_by_css_selector("body").send_keys(Keys.END)

    # 스크롤 사이 페이지 로딩 시간
    time.sleep(1)

    # 스크롤 후 높이
    after_h = browser.execute_script("return window.scrollY")

    if after_h == before_h :
        break
    before_h = after_h

# 파일 생성
f = open(r"C:/Users/User/pythonstudy/네이버_쇼핑_크롤링/data.csv", 'w' , encoding = 'UTF-8', newline='')
csvWriter = csv.writer(f)

# 상품정보 div
items = browser.find_elements_by_css_selector(".basicList_info_area__17Xyo")

for item in items :
    name = item.find_element_by_css_selector(".basicList_title__3P9Q7").text
    try :
        price = item.find_element_by_css_selector(".price_num__2WUXn").text
    except :
        price = "판매중단"
    link = item.find_element_by_css_selector(".basicList_title__3P9Q7 > a").get_attribute('href')

    print(name, price, link)
    csvWriter.writerow([name,price,link])

f.close()