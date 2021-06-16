#!/bin/sh

export VIRTUAL_ENV=$(/root/.local/bin/poetry env info -p)
# python -m poetry config virtualenvs.in-project true
# test if you mounted the dir that has the virtualenv in it.. so we need to recreate it
# this lets you have the venv outside your container and lets you play with that if you need to
# stat /graphene_mongo_xtras_flask_demo/flask/.venv/ || python -m poetry install

# init the database with some example data
stat /graphene_mongo_xtras_flask_demo/database.sqlite3 || /root/.local/bin/poetry run python graphene_mongo_xtras_flask_demo/models/sql_models.py 

# just run all our commands we passed
$@
