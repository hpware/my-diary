from dotenv import load_dotenv
from flask import Flask, render_template

load_dotenv()
app = Flask(__name__)
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/<slug>")
def diraryPage(slug):
    return render_template("dirary_template.html", content="# Here is the markdown content yo", title=slug)
