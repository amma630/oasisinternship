from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

API_KEY = "ed42eadd680182195cf5bd7ecac337c6"
API_URL = "https://api.openweathermap.org/data/2.5/weather?units=metric&q="

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/weather', methods=['GET'])
def weather():
    city = request.args.get('city')
    if city:
        response = requests.get(f"{API_URL}{city}&appid={API_KEY}")
        if response.status_code == 200:
            data = response.json()
            weather_data = {
                'city': data['name'],
                'temp': data['main']['temp'],
                'humidity': data['main']['humidity'],
                'wind': data['wind']['speed'],
                'weather': data['weather'][0]['main']
            }
            return jsonify(weather_data)
        else:
            return jsonify({'error': 'Invalid city name'}), 404
    return jsonify({'error': 'City not provided'}), 400

if __name__ == '__main__':
    app.run(debug=True)
