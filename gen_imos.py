from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

site = "https://artofproblemsolving.com"
url = "/community/c3223_imo_shortlist"
options = webdriver.ChromeOptions()
#options.add_argument('--headless')
browser = webdriver.Chrome(options=options)
browser.get(site + url)
element = WebDriverWait(browser, 5).until(
    EC.presence_of_element_located((By.CLASS_NAME, "cmty-full-cell-link"))
)

SCROLL_PAUSE_TIME = 2
LAST_IMOS_COUNT = 17

last_height = browser.execute_script("return document.body.scrollHeight")
while True:
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(SCROLL_PAUSE_TIME)
    new_height = browser.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

html = browser.page_source
soup = BeautifulSoup(html, 'html.parser')

imos = soup.find_all("a", {"class": "cmty-full-cell-link"})
hrefs = set()
for i in range(LAST_IMOS_COUNT * 2):
    if imos[i]["href"] != url:
        hrefs.add(site + imos[i]["href"])

print(len(hrefs))
for href in hrefs:
    print(href)