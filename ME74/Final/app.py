from flask import Flask, jsonify, render_template, request
from flask_cors import CORS  # Import CORS

import automate as automate
import manual as manual
import airtable as airtable

app = Flask(__name__)
CORS(app)

# Define two Python scripts as functions
def run_script_1():
    stat = manual.movewindow()
    return "Manual ran successfully! Window is currently: " + stat

def run_script_auto():
    automate.automate()
    return "Automate ran successfully!"

def run_update(numbers):
    airtable.post_weather_info(numbers)
    return "Update ran successfully!"

@app.route('/')
def index():
    return render_template('index.html')  # This will render index.html from the templates folder


@app.route('/run_script_1', methods=['GET'])
def script_1():
    result = run_script_1()  # Call your first script
    return jsonify({"message ": result})

@app.route('/run_script_auto', methods=['GET'])
def script_auto():
    result = run_script_auto()
    return jsonify({"message: ": result})

@app.route('/run_update', methods=['POST'])
def update():
    data = request.get_json()
    print(data)
    humidity = data.get('humidity')
    temperature = data.get('temperature')
    uv_index = data.get('uvIndex')
    rain = data.get('rain')
    wind_speed = data.get('windSpeed')
    numbers = [temperature, humidity, uv_index, rain, wind_speed]
    result = run_update(numbers)
    return jsonify({"message: ": result})

if __name__ == '__main__':
    app.run(debug=True)
