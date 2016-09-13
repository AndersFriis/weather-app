from wtforms import Form, StringField

class WeatherForm(Form)
    city = StringField("City")
    Country_code = StringField("Country Code")
    