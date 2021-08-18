from secrets import token_urlsafe
from flask import render_template, jsonify, redirect, abort
from app import app
from .services import LinkService


@app.get("/")
def root():
    return render_template("home.html")


@app.get("/<string:link>")
def short_link(link: str):
    if (associated_link := LinkService.get(link)) is not None:
        return redirect(f"https://{associated_link}", code=302)
    abort(404)


@app.post("/add/<string:link>")
def add_link(link: str):
    shortened_link = token_urlsafe(6)
    LinkService.create(link, shortened_link)
    return jsonify({"link": shortened_link})
