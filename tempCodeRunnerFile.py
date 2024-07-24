from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = "ed42eadd680182195cf5bd7ecac337c6"
API_URL = "https://api.openweathermap.org/data/2.5/weather?units=metric&q="

@app.route('/', methods=['GET', 'POST'])
def index():
    weather_data = {}
    error = None
    if request.method == 'POST':
        city = request.form.get('city')
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
            else:
                error = "Invalid city name"

    return render_template('index.html', weather_data=weather_data, error=error)

if __name__ == '__main__':
    app.run(debug=True)
