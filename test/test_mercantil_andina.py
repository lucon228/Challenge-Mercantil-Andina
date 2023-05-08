import pytest
import time

from pages.home_page import *
from pages.auto_page import *

@pytest.mark.ALL
@pytest.mark.FRONT
@pytest.mark.MA
@pytest.mark.usefixtures("browser_setup")
class TestMercantilAndina:
    # 1- Generar una clase, con un método de test que instancie un chromedriver.

    def setup_class(self):
        logging.info("Se crea instancia webdriver")


    # 2- Ingrese a la home de Mercantil (https://www.mercantilandina.com.ar/).

    def test_go_home(self):
        home_page = HomePage(self.driver)
        home_page.go_to_ma()
        logging.warning("Ingreso al home de MA")

    # 3- Seleccionar “Seguros".
    # 4- Seleccionar “Auto”

    def test_home_click_seg_pers_auto(self):
        home_page = HomePage(self.driver)
        home_page.click_seg_pers_auto()
        logging.warning("Ingreso Autos")

    # 5-Hacer click en “Cotizar”

    def test_auto_click_btn_cotizar(self):
        auto_page = AutoPage(self.driver)
        auto_page.click_btn_cotizar_auto()
        logging.warning("Ingreso Autos")

    # 6- Completar campos y hacer click en Cotizar

    def test_auto_input_marca_anio_modelo_version(self):
        auto_page = AutoPage(self.driver)
        auto_page.input_text_marca_auto(marca="FORD")
        auto_page.input_text_anio_auto(anio="2016")
        auto_page.input_text_modelo_auto(modelo="RANGER")
        auto_page.input_text_version_auto(version="XLT")
        logging.warning("Input detalles vehiculo a cotizar")

    def test_auto_click_btn_siguiente(self):
        auto_page = AutoPage(self.driver)
        auto_page.click_btn_siguiente_auto()
        logging.warning("Redirecciona a completar datos de contacto")
        time.sleep(5)

    def teardown_class(self):
        self.driver.quit()




