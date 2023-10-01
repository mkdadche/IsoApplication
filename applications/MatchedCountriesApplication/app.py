# Standard Library
from io import BytesIO

# Third-Party Libraries
from flask import Flask, request, jsonify
import pandas as pd
from flasgger import Swagger, swag_from
from flask_cors import CORS

# Custom or Project-Specific Modules
from model import get_matched_countries


app = Flask(__name__)
CORS(app)
Swagger(app, template_file="swagger/match_country.yml")

@app.route("/match_country", methods=["POST"])
@swag_from("swagger/match_country.yml")
def match_country():
    """
    Match Countries
    ---
    parameters:
      - name: iso
        in: formData
        type: string
        required: true
        description: ISO code to match countries with
      - name: countries
        in: formData
        type: array
        items:
          type: string
        required: true
        description: List of countries to match against the ISO code
    responses:
      200:
        description: List of matched countries
        schema:
          type: array
          items:
            type: string
      400:
        description: Invalid request
    """
    request_data = request.get_json()

    iso = request_data.get("iso")
    countries = list(request_data.get("countries"))

    if iso is None or countries is None:
        return jsonify({"error": "Invalid request"}), 400

    matched_countries = get_matched_countries(iso, countries)
    # Store matched countries in the cache

    response = {
        "iso": iso,
        "match_count": len(matched_countries),
        "matches": matched_countries,
    }

    return jsonify(response), 200


if __name__ == "__main__":
    app.run(debug=True)