#!/usr/bin/env python3.10
import os

import datetime

from cs50 import SQL
from flask import Flask, render_template, request

from helpers import apology

from restcountries import RestCountryApiV2 as rapi

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///history.db")

@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/", methods=["get"])
def index():
    return render_template("index.html")

@app.route("/results")
def enter():
    count = db.execute("SELECT count(id) FROM history")
    next_id = count[0]['count(id)'] + 1
    country = request.form.get("country")
    query = '''
INSERT INTO history (id, country)
VALUES (?, ?)
    '''
    db.execute(query, next_id, country)
    return apology("TODO")

@app.route("/history")
def history():

    return apology("TODO")