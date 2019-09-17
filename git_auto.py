# TODO: create a new branch named auto
# TODO: add a cred.py file to .gitignore
# TODO: create a cred.py file with your username, password & email
# TODO: create a git_auto.py file
# TODO: install qaviton_git
# TODO: create a script to automatically
#  commit and push every 10 seconds
from qaviton_git import Git
from qaviton_helpers import try_to, multi_try, DynamicWait
from cred import user, password, email


git = Git(
    password=password,
    username=user,
    email=email,
)

try_to(git.create_remote)
while True:
    wait = DynamicWait()
    multi_try(
        lambda: git.commit("auto commit"),
        git.pull,
        git.push)
    wait(10)
