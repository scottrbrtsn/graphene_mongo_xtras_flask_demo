import graphene as graphene

from graphene_mongo import MongoengineConnectionField

import graphene_mongo_xtras_flask_demo.queries.sql_example as sql_queries
import graphene_mongo_xtras_flask_demo.queries.mongo_example as mongo_queries
import graphene_mongo_xtras_flask_demo.mutations.sql_example as sql_mutations
import graphene_mongo_xtras_flask_demo.mutations.mongo_example as mongo_mutations
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField

from graphene_mongo_extras.filtering.fields import FilteringConnectionField

class Query(graphene.ObjectType):
    node =  graphene.relay.Node.Field()
    # Allows sorting over multiple columns, by default over the primary key
    all_employees = SQLAlchemyConnectionField(sql_queries.Employee.connection)
    # Disable sorting over this field
    all_departments = SQLAlchemyConnectionField(sql_queries.Department.connection, sort=None)
    all_users = FilteringConnectionField(mongo_queries.User)
    all_people = MongoengineConnectionField(mongo_queries.Person)
    all_groups = MongoengineConnectionField(mongo_queries.Group)


class Mutations(graphene.ObjectType):

    add_employee = sql_mutations.AddEmployee.Field()
    add_department = sql_mutations.AddDepartment.Field()
    add_user = mongo_mutations.AddUser.Field()
    add_person = mongo_mutations.AddPerson.Field()
    add_group = mongo_mutations.AddGroup.Field()


schema = graphene.Schema(query=Query,
        types=[
            mongo_queries.User,
            sql_queries.Employee,
            sql_queries.Department,
            mongo_queries.Person,
            mongo_queries.Group
            ],
        mutation=Mutations)
