import logging
import os
import sys

from flask import Flask
from flask import render_template


app = Flask(__name__, instance_relative_config=True)
app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.setLevel(logging.DEBUG)


def configure_app(app):
    # from default in config dir
    app.config.from_object('config.default.Config')
    try:
        # from config in instance dir
        app.config.from_object('instance.config.Config')
    except ImportError:
        pass
    is_production = os.getenv('IS_PRODUCTION', None)
    if is_production:
        app.config.from_object('config.production.Config')

configure_app(app)


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

