import graphene
from graphene.relay import Node
from graphene_mongo import MongoengineObjectType, MongoengineConnectionField
from graphene_mongo_xtras_flask_demo.models.mongo_models import (
        User as UserModel, 
        Person as PersonModel, 
        Group as GroupModel
        )

from graphene_mongo_extras.filtering.fields import FilteringConnectionField
from graphene_mongo_extras import MongoengineExtrasType

class User(MongoengineExtrasType):
    class Meta:
        model = UserModel
        interfaces = (Node,)
        connection_field_class = FilteringConnectionField

class Person(MongoengineObjectType):
    class Meta:
        model = PersonModel
        interfaces = (Node,)
        connection_field_class = MongoengineConnectionField

class Group(MongoengineObjectType):
    class Meta:
        model = GroupModel
        interfaces = (Node,)
        connection_field_class = MongoengineConnectionField

