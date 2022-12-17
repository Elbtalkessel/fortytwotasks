#!/usr/bin/env sh

checkPkg() {
  if [ ! -x "$(which $1)" ]
  then
    echo "$2"
    exit 1
  fi
}

checkPkg poetry "Please install poetry https://python-poetry.org/docs/#installation"
checkPkg node "Please install nodejs https://github.com/nvm-sh/nvm"
checkPkg pnpm "Please install pnpm https://pnpm.io/installation"
checkPkg heroku "Please install and configure heroku-cli https://devcenter.heroku.com/articles/heroku-cli"

poetry install
poetry run pre-commit install
cd frontend || exit 1
pnpm install

cat << 'EOF'
Ready.
Use `poetry run inv devserver` to start server, or manually start django and node server.
Use `poetry run inv test` to run unittests, or switch to virtual environment using `poetry shell` and run `coverage run manage.py test`.
EOF
