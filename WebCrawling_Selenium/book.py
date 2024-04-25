from selenium import webdriver 
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By 

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
#브라우저를 자동화한 후 >> browser window 창 유지 
chrome_options.add_experimental_option("excludeSwitches", ['enable-logging'])
#excludeSwitches : 불필요한 로깅 메시지 >> 브라우저에서 제외 

driver = webdriver.Chrome(options=chrome_options)

#주소 위치로 이동 
path = 'https://product.kyobobook.co.kr/bestseller/online?period=001&page=1&per=50'
driver.get(path)

#proi_item, prod_info, prod_author, price 

books = driver.find_elements(By.CLASS_NAME,'prod_item')


for index, book in enumerate(books):
    rank = index + 1
    title = book.find_element(By.CLASS_NAME, 'prod_info').text
    author = book.find_element(By.CLASS_NAME, 'prod_author').text
    price = book.find_element(By.CLASS_NAME, 'price').text

    print(rank, title, author, price)
driver.quit()

