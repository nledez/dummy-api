![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/nledez/dummy-api/docker)
![Docker Pulls](https://img.shields.io/docker/pulls/nledez/dummy-api)

Install
=======

```
./install.sh
./.venv/bin/python app.py
./.venv/bin/python app.py --help
./.venv/bin/python app.py --name=test_from_command_line
```

Build and run with Docker
=========================

```
docker build -t dummy-api:latest .
docker run --env-file=test.env -p 5000:5000 dummy-api:latest
```
