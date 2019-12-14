# -*- coding:utf-8 -*-
from flask import render_template
from app import app
from static.Form import card_selection


@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'BlueRain77'}
    return render_template("index.html", title="Home", user=user)


@app.route('/cardselection')
def cardselection():
    form = card_selection()
    return render_template("test.html",form=form)

# @app.route('/songs')
# def Songs():
#     return render_template('test.html')
