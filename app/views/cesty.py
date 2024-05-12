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

@app.route("/smazani", methods=["GET", "POST"])
def smazani():
    if "username" in session:
        # Načtení uživatelů ze souboru users.json
        with open("static/data/users.json", "r") as file:
            users = json.load(file)


        for user in users:
            if session["username"] == user["username"]:
                users.remove(user)
                break


        with open("static/data/users.json", "w", encoding="utf-8") as file:
            json.dump(users, file)


        session.pop("username")

        response = redirect(url_for("web"))
        response.delete_cookie("username")
        return response
    else:
        return redirect(url_for("web"))




@app.route("/Odhlášení")
def odhlaseni():
    #pokud je uživatel přihlášen, získá se  jeho uživatelské jméno
    if "username" in session:
        username = session["username"]
    #odstranění uživatele ze session
    session.pop("username", None)
    return redirect(url_for("web"))


@app.route("/")
def zakladni():
    return render_template("webn.html")

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

@app.route("/kosik.html")
def kosik():
    return render_template("kosik.html")


@app.route("/payment_form.html")
def payment():
    return render_template("payment_form.html")


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

class PaymentGateway:
    @staticmethod
    def process_payment(credit_card_number, amount):
        return True


@app.route('/payment_form', methods=['GET', 'POST'])
def payment_form():
    if request.method == 'POST':
        credit_card_number = request.form['credit_card_number']
        amount = float(request.form['amount'])

        if PaymentGateway.process_payment(credit_card_number, amount):
            session['payment_success'] = True
            return redirect(url_for('payment_success'))
        else:
            return render_template('payment_failed.html')

    return render_template('payment_form.html')


@app.route('/payment_success')
def payment_success():
    if 'payment_success' in session:
        session.pop('payment_success')
        return render_template('payment_success.html')
    else:
        return redirect(url_for('payment_form'))

@app.route('/zpracuj-email', methods=["POST"])
def zpracuj_email():
    email = request.form.get("email")

    return redirect(url_for("web"))


@app.route('/Jordany.html')
def jordany():
    return render_template('Jordany.html')

@app.route('/Dunk.html')
def Dunk():
    return render_template('Dunk.html')

@app.route('/Ostatní.html')
def Ostatní():
    return render_template('Ostatní.html')

@app.route('/prvnibota.html')
def prvnibota():
    return render_template('prvnibota.html')

@app.route('/druhabota.html')
def druhabota():
    return render_template('druhabota.html')
