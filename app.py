from dotenv import load_dotenv
from flask import Flask, render_template
from apscheduler.schedulers.background import BackgroundScheduler
import os

load_dotenv()

def sensor():
    """ Function for test purposes. """
    print("Scheduler is alive!")

sched = BackgroundScheduler(daemon=True)
sched.add_job(sensor,'interval',minutes=60)
sched.start()

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
