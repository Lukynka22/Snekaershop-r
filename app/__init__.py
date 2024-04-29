from flask import Flask, request, render_template, redirect, session, url_for, make_response


app = Flask(__name__)
app.config["SECRET_KEY"] = "123456789"
app.config.from_object("config.Config")


from app.views import cesty
