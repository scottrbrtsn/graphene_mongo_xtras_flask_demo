import graphene
from graphene import relay
from graphene_mongo_xtras_flask_demo.models.sql_models import sql_db_session, Department as DepartmentModel, Employee as EmployeeModel
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField

class Department(SQLAlchemyObjectType):
    class Meta:
        model = DepartmentModel
        interfaces = (relay.Node, )

class Employee(SQLAlchemyObjectType):
    class Meta:
        model = EmployeeModel
        interfaces = (relay.Node, )
