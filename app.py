from dotenv import load_dotenv
from flask import Flask, render_template

load_dotenv()
app = Flask(__name__)
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/<year>/<slug>")
def diraryPage(year, slug):
    try:
        if len(year) != 4:
            return render_template("error.html")
        return render_template("dirary_template.html", content="# Here is the markdown content yo", title=slug, year=year)
    except:
        return render_template("error.html")
