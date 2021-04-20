import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Enum, UniqueConstraint
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class Follower(Base):
    __tablename__ = 'follower'
    id = Column(Integer, primary_key = True)
    user_from_id = Column(Integer, ForeignKey('user.id'))
    user_to_id = Column(String(50), ForeignKey('user.id'))
    user = relationship('User')

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key = True)
    username = Column(String(30), index = True, nullable = False)
    firstname = Column(String(30), nullable = False)
    lastname = Column(String(30), nullable = False)
    email = Column(String(150), unique = True, nullable = False)

class Post(Base):
    __tablename__ = 'post'
<<<<<<< HEAD
    id = Column(Integer, primary_key = True)
    user_id = Column(Integer, ForeignKey('user.id'))
=======
    id = Column(Integer, primary_key=True)
    post_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    comment = relationship(Comment)

class Follower(Base):
    __tablename__ = 'follower'
    id = Column(Integer, primary_key=True)
    user_from_id = Column(Integer, ForeignKey('user.id'))
    user_to_id = Column(Integer, ForeignKey('user.id'))
>>>>>>> ad2c86f2d2d28a35f9c6c741df17c4e3f53fe7c9
    user = relationship(User)

class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    commentText = Column(String(150), nullable = False)
    author_id = Column(Integer, ForeignKey('user.id'))
    post_id = Column(Integer, ForeignKey('post.id'))
    user = relationship('User')
    post = relationship('Post')

<<<<<<< HEAD
class Media(Base):
    __tablename__ = 'media'
    id = Column(Integer, primary_key = True)
    typemedia = Column(Enum('video', 'foto'), nullable = False)
    url = Column(String(250), nullable = False)
    post_id = Column(Integer, ForeignKey('post.user_id'))
    post = relationship('Post')

=======
>>>>>>> ad2c86f2d2d28a35f9c6c741df17c4e3f53fe7c9
    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')