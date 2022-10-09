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


chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

class FindInfo():
    def __init__(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=chrome_options)
        self.price_list = []
        self.address_list = []
        self.link_list =[]
        self.des_list=[]

    def house_scraping(self,current_page):
        self.driver.get(f"https://www.redfin.com/city/11203/CA/Los-Angeles/apartments-for-rent/filter/max-price=2k,min-beds=1,max-beds=1,min-baths=1/page-{current_page}")
        time.sleep(5)

        site = self.driver.page_source
        soup = BeautifulSoup(site, "html.parser")

        prices = soup.select(".homecardV2Price")
        self.price_list = [price.getText() for price in prices]

        addresses = soup.select(".homeAddressV2")
        self.address_list = [address.getText().split("|")[-1].strip() for address in addresses]

        links = soup.select(".bottomV2 a")
        self.link_list = ["https://www.redfin.com" + link.get("href") for link in links]

        descriptions = soup.select(".HomeStatsV2 div")
        list =[des.getText() for des in descriptions]
        list1 = [list[n:n+3] for n in range(0,len(list),3)]
        self.des_list=[]
        for item in list1:
            item = " ".join(str(stat) for stat in item)
            self.des_list.append(item)


    def click_next_page(self):
        time.sleep(10)
        self.driver.find_element(By.XPATH,'/html/body/div[1]/div[8]/div[2]/div[2]/div[4]/div/div/div[3]/button[2]').click()





