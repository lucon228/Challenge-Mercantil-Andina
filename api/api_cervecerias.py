import json
import logging
import requests
from pprint import pprint


class ApiCerveceria:
    def __init__(self):
        logging.info("Construyendo api")
        self.api_url_breweries = "https://api.openbrewerydb.org/breweries/"

        """    
        def get_cervecerias(self):
        path = "autocomplete?query=lagunitas"
        headers = {}
        logging.info(f"Request GET a la API:{self.api_url_breweries+path}")
        payload = {}
        response = requests.get(url=self.api_url_breweries+path, headers=headers, data=payload)
        logging.info("Fin del Request CERVECERIAS")
        data = response.json()
        pprint(data)
        return response
        """

    def get_cervecerias_by_path(self, path):
        headers = {}
        logging.info(f"Request GET a la API BY PATH:{self.api_url_breweries+path}")
        payload = {}
        response = requests.get(url=self.api_url_breweries+path, headers=headers, data=payload)
        data = response.json()
        pprint(data)
        logging.info("Fin del Request CERVECERIAS BY PATH")
        return response

    def get_id_cervecerias_with_name(self, name, state):
        response_name = self.get_cervecerias_by_path(path="autocomplete?query=lagunitas")

        data = response_name.json()
        response_info_cerveceria = []
        for v in range(len(data)):
            print("EMPIEZA EL FOR")
            if data[v]["name"] == name:
                print(f'V {v}')
                print(f'El NAME es {data[v]["name"]}')
                print(f'El ID es {data[v]["id"]}')
                response_info_cerveceria = requests.get(url=self.api_url_breweries + data[v]["id"])
                data_info_cerveceria = response_info_cerveceria.json()
                logging.info("Fin del Request INFO CERVECERIA BY NAME")
                if state is not None:
                        if data_info_cerveceria['state'] == state:
                            print(f'El STATE es {data_info_cerveceria["state"]}')
                            print(f'El ID es {data_info_cerveceria["id"]}')
                            response_by_state = requests.get(url=self.api_url_breweries + data_info_cerveceria["id"])
                            data_state = response_by_state.json()
                            pprint(data_state)
                            logging.info("Fin del Request INFO CERVECERIA BY STATE")
                            #return response_by_state

                            return response_by_state






    def get_cerveceria_with_state(self, state):
        response_state = self.get_id_cervecerias_with_name(name="Lagunitas Brewing Co")
        print("print response_state")
        pprint(response_state.json())
        print("print response_state")
        data = response_state.json()
        data_json = json.load(data)
        dataDumps = json.dumps(json.loads(data_json))
        pprint(data)
        pprint(dataDumps)
        print(len(data))
        print(range(len(data)))
        for v in range(len(data)):
            print("EMPIEZA EL FOR 2")
            if data[v]["state"] == state:
                print(f'V {v}')
                print(f'El STATE es {data[v]["state"]}')
                print(f'El ID es {data[v]["id"]}')
                response_by_state = requests.get(url=self.api_url_breweries + data[v]["state"])
                data_state = response_by_state.json()
                pprint(data_state)
                logging.info("Fin del Request INFO CERVECERIA BY ID")
                return response_by_state
