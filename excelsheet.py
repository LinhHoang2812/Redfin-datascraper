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

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

form_link ="https://docs.google.com/forms/d/e/1FAIpQLSfop5hF-3TEfOdp7qhRAHP8LwW0XZtOe49m7eZijt61A-PtFw/viewform?usp=sf_link"


class ExcelSheet():
    def __init__(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    def fill_form(self,address_list,price_list,link_list,des_list):
        self.driver.get(form_link)
        for n in range(0, len(address_list)):
            address = self.driver.find_element(By.XPATH,'/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
            address.send_keys(f"{address_list[n]}")

            price = self.driver.find_element(By.XPATH,'/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
            price.send_keys(f'{price_list[n]}')

            link = self.driver.find_element(By.XPATH,'/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
            link.send_keys(f"{link_list[n]}")

            desc = self.driver.find_element(By.XPATH,'/html/body/div/div[2]/form/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[1]/input')
            desc.send_keys(f"{des_list[n]}")

            send = self.driver.find_element(By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div')
            send.click()

            fill_again = self.driver.find_element(By.LINK_TEXT, "Invia un'altra risposta")
            fill_again.click()

            time.sleep(3)


