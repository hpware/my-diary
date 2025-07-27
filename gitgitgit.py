import os
import git
from dotenv import load_dotenv
import re

load_dotenv()

github_repo = os.getenv("github_repo")

pattern = r"^[a-zA-Z0-9-]{1,39}/[a-zA-Z0-9-_.]{1,100}$"

if not github_repo or not re.match(pattern, github_repo):
    print(f"Cannot run with repo name {github_repo}")
    exit()


repo = git.Repo.clone_from(f"https://github.com/{os.getenv("github_repo")}",
                           './data',
                           branch=f'{os.getenv("git_branch")}')
