import pytest
from assertpy import assert_that
import logging
from api.api_cervecerias import ApiCerveceria
from pprint import pprint

@pytest.mark.ALL
@pytest.mark.API
class TestApi:

    def setup_class(self):
        logging.info("Llamando al constructor de la API Cervecerias")
        self.api = ApiCerveceria()

    def test_get_cervecerias_by_path(self):
        response = self.api.get_cervecerias_by_path(path="autocomplete?query=lagunitas")
        assert_that(response.status_code).is_equal_to(200)

    def test_get_id_with_name(self):
        self.api.get_id_cervecerias_with_name(name="Lagunitas Brewing Co", state=None)

    def test_get_id_with_state(self):
        response = self.api.get_id_cervecerias_with_name(name="Lagunitas Brewing Co", state="California")
        assert_that(response.json()["id"]).is_equal_to("761")
        assert_that(response.json()["name"]).is_equal_to("Lagunitas Brewing Co")
        assert_that(response.json()["street"]).is_equal_to("1280 N McDowell Blvd")
        assert_that(response.json()["phone"]).is_equal_to(7077694495)