from selenium import webdriver 
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By 

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
#브라우저를 자동화한 후 >> browser window 창 유지 
chrome_options.add_experimental_option("excludeSwitches", ['enable-logging'])
#excludeSwitches : 불필요한 로깅 메시지 >> 브라우저에서 제외 

driver = webdriver.Chrome(options=chrome_options)

driver.get(f"https://www.google.com/search?q=애플 주식")

keyword_list = ['애플','삼성전자','SK하이닉스'] 

for kw in keyword_list:
    driver.get(f"https://www.google.com/search?q={kw}+주식")

    name = driver.find_element(By.CSS_SELECTOR, ".DoxwDb").text
    price = driver.find_element(By.CSS_SELECTOR, ".IsqQVc").text
    high_price = driver.find_element(By.CSS_SELECTOR, "div[data-attrid='최고']").text
    low_price = driver.find_element(By.CSS_SELECTOR, "div[data-attrid='최저']").text


    #데이터 출력 
    print(f"{kw}주식 정보 수집 완료")
    print(f'주식명: {name}')
    print(f'현재가격: {price}')
    print(f'최고가격: {high_price}')
    print(f'최저가격: {low_price}\n')

driver.quit()




