# Welcome to graphene_mongo_xtras_flask_demo!
This takes [graphene-mongo-extras](https://github.com/riverfr0zen/graphene-mongo-extras) and integrates it into a graphql-api cookie cutter project called [Cronus](https://gitlab.com/usmcamp0811/cronus/-/tree/graphql-api)

Graphene Mongoengine Filtering Flask Demo
# graphene_mongo_xtras_flask_demo

1. `cd flask`
2. `poetry install`
3. `poetry shell`
4. `flask run` #make sure FlASK-APP env variable is set, and mongo environment is correct. see /graphene_mongo_xtras_flask_demo/app.py 
5. `http://localhost:5000/graphql`
6. [Add Users](https://github.com/scottrbrtsn/graphene_mongo_xtras_flask_demo-/blob/master/flask/graphql_default_queries/add_user.graphql)
7. [Get Filtered Users](https://github.com/scottrbrtsn/graphene_mongo_xtras_flask_demo-/blob/master/flask/graphql_default_queries/get_filtered_users.graphql)
