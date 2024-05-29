from selenium import webdriver 
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By 
import time

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_experimental_option("excludeSwitches", ['enable-logging'])

driver = webdriver.Chrome(options=chrome_options)

import numpy as np 
import pandas as pd

url= 'https://www.melon.com/chart/index.htm'
driver.get(url)

#html 다운로드 및 bs4 로 읽기 
# from bs4 import BeautifulSoup

# html = driver.page_source
# soup = BeautifulSoup(html, 'html.parser')
# print(soup)

#100개의 노래 tag찾기 
 
# NGD기법 방법 1 
# songs = soup.select('tbody > tr')
# print(len(songs))
# print(type(songs))
# print(songs[0])

# print(soup.select('tr')[1:])


# songs = soup.select('tr')[1:]
# # print(len(songs))
# # print(songs[0])

# # print(songs[0])
# song = songs[0]
# # print(song.select('a'))

# title = song.select('a')
# # print(len(title))
# # print(title[1])

# # print(title[0].text)
# # print(title[2].text) # supernova

# #곡 제목 찾는 방법 2
# # print(song.select('span > a'))

# title = song.select('span > a')
# # print(len(title))
# # print(title[0]) # supernova
# # print(title[0].text) #supernova

# #곡 제목 찾는 방법 3

# # div : class="ellipsis rank01" 

# title = song.select('div.ellipsis.rank01 > span > a')
# # print(title[0].text) #supernova

# #가수정보 
# singer = song.select('div.ellipsis.rank02 > a')

#곡 정보 100개 다 가져오기
# for i, song in enumerate(songs, 1):
#     title = song.select('div.ellipsis.rank01 > span > a')[0].text
#     singer = song.select('div.ellipsis.rank02 > a')[0].text
#     print(f"{i}위: {title}, {singer}")
#     print('*' * 60)
 
#------------------------------------------------------------------------------------   
#정리본 
# from bs4 import BeautifulSoup

# html = driver.page_source
# soup = BeautifulSoup(html, 'html.parser')  

# songs = soup.select('tr')[1:]

# for i, song in enumerate(songs, 1):
#     title = song.select('div.ellipsis.rank01 > span > a')[0].text
#     singer = song.select('div.ellipsis.rank02 > a')[0].text
#     print(f"{i}위: {title}, {singer}")
#     print('*' * 60)
   
#------------------------------------------------------------------------------------   
   
#업그레이드 버전 크롤러 
from bs4 import BeautifulSoup

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

song_data = []
rank = 1 #초기화 

songs = soup.select('tr')[1:]

for song in songs:
    title = song.select('div.ellipsis.rank01 > span > a')[0].text
    singer = song.select('div.ellipsis.rank02 > a')[0].text
    mylist = ['melon', rank, title, singer]
    song_data.append(mylist)
    rank += 1
print(song_data)  

df = pd.DataFrame(song_data, columns=['서비스업체','순위','곡','제목'])  
# print(df)

df.to_excel('./melon_rank_20240523.xlsx', index=False)
time.sleep(8)

