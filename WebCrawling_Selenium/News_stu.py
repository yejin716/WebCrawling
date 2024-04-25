from selenium import webdriver 
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By 

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
#브라우저를 자동화한 후 >> browser window 창 유지 
chrome_options.add_experimental_option("excludeSwitches", ['enable-logging'])
#excludeSwitches : 불필요한 로깅 메시지 >> 브라우저에서 제외 

driver = webdriver.Chrome(options=chrome_options)

#네이버 뉴스 >> "푸바오"검색 
#https://search.naver.com/search.naver?
#ssc=tab.news.all&where=news&sm=tab_jum&query=%ED%91%B8%EB%B0%94%EC%98%A4

keyword = input("키워드 입력해 주세요: ")
driver.get(f"https://search.naver.com/search.naver?ssc=tab.news.all&where=news&sm=tab_jum&query={keyword}")

#뉴스 타이틀 >> news_tit
title_list = driver.find_elements(By.CLASS_NAME, "news_tit")
for title in title_list:
    title = title.text
    print(title)
driver.quit()