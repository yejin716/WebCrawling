from selenium import webdriver 
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By 

#브라우저 옵션 설정 
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
#브라우저를 자동화한 후 >> browser window 창 유지 
chrome_options.add_experimental_option("excludeSwitches", ['enable-logging'])
#excludeSwitches : 불필요한 로깅 메시지 >> 브라우저에서 제외 

driver = webdriver.Chrome(options=chrome_options)

#예시로 google의 날씨 정보 페이지로 이동 
path = "https://www.google.com/search?q=weather"
driver.get(path)

element = driver.find_element(By.ID, 'wob_tm').text
# print(element)

#oFNiHe > omnient-visibility-control > div > div > div.eKPi4.BUSxSd > 
#span:nth-child(2) > span.BBwThe

location = driver.find_element(By.CSS_SELECTOR,'span.BBwThe').text
print("-" * 30)
print(f"현재 {location}의 온도는 {element}도 입니다.")

driver.quit()