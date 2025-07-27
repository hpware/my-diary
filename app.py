from dotenv import load_dotenv
from flask import Flask, render_template
from apscheduler.schedulers.background import BackgroundScheduler
import os
import git
load_dotenv()


# git
repolink = f"https://github.com/{os.getenv("github_repo")}"
branch = os.getenv("git_branch")
if (os.path.isdir("./data") == False ):
    repo = git.Repo.clone_from(repolink, './data', branch=branch)
else:
    repo = git.Repo("./data")


# testing
def sensor():
    """ Function for test purposes. """
    print("Scheduler is alive!")

sched = BackgroundScheduler(daemon=True)
sched.add_job(sensor,'interval',minutes=60)
sched.start()


# web service
app = Flask(__name__)
@app.route("/")
def index():
    contentArray = [
        {
            "year": 2025,
        "url": "hi",
        "title": "Hello",
        "description": "Hello world"
        },
        {
            "year": 2025,
        "url": "hi",
        "title": "Hello",
        "description": "Hello world"
        }
    ]
    return render_template("index.html", contentArray=contentArray)

@app.route("/<year>/<slug>")
def diraryPage(year, slug):
    try:
        if len(year) != 4:
            return render_template("error.html")
        return render_template("dirary_template.html", content="# Here is the markdown content yo", title=slug, year=year)
    except:
        return render_template("error.html")

@app.route("/api/submit")
def submitApi():
    return {
        "success": True
    }
