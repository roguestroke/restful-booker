import requests


base_url = "http://localhost:3001"


def test_should_check_existing_booking():
    booking_id = "10"
    response = requests.get(f"{base_url}/booking/{booking_id}")
    data = response.json()
    print(data)
    assert response.status_code == 200, "Wrong response code"
    assert 'firstname' in data

