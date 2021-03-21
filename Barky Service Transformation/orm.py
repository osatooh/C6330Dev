import os
import sys
import DomainModel


from sqlalchemy import Table, MetaData, Column, Integer, String, Date, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from Barkyapp import db

# creating and instance of the declarative base
Base = declarative_base()
metadata = MetaData()

'''
unlike percival an Gregory. Barky only has one system a bookmark management system. It starts with a table 
and several CRUD activities performed on this table  or used to create this table 
# from sqlalchemy import Table, MetaData, Column, Integer, String, Date, ForeignKey
# Make the ORm dependent on the domain model 
# Table is defined using SQLAlchemy abstraction
#using the mapper function to bind the domain model classes to the table defined below
'''


# bookmark model 
Class bookmark(db.Model):
    tablename = 'Bookmarks'

    id = Column(Integer, primary_key=True, autoincrement=True),
    title = Column(String(255)),
    url = Column(Integer, nullable=False),
    notes = Column(String(255)
    data_added = Column(String(255))



  # define how to represent the tables when printed out
def __repr__(self):
    return "<tablename: {}>".format(self.tablename)
    

# persisting our table using the declarative base, using the metadata against the engine to create our table in memory 

