from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS
import requests

app = Flask(__name__, static_folder='static')
CORS(app)

@app.route('/')
def index():
    print("Serving index.html")
    return send_from_directory('', 'index.html')

@app.route('/visa-data')
def visa_data():
    url = "https://visacent.com/la/api/visa_eligible_countries/Tanzania"
    headers = {
        "X-Mashape-Host": "visacent",
        "X-Mashape-Key": "visacent@2018"
    }
    print("Calling external visa API...")
    try:
        response = requests.get(url, headers=headers)
        print(f"API Response Code: {response.status_code}")
        print(f"API Raw Response: {response.text[:300]}...")  # only show a snippet
        data = response.json().get('data', {})
        print("Visa data extracted and returned to frontend.")
        return jsonify(data)
    except Exception as e:
        print("Error during visa API call:", e)
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    print("Starting Flask server on http://localhost:5000")
    app.run(debug=True)