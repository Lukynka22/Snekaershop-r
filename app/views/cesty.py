from app import app, request, render_template, redirect, session, url_for, make_response
import os
import json

from flask import jsonify


def precti_json(nazev_souboru):
    try:
        with open(f"static/data/{nazev_souboru}.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}








@app.route("/")
def zakladni():
    return render_template("web.html")

@app.route("/Tenisky.html")
def tenisky():
    return render_template("Tenisky.html")

@app.route("/Přihlásit se.html")
def prihlasit():
    return render_template("Přihlásit se.html")

@app.route("/O nás.html")
def onas():
    return render_template("O nás.html")


@app.route("/web.html")
def web():
    return render_template("web.html")


@app.route("/Kontakty.html")
def kontakty():
    return render_template("Kontakty.html")



@app.route("/cesta")
def cesta():
    objekt = {
        "klic1": "ahoj",
        "klic2": 123,
        "klic3": 3.1415,
        "pole": [1, 2, 3, 4],
        "objekt": {
            "klic11": "test",
        }
    }

    return jsonify(objekt)
