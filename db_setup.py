#!/usr/bin/env python2.7

import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    picture = Column(String(250))


class Category(Base):
    __tablename__ = 'category'

    name = Column(String(80), nullable=False)
    id = Column(Integer, primary_key=True)

    @property
    def serialize(self):
        return {
            'name': self.name,
            'id': self.id
        }


class Item(Base):
    __tablename__ = 'item'
    name = Column(String(80), nullable=False)
    id = Column(Integer, primary_key=True)
    description = Column(String(250))
    category_id = Column(Integer, ForeignKey('category.id'))
    category = relationship(Category)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    filename = Column(String(250))
    picture = Column(String(250)) 

    @property
    def serialize(self):
        return {
            'category_id': self.category_id,
            'name': self.name,
            'description': self.description,
            'id': self.id,
            'user_id': self.user_id,
            'filename': self.filename,
            'picture': self.picture
        }


engine = create_engine('sqlite:///catalog.db')
Base.metadata.create_all(engine)
