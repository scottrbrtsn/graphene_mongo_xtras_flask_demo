from sqlalchemy import *
from sqlalchemy.orm import (scoped_session, sessionmaker, relationship,
                            backref)
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///database.sqlite3', convert_unicode=True)
sql_db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))

Base = declarative_base()
# We will need this for querying
Base.query = sql_db_session.query_property()


class Department(Base):
    __tablename__ = 'department'
    id = Column(Integer, primary_key=True)
    name = Column(String)


class Employee(Base):
    __tablename__ = 'employee'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    hired_on = Column(DateTime, default=func.now())
    department_id = Column(Integer, ForeignKey('department.id'))
    department = relationship(
        Department,
        backref=backref('employees',
                        uselist=True,
                        cascade='delete,all'))


if __name__ == "__main__":
    ## You will want to initialize your database some how.. this is one way
    Base.metadata.create_all(bind=engine)
    # sql_db_session.create_all()
    # make a department for testing
    dep = Department(name="Data Science", id=1)
    # make an employee
    employee = Employee(id=1, name="Matt Camp", department_id=dep.id)
    # add the object to the database transaction
    sql_db_session.add(dep)
    print("add example department")
    sql_db_session.add(employee)
    print("add example employee")
    # commit ("Save/write") the transaction to the database
    sql_db_session.commit()
    print("commit")
    
    sql_db_session.close()
    print("close")
