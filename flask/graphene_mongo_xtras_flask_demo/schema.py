import graphene

from graphene_mongo import MongoengineConnectionField
from graphene.relay import Node

from graphene_mongo_xtras_flask_demo.queries.sql_example import *
from graphene_mongo_xtras_flask_demo.queries.mongo_example import *
from graphene_mongo_xtras_flask_demo.mutations.sql_example import *
from graphene_mongo_xtras_flask_demo.mutations.mongo_example import *
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField

from graphene_mongo_extras.filtering.fields import FilteringConnectionField

class Query(graphene.ObjectType):
    node = relay.Node.Field()
    # Allows sorting over multiple columns, by default over the primary key
    all_employees = SQLAlchemyConnectionField(Employee.connection)
    # Disable sorting over this field
    all_departments = SQLAlchemyConnectionField(Department.connection, sort=None)
    all_users = FilteringConnectionField(User)
    all_people = MongoengineConnectionField(Person)
    all_groups = MongoengineConnectionField(Group)


class Mutations(graphene.ObjectType):

    add_employee = AddEmployee.Field()
    add_department = AddDepartment.Field()
    add_user = AddUser.Field()
    add_person = AddPerson.Field()
    add_group = AddGroup.Field()
    


schema = graphene.Schema(query=Query, types=[User, Employee, Department, Person, Group], mutation=Mutations)
