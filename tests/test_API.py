from fastapi.testclient import TestClient

from ..app import app

client = TestClient(app)


def test_convert_celsius_to_fahrenheit():
    """
    Test converting Celsius to Fahrenheit.

    Send a POST request to the "/convert/" endpoint with Celsius temperature.
    Assert that the response status code is 200 and the converted temperature is correct.
    """
    response = client.post("/convert/", json={"units": "c", "value": 0})
    assert response.status_code == 200
    assert response.json() == {"units": "fahrenheit", "value": 32}


def test_convert_fahrenheit_to_celsius():
    """
    Test converting Fahrenheit to Celsius.

    Send a POST request to the "/convert/" endpoint with Fahrenheit temperature.
    Assert that the response status code is 200 and the converted temperature is correct.
    """
    response = client.post("/convert/", json={"units": "f", "value": 32})
    assert response.status_code == 200
    assert response.json() == {"units": "celsius", "value": 0}


def test_invalid_units():
    """
    Test supplying invalid units.

    Send a POST request to the "/convert/" endpoint with invalid units.
    Assert that the response status code is 422 and the error message is correct.
    """
    response = client.post("/convert/", json={"units": "invalid", "value": 0})
    assert response.status_code == 422
    assert response.json()["detail"][0]["msg"] == "Input should be 'c' or 'f'"
