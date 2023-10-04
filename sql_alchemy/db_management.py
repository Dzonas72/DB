from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sql_alchemy.models import Projektas


engine = create_engine('sqlite:///projektai.db')
Session = sessionmaker(bind=engine)
session = Session()


class DbManagement:
    def __init__(self):
        self.session = session

# Crud
    def add_value(self, projektas: Projektas):
        self.session.add(projektas)
        self.session.commit()

# add full projects
#     def add_values(self, projektas:list):
#         session.add_all(projects)
#         session.commit()


# cRud
    def get_value_by_id(self, id):
        value = session.query(Projektas).get(id)
        return (value)

    def filter_by_name(self,name):
        return session.query(Projektas).filter_by(name=name).all()


# crUd
    def update_value(self, id, new_name):
        value = session.query(Projektas).get(id)
        value.name = new_name
        session.commit()


    def delete_value(self, id):
        value = session.query(Projektas).get(id)
        session.delete(value)
        session.commit()


