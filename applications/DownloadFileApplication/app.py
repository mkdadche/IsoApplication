# Standard Library
from io import BytesIO
import os

# Third-Party Libraries
from flask import Flask, request
from flask_cors import CORS
import pandas as pd

# Custom or Project-Specific Modules
from model import send_excel_response

app = Flask(__name__)
CORS(app)

# Add a new route to download the Excel file
@app.route("/download_excel", methods=["POST"])
def download_excel():
    request_data = request.get_json()
    iso = request_data.get("iso")
    matched_countries = request_data.get("countries")

    # Generate a DataFrame from the result data
    df = pd.DataFrame({
        "ISO": iso,
        "Matched Countries" : matched_countries,
    })

    # Create an in-memory Excel file and write the DataFrame to it
    excel_output = BytesIO()
    with pd.ExcelWriter(excel_output, engine='xlsxwriter') as writer:
        df.to_excel(writer, sheet_name="Matching Countries", index=False)

    excel_output.seek(0)

    # Send the Excel file as a downloadable attachment
    return send_excel_response(excel_output.read(), "matching_countries")


if __name__ == "__main__":
    app.run(debug=True)