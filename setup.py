# -*- coding: utf-8 -*-
import sys
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

sys.path.insert(0, '.')
from idunnostill import __version__


setup(
    name="idunnostill",
    version=__version__,
    description="Flask based microservice.",
    maintainer="",
    packages=["idunnostill", "idunnostill.myservicce"],
    platforms=["any"]
)
