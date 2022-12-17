import os
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
def test(c):
    c.run("coverage run manage.py test")
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
