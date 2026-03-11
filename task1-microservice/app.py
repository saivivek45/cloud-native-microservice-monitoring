from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route("/")
def get_location():
    try:
        response = requests.get("http://ip-api.com/json/")
        data = response.json()

        location = {
            "city": data.get("city"),
            "region": data.get("regionName"),
            "country": data.get("country"),
            "latitude": data.get("lat"),
            "longitude": data.get("lon")
        }

        return jsonify(location)

    except Exception as e:
        return jsonify({"error": "Unable to fetch location"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
