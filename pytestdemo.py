import requests
import aligner as al

# Pytest demo.

def test_perfectalign_ok():
     seq1: str = "ACAT"
     seq2: str = "ACAT"
     result: bool = al.perfect_align(seq1,seq2)
     assert result == True

def test_not_perfectalign1_ok():
     seq1: str = "ACA"
     seq2: str = "ACAG"
     result: bool = al.perfect_align(seq1,seq2)
     assert result == False

# Requests library demo.
# https://www.ontestautomation.com/writing-tests-for-restful-apis-in-python-using-requests-part-1-basic-tests/

def test_get_locations_for_us_90210_check_status_code_equals_200():
     expected_result: int = 200
     response: str = requests.get("http://api.zippopotam.us/us/90210")
     assert response.status_code == 200

def test_get_locations_for_us_90210_check_country_equals_united_states():
     expected_result: int = "United States"
     response = requests.get("http://api.zippopotam.us/us/90210")
     response_body: str = response.json()
     assert response_body["country"] == expected_result

def test_get_pokeapi_pikachu_id():
     expected_result: int = 25
     response = requests.get("https://pokeapi.co/api/v2/pokemon/pikachu")
     response_body: str = response.json()
     pikachu_id: int = response_body["id"]
     print(pikachu_id)
     assert pikachu_id == expected_result

# Requests library demo; own API created with Flask.
def test_api_app5_works():
     expected_result: str = 'Hello World!'
     response = requests.get("http://127.0.0.1:5000/")
     assert response.status_code == 200

def test_api_db():
     expected_result: str = 'Hello World!'
     response = requests.get("http://127.0.0.1:5000/")
     assert response.status_code == 200

def test_api_db_pablo():
     expected_character: str = 'Pablo'

     response = requests.get("http://127.0.0.1:5000/db2/0")
     response_body: str = response.json()
     character: str = response_body["character"]
     print(expected_character)
     print(len(expected_character))
     print(character)
     print(len(character))
     assert character == expected_character