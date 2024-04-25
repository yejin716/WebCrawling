from selenium import webdriver 
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By 

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
#브라우저를 자동화한 후 >> browser window 창 유지 
chrome_options.add_experimental_option("excludeSwitches", ['enable-logging'])
#excludeSwitches : 불필요한 로깅 메시지 >> 브라우저에서 제외 

driver = webdriver.Chrome(options=chrome_options)

#keyword = input("멀티캠퍼스라고 입력하세요:")
driver.get("https://search.naver.com/search.naver?ssc=tab.news.all&where=news&sm=tab_jum&query=멀티캠퍼스")

#멀티캠퍼스 신문사 >> info press
news_title = driver.find_elements(By.CLASS_NAME, "info.press") 
content_list = driver.find_elements(By.CLASS_NAME, "dsc_wrap")


for i, j in zip(news_title, content_list):
    news = i.text
    content = j.text
    print(f"{news} ==> {content}")

#driver.quit()
