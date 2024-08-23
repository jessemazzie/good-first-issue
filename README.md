# good-first-issue
A Flask web app for finding open source projects to contribute to.

## Developing
```
# deploy Flask app locally (no container)
pip3 install -r requirements.txt
make run-dev

# deploy app to container using gunicorn
make build
make run-container

# deploy full stack (gunicorn container + nginx proxy)
make build
make compose-up
```