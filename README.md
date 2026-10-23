# Flask CI/CD Learning Project

A small Flask application used to practice automated linting, endpoint tests, Docker packaging, and deployment through GitHub Actions.

## Project Overview

The application has two routes:

- `GET /` returns `Hello, World!`.
- `GET /add/<int:a>/<int:b>` returns the sum of two integer path parameters.

## Methodology

1. Implement HTTP routes in [app/main.py](app/main.py).
2. Use Flask's test client with pytest to check the home response and `/add/3/4` → `7` in [tests/test_main.py](tests/test_main.py).
3. Run flake8 and pytest through the [GitHub Actions workflow](.github/workflows/ci.yml) on pushes and pull requests to `main`.
4. On pushes, build and publish a Docker image to GitHub Container Registry after the checks, then deploy over SSH using repository secrets.

## Results and Limitations

The uploaded source implements the greeting and addition endpoints and includes two automated test cases. The repository also contains the Docker build and deployment workflow. These are implementation outcomes; a successful live deployment or current CI pass is not asserted here.

Deployment requires a configured server, Docker, registry access, and the `SERVER_HOST`, `SERVER_USER`, and `SERVER_SSH_KEY` repository secrets.

## Run Locally

Use Python 3.12, matching the CI workflow and Docker image.

```bash
git clone https://github.com/jarichooo/SE2-Finals-LT.git
cd SE2-Finals-LT
python -m venv .venv
# Activate .venv using the command for your shell.
python -m pip install -r requirements.txt
python -m flask --app app.main run
```

Open `http://127.0.0.1:5000/` or `http://127.0.0.1:5000/add/3/4`.

From the repository root, run the checks:

```bash
python -m flake8 app/
python -m pytest tests/
```

Build and run with Docker:

```bash
docker build -t se2-finals-lt .
docker run --rm -p 5000:5000 se2-finals-lt
```

## Source, Data, and Documentation

- [app/](app/) — Flask source code.
- [tests/](tests/) — endpoint tests.
- [requirements.txt](requirements.txt) — Python dependencies.
- [Dockerfile](Dockerfile) — container build and runtime.
- [.github/workflows/ci.yml](.github/workflows/ci.yml) — lint, test, image publication, and deployment steps.

No dataset or database is required. Requests supply the addition inputs.

## Topics

`python` · `flask` · `pytest` · `docker` · `github-actions` · `ci-cd` · `student-project`
