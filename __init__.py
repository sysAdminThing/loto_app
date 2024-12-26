import os

from flask import Flask, render_template, jsonify, session, Blueprint


def create_app():
    app = Flask(__name__, template_folder='templates')
    app.secret_key = os.urandom(24)

    from .main import main

    app.register_blueprint(main, url_prefix='/')

    return app

