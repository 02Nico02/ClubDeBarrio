from http import client
from web import create_app

app = create_app()
app.testing = True
client = app.test_client()

def test_api_sport_by_id():
    response = client.get("/api/sport/1")
    assert response.status_code == 200
    json_sport_info = response.get_json()
    assert json_sport_info["division"] == "Sub 20"
    assert json_sport_info["instructors"] == "Carlos Gomez"
    assert json_sport_info["monthly_fee"] == "2000"
    assert json_sport_info["name"] == "Futbol"
    assert json_sport_info["schedule"] == "Lunes 15 a 16, Miercoles 14 a 15"
       
def test_api_sport_without_id():
    response = client.get("/api/sport/")
    assert response.status_code == 404
       
def test_api_defaulters():
    response = client.get("/api/club/data/defaulters")
    assert response.status_code == 200
    json_defaulters_info = response.get_json()
    assert json_defaulters_info["defaulters"] == 2
    assert json_defaulters_info["non_defaulters"] == 14

def test_api_associated_by_id():
    response = client.get("/api/club/associated/1")
    assert response.status_code == 200
    json_associated_info = response.get_json()
    assert json_associated_info["defeated_quotas"] == 0
    assert json_associated_info["name"] == "Luis Emanuel"
    sport_list = json_associated_info["sports"]
    assert len(sport_list) == 2
    assert sport_list[0] == "Futbol"
    assert sport_list[1] == "Volley"

def test_api_associated_without_id():
    response = client.get("/api/club/associated/")
    assert response.status_code == 404