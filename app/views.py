from flask import render_template

from app import app

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/current", methods=["GET", "POST"])
def current_weather():
    weather_form = WeatherForm(request.form)
    
    return render_template("current.html", 
        weather_form=weather_form)


@app.route("/forecast", methods=["GET", "POST"])
def current_weather():
    return render_template("forecast.html")


