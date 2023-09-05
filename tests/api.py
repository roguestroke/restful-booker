import requests
from environment import ENV_OBJECT


base_url = ENV_OBJECT.get_base_url()
print(base_url)

payload = {
        "firstname": "Jim",
        "lastname": "Halper",
        "totalprice": 500,
        "depositpaid": 150,
        "bookingdates": {
            "checkin": "2023-01-01",
            "checkout": "2023-01-02"
        },
        "additionalneeds": "Breakfast"
    }


def test_should_check_existing_booking():
    booking_id = "10"
    response = requests.get(f"{base_url}/booking/{booking_id}")
    json_data = response.json()
    print(json_data)
    assert response.status_code == 200, "Wrong response code"
    assert "firstname" in json_data, "There is no field in the response"
    assert "lastname" in json_data, "There is no field in the response"
    assert "totalprice" in json_data, "There is no field in the response"
    assert "depositpaid" in json_data, "There is no field in the response"
    assert "bookingdates" in json_data, "There is no field in the response"
    assert "checkin" in json_data["bookingdates"], "There is no field in the response"
    assert "checkout" in json_data["bookingdates"], "There is no field in the response"


def test_should_create_booking():
    expected_first_name = payload["firstname"]
    expected_last_name = payload["lastname"]
    expected_total_price = payload["totalprice"]
    expected_check_in = payload["bookingdates"]["checkin"]
    expected_check_out = payload["bookingdates"]["checkout"]

    response = requests.post(f"{base_url}/booking", json=payload)
    json_data = response.json()
    print(json_data)

    assert response.status_code == 200, "Wrong response code"

    assert "bookingid" in json_data, "There is no field in the response"

    actual_first_name = json_data["booking"]["firstname"]
    assert expected_first_name == actual_first_name, f"Actual last name {actual_first_name} is not equal to expected {expected_first_name}"

    actual_lastname = json_data["booking"]["lastname"]
    assert expected_last_name == actual_lastname, f"Actual last name {actual_lastname} is not equal to expected {expected_last_name}"

    actual_totalprice = json_data["booking"]["totalprice"]
    assert expected_total_price == actual_totalprice, f"Actual total price {actual_totalprice} is not equal to expected {expected_total_price}"

    actual_depositpaid = json_data["booking"]["depositpaid"]
    assert actual_depositpaid is True, "Wrong deposit paid value in the response"

    actual_checkin = json_data["booking"]["bookingdates"]["checkin"]
    assert expected_check_in == actual_checkin, f"Actual checkin {actual_checkin} is not equal to expected {expected_check_in}"

    actual_checkout = json_data["booking"]["bookingdates"]["checkout"]
    assert expected_check_out == actual_checkout, f"Actual checkout {actual_checkout} is not equal to expected {expected_check_out}"



