# -*- coding:utf-8 -*-
from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'BlueRain77'}
    return render_template("index.html", title="Home", user=user)


@app.route('/test')
def test():
    return render_template("test.html")
