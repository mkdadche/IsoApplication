# Third-Party Libraries
import requests
from mtranslate import translate
from cachetools import TTLCache

# Initialize a TTL (Time-to-Live) cache with a maximum size (hold 100 item) and expiration time (3600 seconds)
cache = TTLCache(maxsize=100, ttl=3600)

# Function to translate a list of country names to English
def translate_countries(country_list):
    translated_countries = []
    for country in country_list:
        translated = translate(country, "en")
        translated_countries.append(translated)
    return translated_countries

# Function to get ISO country codes using REST Countries API
def get_iso_country_codes(country_list):
    iso_country_codes = []
    base_url = "https://restcountries.com/v3/name/"
    
    for country_name in country_list:
        try:
            # Check if ISO code lookup is in cache
            if country_name in cache:
                iso_data = cache[country_name]
            else:
                response = requests.get(base_url + country_name)
                data = response.json()
                
                if response.status_code == 200 and len(data) > 0:
                    cca3 = data[0].get('cca3', "N/A")
                    cca2 = data[0].get('cca2', "N/A")
                    iso_data = (cca3, cca2)
                    cache[country_name] = iso_data  # Cache the ISO data
                else:
                    iso_data = ("N/A", "N/A")
                
                cache[country_name] = iso_data  # Cache the ISO data
            
            iso_country_codes.append(iso_data)
        except requests.exceptions.RequestException as e:
            print(f"Error fetching data for {country_name}: {e}")
            iso_country_codes.append(("N/A", "N/A"))
    
    return iso_country_codes

def get_matched_countries(iso_code, country_list):
    iso_code = iso_code.upper()
    translated_countries = translate_countries(country_list)
    iso_country_codes = get_iso_country_codes(translated_countries)
    
    matching_countries = []
    for i, (cca3, cca2) in enumerate(iso_country_codes):
        if cca3 == iso_code or cca2 == iso_code:
            matching_countries.append(country_list[i])
    
    return matching_countries
