# -*- coding: utf-8 -*-
from flask import Blueprint

__all__ = ['myservicce_app']

myservicce_app = Blueprint('myservicce_app', __name__)


@myservicce_app.route('/')
def index():
    return "Hello World!"
