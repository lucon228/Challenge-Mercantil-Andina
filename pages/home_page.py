import logging

from selenium.webdriver.common.by import By
from pages.base_page import BasePage
#from utils.selenium_helper import SeleniunHelper


class HomePage(BasePage):

    # WEB ELEMENTS HOME PAGE

    home_title = "Seguros Online | Mercantil Andina. Incondicional. Siempre."
    btn_seguros_personales = (By.XPATH, "//*[@id='menu-item-32651']/a")
    btn_auto = (By.XPATH, "//*[@id='menu-item-32655']/a")
    UrlMA = "https://www.mercantilandina.com.ar/"

    def __init__(self, driver):
         self.driver = driver
         logging.info("PRUEBAS HOME - INICIO")

    def go_to_ma(self):
        self.driver.get(self.UrlMA)

    def click_seg_pers_auto(self):
        self.element_click(self.btn_seguros_personales)
        self.element_click(self.btn_auto)
        logging.info("PRUEBAS HOME - FIN")

