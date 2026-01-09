from database import engine
from models import Base
from etl_logic import *

def run_pipeline():

    #Eliminamos las tablas
    Base.metadata.drop_all(engine)

    #Crea las tablas necesarias
    Base.metadata.create_all(engine)


    #Extrae y procesa los usuarios
    df_users = get_transform_user_data()
    df_users.to_sql(name="users", con=engine, if_exists='append', index= False)


    #Extrae y procesa todos
    df_todos = get_transform_todo_data()
    df_todos.to_sql(name="todos", con=engine, if_exists='append', index= False)

    #Extrae y procesa los posts
    df_posts = get_transform_post_data()
    df_posts.to_sql(name="posts", con=engine, if_exists='append', index= False)

    #Extrae y procesa comments
    df_comments = get_transform_comment_data()
    df_comments.to_sql(name="comments", con=engine, if_exists='append', index= False)

    #Extrae y procesa albums
    df_albums = get_transform_album_data()
    df_albums.to_sql(name="albums", con=engine, if_exists='append', index= False)

    #Extrae y procesa albums
    df_photos = get_transform_photo_data()
    df_photos.to_sql(name="photos", con=engine, if_exists='append', index= False)


if __name__ == '__main__':
    run_pipeline()