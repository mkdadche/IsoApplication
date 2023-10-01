import requests
from model import get_iso_country_codes, get_matched_countries
from requests.exceptions import RequestException
from flask import Response
import pytest

def test_get_matched_countries():
    # Test a case where the country code matches one of the country.
    assert get_matched_countries("US", ["USA", "Russia", "Austria"]) == ["USA"]

    # Test a case where the country code does not match any country.
    assert get_matched_countries("Can", ["Mexico", "Japan"]) == []

    # Test a case with an empty country list.
    assert get_matched_countries("FRA", []) == []

    # Test a case with a longer country code.
    assert get_matched_countries("FRANCE", ["France", "Spain"]) == []

    # Test a case where the country code is matching multiple country names in different languages.
    assert get_matched_countries("IT", ["Italy", "italia", "Argentina"]) == ["Italy","italia"]
    
    # Test a case where the country code is matching multiple country names in different languages.
    assert get_matched_countries("svk", ["slovakia", "Eslovaquia", "Argentina"]) == ["slovakia","Eslovaquia"]

    # Test a case where the country code is empty.
    assert get_matched_countries("", ["USA", "Russia", "Austria"]) == []

    # Test another case where the country code is empty with an empty country list.
    assert get_matched_countries("", []) == []

    # Test a case where there is a city name in the country list to test the lines 32-35 in model.py.
    assert get_matched_countries("US", ["USA", "prague", "Austria"]) == ["USA"]

@pytest.fixture
def mock_requests_get_exception(monkeypatch):
    def mock_get(*args, **kwargs):
        raise requests.exceptions.RequestException("Simulated exception")

    monkeypatch.setattr(requests, "get", mock_get)

def test_request_exception_handling(mock_requests_get_exception):
    # Define a list of countries to test
    country_list = ["Country1", "Country2"]

    # Call the function and capture the output
    iso_country_codes = get_iso_country_codes(country_list)

    # Check that the function returned the expected values
    expected_result = [("N/A", "N/A"), ("N/A", "N/A")]
    assert iso_country_codes == expected_result