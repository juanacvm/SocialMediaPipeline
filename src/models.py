from sqlalchemy import create_engine, Column, ForeignKey 
from sqlalchemy.types import Integer, Boolean, String, NVARCHAR 
from sqlalchemy.orm import declarative_base 

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=False)
    name = Column(NVARCHAR(100))
    username = Column(NVARCHAR(50))
    email = Column(NVARCHAR(70))
    address_street = Column(NVARCHAR(100))
    address_city = Column(NVARCHAR(50))
    phone = Column(NVARCHAR(50))
    website = Column(NVARCHAR(60))

class Todo(Base):
    __tablename__ = 'todos'

    id = Column(Integer, primary_key=True, autoincrement=False)
    user_id = Column(Integer, ForeignKey('users.id', name='fk_todo_userid'))
    title = Column(NVARCHAR(250), nullable=False)
    completed = Column(Boolean, nullable=False)
    
class Post(Base):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True, autoincrement=False)
    user_id = Column(Integer, ForeignKey('users.id', name='fk_post_userid'))
    title = Column(NVARCHAR(150), nullable=False)
    body = Column(NVARCHAR(250), nullable=False)

class Comment(Base):
    __tablename__ = 'comments'

    id = Column(Integer, primary_key=True, autoincrement=False)
    post_id = Column(Integer, ForeignKey('posts.id', name='fk_comments_postid'))
    name = Column(NVARCHAR(150), nullable=False)
    body = Column(String, nullable=False)

class Album(Base):
    __tablename__ = 'albums'

    id = Column(Integer, primary_key=True, autoincrement=False)
    user_id = Column(Integer, ForeignKey('users.id', name='fk_albums_userid'))
    title = Column(NVARCHAR(150), nullable=False)

class Photo(Base):
    __tablename__ = 'photos'
    id = Column(Integer, primary_key=True, autoincrement=False)
    album_id = Column(Integer, ForeignKey('albums.id', name='fk_album_albumid'))
    title = Column(NVARCHAR(150), nullable=False)
    url = Column(String, nullable = True)
    thumbnail_url = Column(String, nullable = True)
