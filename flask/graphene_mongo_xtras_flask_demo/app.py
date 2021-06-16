import os
from flask import Flask
from flask_graphql import GraphQLView
from flask_mongoengine import MongoEngine, MongoEngineSessionInterface
from mongoengine.connection import disconnect

from graphene_mongo_xtras_flask_demo.models.sql_models import sql_db_session
from graphene_mongo_xtras_flask_demo.schema import schema, Department

app = Flask(__name__)
app.debug = True

app.config['MONGODB_SETTINGS'] = {
    'db': os.getenv('MONGO_DB', default="example-db"),
    'host': os.getenv('MONGO_HOST', default="mongodb"),
    'username': os.getenv('MONGO_USER', default="cronus"),
    'password': os.getenv('MONGO_PASSWORD', default="password"),
    'port': int(os.getenv('MONGO_PORT', default="27017")),
    'connect': False
}

try:
    db = MongoEngine(app)
    app.session_interface = MongoEngineSessionInterface(db)
except Exception as e:
    app.logger.error(e)
    app.logger.error("Could not create connection to Mongo")

app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view(
        'graphql',
        schema=schema,
        graphiql=True # for having the GraphiQL interface
    )
)

@app.teardown_appcontext
def shutdown_session(exception=None):
    sql_db_session.remove()

@app.route('/')
def hello():
    return "Hello World!"

@app.route('/<name>')
def hello_name(name):
    return "Hello {}!".format(name)

if __name__ == '__main__':
    app.run()
