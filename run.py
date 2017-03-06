#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask
from flask import render_template


# app = Flask(__name__, static_url_path="", static_folder="static")
app = Flask(__name__)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.route('/')
def index():
#    return app.root_path
    return render_template('index.html')


if __name__ == "__main__":
#    app.run(host='0.0.0.0')
    app.run(debug=True, host='0.0.0.0')
