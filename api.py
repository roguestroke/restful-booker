import requests


def test_one():
    response = requests.get("http://localhost:3001/booking")
    print(response.text)
    assert response.status_code == 200
