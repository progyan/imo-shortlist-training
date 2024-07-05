from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import webbrowser
import os

IMO2023S1_RATING = 1200
LEVELUP_RATING = 250
YEAR_DEFLATION_RATING = 20

options = webdriver.ChromeOptions()
#options.add_argument('--headless')
browser = webdriver.Chrome(options=options)

n = int(input())

for i in range(n):
    browser.get(input())
    element = WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.CLASS_NAME, "cmty-view-post-item-text"))
    )
    html = browser.page_source
    soup = BeautifulSoup(html, "html.parser")
    probs = soup.find_all("div", {"class": "cmty-view-post-item-text"})
    year = soup.find("div", {"class": "cmty-category-cell-title"}).text.split()[0]
    topic = "ERROR"
    probid = 0
    for prob in probs:
        probhtml = str(prob).replace("//", "https://")
        if len(probhtml) < 100:
            topic = prob.text[0]
            probid = 0
            continue
        probid += 1
        dirname = year + "_" + topic + str(probid)
        if not os.path.exists("./problems/" + dirname):
            os.makedirs("./problems/" + dirname)
        with open("./problems/" + dirname + "/statement.html", "w") as f:
            f.write(probhtml)
        with open("./problems/" + dirname + "/rating.txt", "w") as f:
            f.write(str(IMO2023S1_RATING + (probid - 1) * LEVELUP_RATING - (2023 - int(year)) * YEAR_DEFLATION_RATING) + "\n")