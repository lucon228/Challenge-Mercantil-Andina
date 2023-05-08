import logging
import nums_from_string

from selenium.webdriver.common.by import By
from pages.base_page import BasePage
#from utils.selenium_helper import SeleniunHelper


class HogarProvPage(BasePage):

    # WEB ELEMENTS HOGAR PAGE

    UrlCotizador = "https://cotizadorhogar.provinciaseguros.com.ar/"
    btn_cotiza_aca = (By.XPATH, "//a[contains(text(),'COTIZÁ ACÁ')]")
    btn_cotizar = (By.XPATH, "//button[contains(text(),'Cotizar')]")
    btn_contactame = (By.XPATH, "//button[contains(text(),'Contactame')]")
    input_provincia = (By.XPATH, "//select[@id='provincia']")
    input_nombre_apellido = (By.XPATH, "//input[@id='apellido']")
    input_email = (By.XPATH, "//input[@id='email']")
    input_cod_area = (By.XPATH, "//input[@id='codArea']")
    input_telefono = (By.XPATH, "//input[@id='telefono']")
    table_cotizaciones = (By.XPATH, "//body/div[@id='app']/main[@id='202112061137']/div[1]/div[1]/div[2]/div[2]/div[1]")
    monto_total = (By.XPATH, "//body/div[@id='app']/main[@id='202112061137']/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/h6[1]")
    monto_oro = (By.XPATH, "//body/div[@id='app']/main[@id='202112061137']/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/h6[1]")
    monto_premium = (By.XPATH, "//body/div[@id='app']/main[@id='202112061137']/div[1]/div[1]/div[2]/div[2]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/h6[1]")

    def __init__(self, driver):
         super().__init__(driver)

    def go_to_cotizador(self):
        self.driver.get(self.UrlCotizador)

    def click_btn_cotiza_aca_hogar(self):
        self.element_click(self.btn_cotiza_aca)

    def click_btn_cotizar_hogar(self):
        self.element_click(self.btn_cotizar)

    def input_text_provincia_hogar(self, provincia):
        self.element_enter_text(self.input_provincia, provincia)

    def input_text_nombre_apellido_hogar(self, nombre):
        self.element_enter_text(self.input_nombre_apellido, nombre)

    def input_text_email_hogar(self, email):
        self.element_enter_text(self.input_email, email)

    def input_text_cod_area_hogar(self, codarea):
        self.element_enter_text(self.input_cod_area, codarea)

    def input_text_telefono_hogar(self, tel):
        self.element_enter_text(self.input_telefono, tel)

    def save_table_cotizaciones(self):
        tabla_text = self.find_element(self.table_cotizaciones)
        print(f"Valores de la grilla {tabla_text.text}")

    def valor_plan_total(self):
        monto_total_text = self.find_element(self.monto_total)
        monto_total_text_1 = monto_total_text.get_attribute("textContent")[3:8]
        monto_total_text_2 = monto_total_text_1.replace(".", "")
        monto_total_text_3 = int(monto_total_text_2)
        print(f"Valor plan total solo: {monto_total_text_3}")
        return monto_total_text_3

    def valor_plan_oro(self):
        monto_oro_text = self.find_element(self.monto_oro)
        monto_oro_text_1 = monto_oro_text.get_attribute("textContent")[3:8]
        monto_oro_text_2 = monto_oro_text_1.replace(".", "")
        monto_oro_text_3 = int(monto_oro_text_2)
        print(f"Valor plan total solo: {monto_oro_text_3}")
        return monto_oro_text_3

    def valor_plan_premium(self):
        monto_premium_text = self.find_element(self.monto_premium)
        monto_premium_text_1 = monto_premium_text.get_attribute("textContent")[3:8]
        monto_premium_text_2 = monto_premium_text_1.replace(".", "")
        monto_premium_text_3 = int(monto_premium_text_2)
        print(f"Valor plan total solo: {monto_premium_text_3}")
        return monto_premium_text_3

    def is_valor_plan_total_entero(self):
        self.validate_number_is_int(self.valor_plan_total())

    def is_valor_plan_oro_entero(self):
        self.validate_number_is_int(self.valor_plan_oro())

    def is_valor_plan_premium_entero(self):
        self.validate_number_is_int(self.valor_plan_premium())

    def is_element_chat_displayed(self):
        try:
            self.find_element(self.btn_contactame)
            return True
        except:
            return False

    def is_title_text(self, text):
        return self.get_title(text)
