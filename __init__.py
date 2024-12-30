import os
import random
import json
from datetime import timedelta

from flask import Flask, render_template, jsonify, session, Blueprint,request, redirect, url_for
from functools import wraps


def create_app():
    app = Flask(__name__, template_folder='templates')
    app.secret_key = os.urandom(24)
    app.SESSION_PERMANENT = False
    app.SESSION_COOKIE_NAME = 'loto_game_123'
    app.PERMANENT_SESSION_LIFETIME = timedelta(hours=18)
    from .main import main

    app.register_blueprint(main, url_prefix='/')

    return app

