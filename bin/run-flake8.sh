#!/usr/bin/env sh
poetry run flake8 core addressbook authentication --exclude "migrations" #src tests --exclude "src/base.py","src/yielding.py","src/viscoelastic.py"