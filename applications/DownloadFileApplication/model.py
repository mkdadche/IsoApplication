# Third-Party Libraries
from flask import Response

# Function to convert data to Excel and send it as a response
def send_excel_response(data, filename):
    response = Response(data)
    response.headers["Content-Type"] = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    response.headers["Content-Disposition"] = f"attachment; filename={filename}.xlsx"
    return response
