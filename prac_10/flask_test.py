"""CP1404 Prac 10"""

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h1> Hello World! :)<h1>'

@app.route('/greet')
@app.route('/greet/<name>')
def greet(name=''):
    return f"Hello {name}"

def convert_fahrenheit_to_celsius(fahrenheit):
    """Convert temperature from fahrenheit to celsius"""
    celsius = 5 / 9 * (fahrenheit - 32)
    return celsius

@app.route('/f/<celsius>')
def convert_celsius_to_fahrenheit(celsius):
    """Convert temperature from celsius to fahrenheit"""
    fahrenheit = int(celsius) * 9.0 / 5 + 32
    return f"{celsius} degrees C is {fahrenheit} degrees F"

if __name__ == '__main__':
    app.run()