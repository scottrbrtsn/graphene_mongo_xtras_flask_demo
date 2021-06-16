import graphene
from graphene.relay import Node
from graphene_mongo import MongoengineObjectType
from graphene_mongo_xtras_flask_demo.models.mongo_models import (
        User as UserModel, 
        Person as PersonModel, 
        Group as GroupModel
        )

class User(MongoengineObjectType):
    class Meta:
        model = UserModel
        interfaces = (Node,)

class Person(MongoengineObjectType):
    class Meta:
        model = PersonModel
        interfaces = (Node,)

class Group(MongoengineObjectType):
    class Meta:
        model = GroupModel
        interfaces = (Node,)
