from bs4 import BeautifulSoup
import requests
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import json
from findinfo import FindInfo
from excelsheet import ExcelSheet


chrome_options = Options()
chrome_options.add_experimental_option("detach", True)



headers = {
    "Accept-Language": "en-gb",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.2 Safari/605.1.15"

}

response = requests.get(url="https://www.redfin.com/city/11203/CA/Los-Angeles/apartments-for-rent/filter/max-price=2k,min-beds=1,max-beds=1,min-baths=1",headers=headers)
site = response.text

soup = BeautifulSoup(site,"html.parser")

current_page = 1

pages = soup.select(".goToPage")
page_list = [int(page.getText()) for page in pages]
page_max = max(page_list)


bot= FindInfo()
sheet = ExcelSheet()
while current_page <= page_max:
    bot.house_scraping(current_page)
    sheet.fill_form(bot.address_list,bot.price_list,bot.link_list,bot.des_list)
    current_page +=1
    time.sleep(5)
print("Finish")









