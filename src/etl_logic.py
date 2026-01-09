import requests
import pandas as pd
import logging

logging.basicConfig(level=logging.INFO)

url = 'https://jsonplaceholder.typicode.com'

def get_transform_user_data() -> pd.DataFrame:
  try:
    response = requests.get(f"{url}/users", timeout=100) #Lee la API usuarios
    response.raise_for_status() #Termina si hay un mal request
    raw_users = pd.json_normalize(response.json(), sep='_') #Crea la DF sucia con campos json normalizamos
    df_users = raw_users[['id','name','username','email','address_street','address_city','phone','website']] #Extrae la informacion necesaria
    return df_users
  except requests.exceptions.RequestException as e:
    logging.error(f'Error de conectar a la red o API {e}')

def get_transform_todo_data() -> pd.DataFrame:
  try:
    response = requests.get(f"{url}/todos",timeout=100)
    response.raise_for_status()
    raw_todos = pd.json_normalize(response.json(), sep='_')
    df_todos = raw_todos[['id','userId','title','completed']].rename(columns={
        'userId': 'user_id'
    })
    return df_todos
  except requests.exceptions.RequestException as e:
    logging.error(f'Error de conectar a la red o API {e}')

def get_transform_post_data() -> pd.DataFrame:
  try:
    response = requests.get(f"{url}/posts",timeout=100)
    response.raise_for_status()
    raw_posts = pd.json_normalize(response.json(), sep='_')
    df_posts = raw_posts[['id','userId','title','body']].rename(columns={
        'userId': 'user_id'
    })
    return df_posts
  except requests.exceptions.RequestException as e:
    logging.error(f'Error de conectar a la red o API {e}')

def get_transform_comment_data() -> pd.DataFrame:
  try:
    response = requests.get(f"{url}/comments",timeout=100)
    response.raise_for_status()
    raw_comments = pd.json_normalize(response.json(), sep='_')
    df_comments = raw_comments[['id','postId','name','body']].rename(columns={
        'postId': 'post_id'
    })
    return df_comments
  except requests.exceptions.RequestException as e:
    logging.error(f'Error de conectar a la red o API {e}')

def get_transform_album_data() -> pd.DataFrame:
  try:
    response = requests.get(f"{url}/albums",timeout=100)
    response.raise_for_status()
    raw_albums = pd.json_normalize(response.json(), sep='_')
    df_comments = raw_albums[['id','userId','title']].rename(columns={
        'userId': 'user_id'
    })
    return df_comments
  except requests.exceptions.RequestException as e:
    logging.error(f'Error de conectar a la red o API {e}')

def get_transform_photo_data() -> pd.DataFrame:
  try:
    response = requests.get(f"{url}/photos",timeout=100)
    response.raise_for_status()
    raw_photos = pd.json_normalize(response.json(), sep='_')
    df_photos = raw_photos[['id','albumId','title','url','thumbnailUrl']].rename(columns={
        'albumId': 'album_id',
        'thumbnailUrl': 'thumbnail_url'
    })
    return df_photos
  except requests.exceptions.RequestException as e:
    logging.error(f'Error de conectar a la red o API {e}')
