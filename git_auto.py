# TODO: create a new branch named auto
# TODO: add a cred.py file to .gitignore
# TODO: create a cred.py file with your username, password & email
# TODO: create a git_auto.py file
# TODO: install qaviton_git
# TODO: create a script to automatically
#  commit and push every 10 seconds
from qaviton_git import Git
from cred import user, password, email
from time import time, sleep


git = Git(
    password=password,
    username=user,
    email=email,
)
while True:
    t = time()
    try:
        git.commit("auto commit")
        git.pull()
        git.push()
    except:
        pass
    t = time() - t
    if t < 10:
        sleep(10-t)
