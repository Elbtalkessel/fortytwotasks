import os
import secrets
import threading

from invoke import task


@task
def devserver(c):
    """
    Starts django and node server
    """
    threads = [
        threading.Thread(target=c.run, args=("python manage.py runserver 0.0.0.0:8000",)),
        threading.Thread(target=c.run, args=("cd frontend && pnpm run dev",)),
    ]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()


@task
def runserver(c):
    c.run("DEBUG=False gunicorn -b 0.0.0.0:8000 settings.wsgi")


@task
def test(c):
    c.run("coverage run manage.py test --noinput")
    try:
        c.run("coverage html")
        c.run("coverage report")
    except Exception as e:
        if browser := os.environ.get("BROWSER"):
            c.run(f"{browser} ./htmlcov/index.html")
        raise e


@task
def style(c):
    c.run("pre-commit run --all-files")


@task
def build(c):
    c.run("cd frontend && pnpm run build")


@task
def setup(c):
    while (ans := input("Deploy to heroku? (Y/n) ").lower()) not in ["y", "n"]:
        print(" type `y` to say yes or `n` to say no.")
    if ans == "n":
        print("You can host your application on any other platform, for example https://www.pythonanywhere.com/")
        return
    try:
        # throws exception if exit code not 0
        c.run("which heroku", hide=True)
    except Exception:
        print(
            "Please install and configure heroku-cli first https://devcenter.heroku.com/articles/heroku-cli. "
            "If you choice deploying somewhere else, please don't forget to set DEBUG, SECRET_KEY and ALLOWED_HOSTS "
            "environment variables (or use .env file on remote server)."
        )
        return

    # create application with a random name, if user didn't log in yet, the create command will prompt to do so.
    c.run("heroku create", pty=True)
    # setting env vars
    c.run("heroku config:set DEBUG=False")
    if not c.run("heroku config:get SECRET_KEY").stdout.strip():
        c.run(f"heroku config:set SECRET_KEY={secrets.token_urlsafe(32)}")
    else:
        print("SECRET_KEY is already set on heroku, skipping...")
    if domain := c.run("heroku domains | tail -1").stdout.strip():
        c.run(f"heroku config:set ALLOWED_HOSTS={domain}")
    else:
        print("Cannot determine your app domain, please set ALLOWED_HOSTS on heroku manually.")

    # if current branch is master, push to heroku
    result = c.run("git rev-parse --abbrev-ref HEAD", hide=True)
    if result.stdout.strip() == "master":
        c.run("git push heroku master")
    else:
        print("To deploy application switch to master branch and run `git push heroku master`")
    print(
        "Before each deploy don't forget to run `poetry run inv build` to rebuild static assets and refresh "
        "requirements file."
    )
