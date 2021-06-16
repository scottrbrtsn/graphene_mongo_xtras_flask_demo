import graphene
from graphene.relay import Node
from graphene_mongo import MongoengineObjectType
from graphene_mongo_xtras_flask_demo.queries.mongo_example import *
from graphene_mongo_xtras_flask_demo.models.mongo_models import (
        User as UserModel, 
        Person as PersonModel, 
        Group as GroupModel
        )

class PersonInput(graphene.InputObjectType):
    uid = graphene.Int(required=True)
    sid = graphene.String(required=True)
    fname = graphene.String()
    lname = graphene.String()

class GroupInput(graphene.InputObjectType):
    name = graphene.String()
    type = graphene.String()

class AddPerson(graphene.Mutation):
    class Arguments:
        person_data = PersonInput(required=True)

    person = graphene.Field(Person)

    def mutate(self, info, **kwargs):
        pdata = kwargs["person_data"]
        pdata["fullname"] = f'{pdata["fname"]} {pdata["lname"]}'
        person = PersonModel(**pdata).save()
        return AddPerson(person=person)

class AddUser(graphene.Mutation):
    class Arguments:
        person_data = PersonInput(required=True)
        groups = graphene.List(GroupInput, default_value=[])
        logged_in = graphene.Boolean()
        user_type = graphene.String()

    user = graphene.Field(User)

    def mutate(self, info, **kwargs):
        pdata = kwargs["person_data"]
        user = UserModel(groups=kwargs["groups"], logged_in=kwargs["logged_in"], user_type=kwargs["user_type"], **pdata).save()
        return AddUser(user)

class AddGroup(graphene.Mutation):
    class Arguments:
        group_data = GroupInput(required=True)

    group = graphene.Field(Group)

    def mutate(self, info, **kwargs):
        gdata = kwargs["group_data"]
        group = GroupModel(**gdata).save()
        return AddGroup(group)

class RemoveUser(graphene.Mutation):
    class Arguments:
        uid = graphene.Int(required=True)

    success = graphene.Boolean()

    def mutate(self, info, **kwargs):
        UserModel.objects(uid=kwargs["uid"]).remove()
        return RemoveUser(success=True)

