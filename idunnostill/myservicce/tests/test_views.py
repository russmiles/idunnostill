# -*- coding: utf-8 -*-
from flask import url_for


def test_myservicce_index(client):
    res = client.get(url_for('myservicce_app.index'))
    assert res.data == b'Hello World!'
