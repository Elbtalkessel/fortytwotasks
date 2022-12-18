#!/usr/bin/env sh

checkPkg() {
  if [ ! -x "$(which $1)" ]
  then
    echo "$2"
    exit 1
  fi
}
checkVer() {
  if [ "$1" != "$2" ]
  then
    echo "$3"
    exit 1
  fi
}

checkPkg poetry "Please install poetry https://python-poetry.org/docs/#installation"
checkVer "$(poetry -V --no-ansi | grep -Po "\d+.\d+")" "1.3" "poetry version 1.3.x is required."
checkPkg node "Please install nodejs https://github.com/nvm-sh/nvm"
checkPkg pnpm "Please install pnpm https://pnpm.io/installation"

poetry install
poetry run pre-commit install
cd frontend || exit 1
pnpm install
cd - || exit 1

if [ ! -f ".env" ]
then
cat << "EOF" >> .env
DEBUG=True
ALLOWED_HOSTS=*
EOF
fi

poetry run inv setup
