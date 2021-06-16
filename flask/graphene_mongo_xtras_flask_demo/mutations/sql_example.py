import graphene
from graphene import relay
from graphene_mongo_xtras_flask_demo.models.sql_models import ( 
        sql_db_session, 
        Department as DepartmentModel, 
        Employee as EmployeeModel
    )
from graphene_mongo_xtras_flask_demo.queries.sql_example import Employee, Department 

class AddEmployee(graphene.Mutation):

    class Arguments:
        name = graphene.String(required=True)
        department_id = graphene.Int(required=True)

    employee = graphene.Field(Employee)

    def mutate(self, info, **args):
        id = args.get('id')
        name = args.get('name')
        department_id = args.get('department_id')
        query = EmployeeModel(name=name, department_id=department_id)
        sql_db_session.add(query)
        sql_db_session.commit()
        return AddEmployee(person=query)

class AddDepartment(graphene.Mutation):

    class Arguments:
        name = graphene.String(required=True)

    department = graphene.Field(Department)
    
    def mutate(self, info, **args):
        name = args.get('name')
        query = DepartmentModel(name=name)
        sql_db_session.add(query)
        sql_db_session.commit()
        return AddDepartment(department=query)


class ChangeEmployeeName(graphene.Mutation):

    class Arguments:
        id = graphene.Int(required=True)
        name = graphene.String(required=True)

    employee = graphene.Field(Employee)

    def mutate(self, info, **args):
        id = args.get('id')
        name = args.get('name')
        query = EmployeeModel.get_query(context).filter_by(id=id)
        query.update(dict(name=name))
        return ChangeEmployeeName(employee=query)

