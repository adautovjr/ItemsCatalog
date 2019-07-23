import os
import sys
import psycopg2
from psycopg2.extensions import AsIs
from sqlalchemy import create_engine
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy_utils import database_exists, create_database

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    picture = Column(String(250))
    categories = relationship('Category')
    items = relationship('Item')

    @property
    def serialize(self):
        
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'picture': self.picture
        }


class Category(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    name = Column(String(250), nullable=False)
    items = relationship('Item')

    @property
    def serialize(self):
        
        return {
            'id': self.id,
            'name': self.name
        }


class Item(Base):
    __tablename__ = 'items'

    name = Column(String(80), nullable=False)
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    category_id = Column(Integer, ForeignKey('categories.id'))
    category = relationship(Category)
    description = Column(String(250))

    @property
    def serialize(self):
        
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description
        }

# connection = psycopg2.connect(user = "postgres",
#                                 password = "123456",
#                                 host = "localhost",
#                                 port = "5432",
#                                 database = "catalog")

# try:

#     cur=connection.cursor()

#     cur.execute('CREATE ROLE root LOGIN ENCRYPTED PASSWORD \''+str(123456)+'\' SUPERUSER INHERIT NOCREATEDB NOCREATEROLE NOREPLICATION' )

# except (Exception, psycopg2.Error) as error :
#     print ("Error while connecting to PostgreSQL", error)
# finally:
#     #closing database connection.
#     if(connection):
#         cur.close()
#         connection.close()

engine = create_engine('postgresql://postgres:123456@localhost:5432/catalog')

if not database_exists(engine.url):
    create_database(engine.url)

Base.metadata.create_all(engine)
