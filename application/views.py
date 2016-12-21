from flask import Flask, render_template, request

app = Flask(__name__)
app.config['DEBUG'] = True


@app.route('/layout')
def layout():
    return render_template('layout.html')


@app.route('/')
def home():
    return "Hello World"


@app.route('/Alone')
def alone():
    return render_template('Alone.html')


@app.route('/Drunken')
def drunkensailor():
    return render_template('Drunken.html')
