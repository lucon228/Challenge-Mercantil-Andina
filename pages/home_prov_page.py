import logging

from selenium.webdriver.common.by import By
from pages.base_page import BasePage
#from utils.selenium_helper import SeleniunHelper


class HomeProvPage(BasePage):

    # WEB ELEMENTS HOME PAGE

    #home_title = "Seguros Online | Mercantil Andina. Incondicional. Siempre."
    btn_seguros_personas = (By.XPATH, "//*[@id='menu-item-909']/a")
    btn_hogar = (By.XPATH, "//body/div[1]/div[1]/div[1]/div[5]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/a[1]/div[1]/div[2]")
    UrlProvincia = "https://www.provinciaseguros.com.ar/"

    def __init__(self, driver):
         self.driver = driver

    def go_to_ps(self):
        self.driver.get(self.UrlProvincia)

    def click_seg_pers_home(self):
        self.element_click(self.btn_seguros_personas)
        #self.element_click(self.btn_hogar)

    def clic_hogar_home(self):
        self.element_click(self.btn_hogar)

    def is_title_text_home(self, text):
        return self.get_title(text)

