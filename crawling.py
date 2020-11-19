import time
from bs4 import BeautifulSoup
from selenium import webdriver

start = time.time()

driver = webdriver.Chrome(executable_path="chromedriver.exe")
url = "https://www.youtube.com/watch?v=IXUsSXvBu6o"
driver.get(url)

last_page_height = driver.execute_script("return document.documentElement.scrollHeight")

while True:
    driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
    time.sleep(5.0)
    new_page_height = driver.execute_script("return document.documentElement.scrollHeight")

    if new_page_height == last_page_height:
        break
    last_page_height = new_page_height

html_source = driver.page_source

soup = BeautifulSoup(html_source, "lxml")
comments = soup.find_all('yt-formatted-string','style-scope ytd-comment-renderer')
youtube_comments = [comments[n].string for n in range(0, len(comments))]

driver.close()
# print(youtube_comments)

f = open("youtube-comments.txt", 'w', encoding='utf-8')
for i in range(0, len(youtube_comments)):
    f.write(str(youtube_comments[i]))
f.close()

