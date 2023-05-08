import pytest
import time

from pages.home_prov_page import *
from pages.hogar_prov_page import *

@pytest.mark.ALL
@pytest.mark.FRONT
@pytest.mark.PROV

@pytest.mark.usefixtures("browser_setup")
class TestCotizadorProvincia:
    # 1- Generar una clase, con un método de test que instancie un chromedriver.

    def setup_class(self):
        logging.info("Se crea instancia webdriver")

    # 2- Ingrese a la home de ProvinciaSeguros (https://www.provinciaseguros.com.ar/).

    def test_go_home(self):
        home_prov_page = HomeProvPage(self.driver)
        home_prov_page.go_to_ps()
        logging.info("Ingreso al home de Provincia")

    # 3- Seleccionar “Seguros".

    def test_home_click_seg_pers(self):
        home_prov_page = HomeProvPage(self.driver)
        home_prov_page.click_seg_pers_home()
        logging.info("Visualizo tipos de seguros")

    # 4- Seleccionar “HOGAR”

    def test_home_click_btn_hogar(self):
        time.sleep(5)
        home_prov_page = HomeProvPage(self.driver)
        home_prov_page.clic_hogar_home()
        time.sleep(5)
        logging.info("Visualizo tipos de seguros")
        assert home_prov_page.is_title_text_home("Hogar – Provincia Seguros")

    # 5-Hacer click en “Cotizar”

    def test_hogar_click_btn_cotiza_aca(self):
        hogar_page = HogarProvPage(self.driver)
        hogar_page.click_btn_cotiza_aca_hogar()
        logging.info("Ingreso HOGAR")
        time.sleep(5)

    # 6- Completar campos y hacer click en Cotizar

    def test_hogar_input_provincia_nombreapellido_email_codarea_telefono(self):
        logging.info("Input detalles hogar a cotizar")
        driver = self.driver.switch_to.window(self.driver.window_handles[1])
        time.sleep(5)
        hogar_page = HogarProvPage(self.driver)
        hogar_page.input_text_provincia_hogar(provincia="Cordoba")
        hogar_page.input_text_nombre_apellido_hogar(nombre="Test Lucas")
        hogar_page.input_text_email_hogar(email="Testlucas@yopmail.com")
        hogar_page.input_text_cod_area_hogar(codarea="3541")
        hogar_page.input_text_telefono_hogar(tel="365478")
        hogar_page.click_btn_cotizar_hogar()

    def test_guardar_cotizaciones(self):
        time.sleep(10)
        logging.info("Comienza recoleccion de datos")
        hogar_page = HogarProvPage(self.driver)
        hogar_page.save_table_cotizaciones()
        time.sleep(10)

    def test_validar_costo_mensual_total_sea_entero(self):
        hogar_page = HogarProvPage(self.driver)
        assert (type(hogar_page.valor_plan_total()) == int)
        assert (hogar_page.valor_plan_total() > 0)

    def test_validar_costo_mensual_oro_sea_entero(self):
        hogar_page = HogarProvPage(self.driver)
        assert (type(hogar_page.valor_plan_oro()) == int)
        assert (hogar_page.valor_plan_oro() > 0)

    def test_validar_costo_mensual_premium_sea_entero(self):
        hogar_page = HogarProvPage(self.driver)
        assert (type(hogar_page.valor_plan_premium()) == int)
        assert (hogar_page.valor_plan_premium() > 0)

    def test_validar_title_and_chat(self):
        hogar_page = HogarProvPage(self.driver)
        assert hogar_page.is_element_chat_displayed()
        assert hogar_page.is_title_text("Cotizador Integral")

    def teardown_class(self):
        self.driver.quit()


"""    # 6- Guarde la grilla de resultados como lista de WebElement y aserte que:
    # - Cada uno de los elementos contenga “Seguro de hogar - Mercantil andina" en su title.
    # -Validar que el costo mensual sea un valor positivo, mayor a cero y entero
    # - Validar que se visualice "Chat Online"
    # El test debe heredar de una clase base (TestBase) donde deben estar los annotation @BeforeTest y @AfterTest.
    # Es deseable utilizar el patrón "Page Object" para el modelado de las páginas."""
