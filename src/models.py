import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Enum, UniqueConstraint
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(30), nullable=False)
    firstname = Column(String(30), nullable=False)
    lastname = Column(String(30), nullable=False)
    email = Column(String(50), nullable=False)

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    post_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

class Follower(Base):
    __tablename__ = 'follower'
    id = Column(Integer, primary_key=True)
    user_from_id = Column(Integer, ForeignKey('user.id'))
    user_to_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    commentText = Column(String(100))
    author_id = Column(Integer, ForeignKey('user.id'))
    post_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

class Media(Base):
    __tablename__ = 'media'
    id = Column(Integer, primary_key=True)
    typemedia = Column(Enum('video', 'foto'))
    url = Column(String(50))
    post_id = Column(Integer, nullable=False)
    post_id = Column(Integer, ForeignKey('user.id'))
    post = relationship(Post)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')