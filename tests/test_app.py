import pytest

from fastapi.testclient import TestClient
from app.main import app


client = TestClient(app)
headers = {"Content-Type": "application/json"}


@pytest.mark.parametrize('string_combos', pytest.valid_tests, indirect=True)
def test_successful_post(string_combos):
    input_string = string_combos[0]
    expected_output_string = string_combos[1]
    response = client.post("/test/", json={"string_to_cut": input_string})
    assert response.status_code == 200
    assert response.json() == {"return_string": expected_output_string}


def test_convert_input_post():
    """
    Pydantic will cast inputs as strings if input is an int or float
    """
    response = client.post("/test/", json={"string_to_cut": 123})
    assert response.status_code == 200
    assert response.json() == {"return_string": "3"}


