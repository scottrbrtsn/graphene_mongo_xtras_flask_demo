# Use the Python3.8 image
FROM python:3.8

# Set the working directory to /app
WORKDIR /graphene_mongo_xtras_flask_demo

# just copy the toml here so if we make changes to the project we don't have to rebuild everything from zero
COPY ./pyproject.toml /graphene_mongo_xtras_flask_demo/pyproject.toml

ENV POETRY_VIRTUALENVS_PATH=/venv
# Install the dependencies
RUN pip install --user poetry pip uWSGI --upgrade \
&&  python -m poetry install

# Copy the current directory contents into the container at /app 
COPY . /graphene_mongo_xtras_flask_demo

ENTRYPOINT ["/bin/bash", "/graphene_mongo_xtras_flask_demo/entrypoint.sh"]
# run the command to start uWSGI
CMD ["/root/.local/bin/uwsgi", "api.ini"]
