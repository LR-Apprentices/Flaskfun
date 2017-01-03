from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('layout.html', title="Home")

	
@app.route('/Alone')
def alone():
    return render_template('Alone.html', title="Naruto - Alone")


@app.route('/Drunken')
def drunkensailor():
    return render_template('Drunken.html', title="Irish Sailors - Drunken Sailors")

@app.route('/Hokage')
def hokagefuneral():
    return render_template('HokageFuneral.html', title="Naruto - Hokage Funeral")