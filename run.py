#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/eventos')
def eventos():
    return render_template('eventos.html')

@app.route('/quienes_somos')
def quienes_somos():
    return render_template('quienes_somos.html')

@app.route('/como_funciona')
def como_funciona():
    return render_template('como_funciona.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0')
#    app.run(debug=True, host='0.0.0.0')
