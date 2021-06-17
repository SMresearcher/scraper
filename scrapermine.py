from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv
START_URL = "https://asianvivekanand.com/events/"
browser = webdriver.Chrome("C:/Users/saba2/Desktop/whitehat/datasc/C127/drv/chromedriver")
browser.get(START_URL)
time.sleep(10)
def scrape():
    headers = ["Events"]
    event_data = []
    soup = BeautifulSoup(browser.page_source, "html.parser")
    for news_tag in soup.find_all("div", attrs={"class", "news-home"}):
        temp=[]
        temp.append(news_tag.find_all("a")[0].contents[0])
        event_data.append(temp)
        
    with open("scrappermine.csv", "w") as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(headers)
        csvwriter.writerows(event_data)
scrape()