import commands
'''importing the abc module so we can delare the abstract method'''
from abc import ABC, abstractmethod
import model

'''
Refactored service layer serving as an abstraction between Flask and our domain model(business logic)
Introducing the parent abstract class defining several abstract methods
# implemetting methods to perform several CRUD activities to create, add, list, delete and update 
# can also be instantiated
'''
class AbstractRepository(abc.ABC):   #abstract class
    @abc.abstractmethod              #abstract method
    def create(self, data):
        raise NotImplementedError


    @abc.abstractmethod
    def add(self, data, timestamp=None):
        raise NotImplementedError

    @abc.abstractmethod
    def list(self, order_by=None):
        raise NotImplementedError
    
     @abc.abstractmethod
    def delete(self, id):
        raise NotImplementedError

    @abc.abstractmethod
    def edit(self, id, data):
        raise NotImplementedError

'''
Uses the Orm model 
'''
class SqlAlchemyRepository(AbstractRepository):
    def __init__(self, session):
        self.session = session
        self.table_name = 'bookmarks'

        self.session.create_table(self.table_name,{
            "id": "INTEGER PRIMARY KEY AUTOINCREMENT",
            "title": "TEXT NOT NULL",
            "url": "TEXT NOT NULL",
            "notes": "TEXT",
            "date_added": "TEXT NOT NULL"
        })

    def create(self, data):
        self.session.add(self.table_name,data)
       

    def list(self, order_by=None):
        return self.session.select(self.table_name, order_by=order_by).fetchall()

    def edit(self, id, data):
        self.session.update(self.table_name, {'id': id}, data)
     

    def delete(self):
       self.session.delete(self.table_name, {'id':id})
      