import os
from mongoengine import *
import bson

class Group(Document):
    meta = { 'collection' : 'Group' }
    name = StringField(primary_key=True)
    type = StringField()

class Person(Document):
    meta = { 'collection': 'Person', 'allow_inheritance': True }
    uid = IntField(required=True, primary_key=True)
    sid = StringField(unique=True, required=True)
    fullname = StringField()
    fname = StringField()
    lname = StringField()

class User(Person):
    group = StringField()
    logged_in = BooleanField()
    groups = ListField(StringField())
#    groups = ListField(ReferenceField('Group'))
    user_type = StringField()
