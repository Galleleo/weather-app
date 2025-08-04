from flask import Flask, render_template, request

app = Flask(__name__, template_folder='flask_bootstrap_templates')
from weather_app import WeatherApp


weather_service = WeatherApp()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/weather', methods=['POST'])
def get_weather():
    city = request.form.get('city', '').strip()
    if not city:
        return render_template('index.html', error="Please enter a city name")
    
    weather_data = weather_service.get_weather(city)
    
    if "error" in weather_data:
        return render_template('index.html', error=weather_data['error'])
    
    return render_template('weather.html', weather=weather_data)

if __name__ == '__main__':
    app.run(debug=True, port=5000)