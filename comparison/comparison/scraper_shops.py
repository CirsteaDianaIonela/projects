from selenium import webdriver
from selenium.webdriver.common.by import By  #importat ca mai tarziu sa pot cauta in functie de un parametru
from webdriver_manager.chrome import ChromeDriverManager #are rolul de a deschide browserul chrome si a realiza task-ul pe care ni-l dorim
import pandas as pd


class ScaperShops:
    def __init__(self, product_code):
        self.product_code = product_code
        self.description_emag = None
        self.description_altex = None
        # self.description_media_galaxy = None
        self.altex_price = None
        self.emag_price = None
        # self.media_galaxy_price = None
        self.image = None
        self.url_altex = None
        self.url_emag = None
        # self.url_media_galaxy = None


    def scraper_emag(self):
        browser = webdriver.Chrome(ChromeDriverManager().install()) #rolul de autoinstalare
        browser.get('https://www.emag.ro/#opensearch') #link-ul unde o sa caute
        get_element = browser.find_element(by=By.ID, value='searchboxTrigger')
        get_element.send_keys(f'{self.product_code}')  # vrem sa cautam in site dupa cuvantul telefon
        get_element.submit() #apasa enter dupa ce cautam
        description_product_emag = browser.find_element(by=By.ID, value="card_grid")
        self.description_emag = description_product_emag.text.split('\n')
        emag_price = browser.find_element(by=By.XPATH, value=f'//*[@id="card_grid"]/div/div/div/div[4]/div[1]/p[2]')
        self.emag_price = self.emag_price.text.removesuffix(' Lei')
        url_emag = browser.find_element(by=By.XPATH, value='//*[@id="card_grid"]/div/div/div/div[3]/div/a')
        self.url_emag = url_emag.get_attribute('href')
        return self.description_emag[0], self.emag_price


    def scraper_altex(self):

        browser = webdriver.Chrome(ChromeDriverManager().install())
        browser.get(f'https://altex.ro/cauta/?q={self.product_code}')
        price_product_altex = browser.find_element(by=By.XPATH, value='//*[@id="__next"]/div[2]/div[1]/main/div[2]/div/div[2]/div/ul[2]/li/a/div[5]/div/div[2]/span[1]')
        description_product_altex = browser.find_element(by=By.XPATH, value='//*[@id="__next"]/div[2]/div[1]/main/div[2]/div/div[2]/div/ul[2]/li/a')
        image = browser.find_element(by=By.XPATH, value=('//*[@id="__next"]/div[2]/div[1]/main/div[2]/div/div[2]/div/ul[2]/li/a/div[1]/img'))
        url_altex = browser.find_element(by=By.XPATH, value=('//*[@id="__next"]/div[2]/div[1]/main/div[2]/div/div[2]/div/ul[2]/li/a'))
        self.url_altex = url_altex.get_attribute('href')
        self.image = image.get_attribute('src')
        self.description_altex = description_product_altex.text.split('\n')[0]
        self.altex_price = price_product_altex.text.removesuffix(' lei')
        return self.description_altex, self.altex_price, self.image

    # def scraper_media_galaxy(self):
    #
    #     browser = webdriver.Chrome(ChromeDriverManager().install())
    #     browser.get(f'https://mediagalaxy.ro/cauta/?q={self.product_code}')
    #     price_product_media_galaxy = browser.find_element(by=By.XPATH, value='//*[@id="__next"]/div[2]/div[1]/main/div[2]/div/div[2]/div/ul[2]/li/a/div[5]/div/div[2]/span[1]')
    #     description_product_media_galaxy = browser.find_element(by=By.XPATH, value='//*[@id="__next"]/div[2]/div[1]/main/div[2]/div/div[2]/div/ul[2]/li/a')
    #     image = browser.find_element(by=By.XPATH, value=('//*[@id="__next"]/div[2]/div[1]/main/div[2]/div/div[2]/div/ul[2]/li/a/div[1]/img'))
    #     url_media_galaxy = browser.find_element(by=By.XPATH, value=('//*[@id="__next"]/div[2]/div[1]/main/div[2]/div/div[2]/div/ul[2]/li/a'))
    #     self.url_media_galaxy = url_media_galaxy.get_attribute('href')
    #     self.image = image.get_attribute('src')
    #     self.description_media_galaxy = description_product_media_galaxy.text.split('\n')[0]
    #     self.media_galaxy_price = price_product_media_galaxy.text.removesuffix(' lei')
    #     return self.description_media_galaxy, self.media_galaxy_price, self.image



