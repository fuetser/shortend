from flask import render_template
from app import app


@app.errorhandler(404)
def handle_page_not_found(error):
    return render_template("error404.html")
