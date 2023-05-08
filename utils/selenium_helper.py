import logging
import os
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SeleniunHelper:
    def __init__(self, driver):
        self.driver = driver

    def element_enter_text(self, locator, text):
        WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(locator)).send_keys(text)

    def element_click(self, locator):
        WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(locator)).click()

    def find_element(self, locator):
        elemento = WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(locator))
        return elemento

    def get_title(self, text):
        try:
            WebDriverWait(self.driver, 15).until(EC.title_is(text))
            return True
        except:
            return False

    def validate_number_is_int(self, number):
        if type(number) == int:
            print(f"ENTERO ---> {number}")
            return True
        else:
            print(f"OTRO ---> {number}")
            return False

