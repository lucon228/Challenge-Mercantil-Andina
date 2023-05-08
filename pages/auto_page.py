import logging

from selenium.webdriver.common.by import By
from pages.base_page import BasePage
#from utils.selenium_helper import SeleniunHelper


class AutoPage(BasePage):

    # WEB ELEMENTS AUTO PAGE

    elemento_title_autos = (By.XPATH, "//*[@id='post-32560']/div/div/section[1]/div[2]/div/div/div[1]/div/h1")
    title_auto = "Seguro para autos"
    btn_cotizar_auto = (By.XPATH, "//*[@id='post-32560']/div/div/section[1]/div[2]/div/div/div[3]/div/div/a/span/span")
    btn_siguiente_auto = (By.XPATH, "//*[@id='post-125']/div/div/section[3]/div/div/div/div/div/form/div[2]/div[1]/div[7]/div/button")
    input_marca = (By.XPATH, "//*[@id='form-field-marca']")
    input_anio = (By.XPATH, "//*[@id='form-field-ano']")
    input_modelo = (By.XPATH, "//*[@id='form-field-modelo']")
    input_version = (By.XPATH, "//*[@id='form-field-version']")

    def __init__(self, driver):
         super().__init__(driver)
         logging.info("PRUEBAS HOME - INICIO")

    def click_btn_cotizar_auto(self):
        self.element_click(self.btn_cotizar_auto)
        logging.info("PRUEBAS HOME - FIN")

    def click_btn_siguiente_auto(self):
        self.element_click(self.btn_siguiente_auto)

    def input_text_marca_auto(self, marca):
        self.element_enter_text(self.input_marca, marca)

    def input_text_anio_auto(self, anio):
        self.element_enter_text(self.input_anio, anio)

    def input_text_modelo_auto(self, modelo):
        self.element_enter_text(self.input_modelo, modelo)

    def input_text_version_auto(self, version):
        self.element_enter_text(self.input_version, version)

        logging.info("PRUEBAS HOME - FIN")

