from flask import render_template, flash, redirect, url_for, request
from website import app, db


@app.route("/")
@app.route("/home", methods=['GET', 'POST'])
def home():
    return render_template('index.html', title='home')

@app.route("/gallery", methods=['GET', 'POST'])
def gallery():
    return render_template('gallery.html')

@app.route("/events", methods=['GET', 'POST'])
def events():
    return render_template('events_and_packages.html')

@app.route("/playlist", methods=['GET', 'POST'])
def playlist():
    return render_template('playlist.html')
