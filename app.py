#!/usr/bin/env python3.10
import os

import datetime

from cs50 import SQL
from flask import Flask, render_template, request

from helpers import apology

from country_api import CountryAPI
rapi = CountryAPI()

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


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/enter", methods=["GET"])
def enter():
    return render_template('enter.html')

@app.route("/info", methods = ["POST"])
def thing():
    country = request.values.get("country")
    country_info = rapi.get_countries_by_name(country)
    name = country_info['name']
    count = db.execute("SELECT count(id) FROM history")
    next_id = count[0]['count(id)'] + 1
    query = '''
    INSERT INTO history (id, country)
    VALUES (?, ?)
        '''
    db.execute(query, next_id, name)

    return render_template("info.html", country_info=country_info, flag=country_info['flag']['large'])

def picture(country):
    country_flag = rapi.get_countries_by_name("SELECT name FROM history" ,filters=["flag"])
    return country_flag
def info():
    country = db.execute("SELECT name FROM history")
    flag = picture(country)
    information = thing(country)

    return information, flag

