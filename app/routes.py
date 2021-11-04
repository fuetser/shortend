from flask import render_template, jsonify, redirect, abort, request
from app import app
from .services import LinkService


@app.get("/")
def root():
    lang = request.args.get("lang", "en")
    return render_template("home.html", lang=lang)


@app.get("/<string:link>")
def short_link(link: str):
    if (associated_link := LinkService.get(link)) is not None:
        redirect_link = associated_link.original_link
        if not redirect_link.startswith("http"):
            redirect_link = f"http://{redirect_link}"
        return redirect(redirect_link, code=302)
    abort(404)


@app.post("/add")
def add_link():
    if (link := request.values.get("link")):
        shortened_link = LinkService.create(link)
        return jsonify({"link": shortened_link})
    return jsonify({"link": "Error"})
