#!/usr/bin/env python

from src.Application.AppBuilder import AppBuilder
from src.Application.App import App


app: App = AppBuilder().build()

app.api_service().run()
