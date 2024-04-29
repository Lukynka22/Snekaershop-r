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

def zapis_do_json(nazev_souboru, data_na_zapis):
    if not os.path.exists("static/data"):
        os.makedirs("static/data")

    try:
        with open(f"static/data/{nazev_souboru}.json", "r") as file:
            uzivatele = json.load(file)
    except FileNotFoundError:
        uzivatele = []

    uzivatele.append(data_na_zapis)

    with open(f"static/data/{nazev_souboru}.json", "w", encoding="utf-8") as file:
        json.dump(uzivatele, file)


@app.route('/zobraz-ucet')
def zobraz_ucet():
    username = session.get("username")
    color = request.cookies.get("color")
    if not color:
        color = "black"
        res = make_response(render_template("ucet.html", username=username))
        res.set_cookie("color", color)
        return res
    return render_template("ucet.html", username=username)


@app.route('/registrace', methods=["GET", "POST"])
def registrace():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        with open("static/data/users.json", "r") as file:
            uzivatele = json.load(file)

        for u in uzivatele:
            if u["username"] == username:
                return render_template("Registrace.html", error="Uživatelské jméno již existuje.")

        novy_uzivatel = {
            "username": username,
            "password": password,
            "color": "black"
        }

        zapis_do_json("users", novy_uzivatel)

        session["username"] = username
        return redirect(url_for("prihlasit"))

    return render_template("Registrace.html")


@app.route("/zpracuj-prihlaseni", methods=["POST"])
def zpracuj_prihlaseni():
    username = request.form.get("username")
    password = request.form.get("password")

    with open("static/data/users.json", "r") as file:
        uzivatele = json.load(file)

    for u in uzivatele:
        if u["username"] == username and u["password"] == password:
            session["username"] = username
            return redirect(url_for("zobraz_ucet"))
    return render_template("Přihlásit se.html", error="Neplatné přihlašovací údaje.")















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
