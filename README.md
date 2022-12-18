42CC TODO Test Task
----

# System requirements
- python 3.10 or higher.
- nodejs 16.x or higher.
- poetry 1.3.x.
- pnpm 7.18.x.
- Optionally heroku-cli, you can use any other platform to host your application, however.

# Local and remote deploy
Setup script should guide you through installation:
```shell
./scripts/setup.sh
```

If you cannot run the script, setup app manually:
- Create *.env* file, content:
  - `DEBUG=True`
  - `ALLOWED_HOSTS=*`
- Double check system requirements.
- Create virtualenv using poetry, `poetry install`.
- Install git hooks, `poetry run pre-commit install`.
- Install frontend dependencies, `cd frontend && pnpm install`.
- Configure platform where your code will be deployed. You can take command to run server from *Procfile*.
- Make sure that you have `DEBUG=False`, `ALLOWED_HOSTS=domain.yourhosting.com` and `SECRET_KEY=random32lenstring` set
  on your server.

To make it easy we keep frontend build artifacts in repository: *frontend/static*, before deploying on server please run
`cd frontend && pnpm run build` to rebuild static assets.

# How to work
1. Start timer.
2. Read task description on gitea carefully, understand the task requirements, if something is unclear - ask questions.
3. Plan your work before starting it, example:
    - [ ] Bootstrap project locally
    - [ ] Select hosting platform
    - [ ] Deploy project
    - [ ] Prepare TODO app wireframe
    - [ ] User can see TODO list
    - [ ] User can add a new entry to TODO list
    - [ ] ...
4. Self-review your code, cleanup any dead / commented-out code, print / console statements, run unittest tests.
5. Re-assign the task to your reviewer.

# How to code
1. You can prefix every command with `poetry run` or active virtualenv using `poetry shell`.
2. To start server run `poetry run inv devserver` (or, in activated virtualenv, `inv devserver`).
3. Local server is available at localhost:8000
4. [Options or Composition API?](https://vuejs.org/guide/introduction.html#api-styles) You probably know well the
    Options API of you know Composition API, use latter, otherwise take Options API.
