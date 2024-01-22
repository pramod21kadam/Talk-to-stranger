from flask import render_template, request
from flask.views import MethodView
import utilities.globals as globals
from .base import *

class HomeController(MethodView):
    def get(self, id):
        try:
            globals.active.append(request.remote_addr)
            return render_template('dashboard.html', title="Talk To Strangers")
        except Exception as error:
            return failureRes(f"{error}"), 500