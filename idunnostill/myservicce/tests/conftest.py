# -*- coding: utf-8 -*-
import pytest

from idunnostill import create_app


@pytest.fixture
def app():
    app = create_app()
    return app
