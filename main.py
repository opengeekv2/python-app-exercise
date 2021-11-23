#!/usr/bin/env python
import sys

from src.Application.AppBuilder import AppBuilder
from src.Application.App import App


app: App = AppBuilder().build()

sys.exit(app.run())
