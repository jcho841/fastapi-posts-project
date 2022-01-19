from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from .config import settings

SQLALCHEMY_DATABASE_URL = f'postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}'

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# while loop so that if the connection to the database fails, it tries again until it does.  time function tells it to wait 2 sec before reconnecting
# connecting with raw sql and not sql alchemy
"""while True:
    try:
        conn = psycopg2.connect(
            host='localhost', database='fastapi', user='postgres', password='Oregonlive2', cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print('database connection was successful')
        break
    except Exception as error:
        print('connection to database failed')
        print('the error was: ', error)
        time.sleep(2)"""

'''# saving posts in memory
my_posts = [{"title": "title of post 1", "content": "content of posts 1", "id": 1}, {
    "title": "favorite foods", "content": "sushi is good", "id": 2}]


def find_post(id):
    for p in my_posts:
        if p["id"] == id:
            return p


def find_index_post(id):
    for i, p in enumerate(my_posts):
        if p['id'] == id:
            return i'''

# app is the decorator, get is the http request and "/" is the root of the url or path

# test request for dependencies
# @app.get("/sqlalchemy")
# def test_posts(db: Session = Depends(get_db)):
#    posts = db.query(models.Post).all()
#    return {"data": posts}

# raw SQL not with alchemy
#    cursor.execute("""SELECT * FROM posts""")
#    posts = cursor.fetchall()

# posts is a list of posts, but the response model is tailoring it to one post, so need List function

# payLoad: dict = Body(...) - inside parameters - extract all of the fields from the body, put it in a python dictionary and store it in a variable (payLoad)
# Post class validates the data its receiveing

# hardcode for posting in memory
#    post_dict = post.dict()
#    post_dict['id'] = randrange(0, 1000000)
#    my_posts.append(post_dict)

#    **post.dict() converts the model columns into the new post variable
#    new_post = models.Post(
#        title=post.title, content=post.content, published=post.published


# raw SQL using without alchemy
#    cursor.execute("""INSERT INTO posts (title, content, published) VALUES (%s, %s, %s) RETURNING * """,
#                   (post.title, post.content, post.published))
#    new_post = cursor.fetchone()
#    conn.commit()
# make sure to commit


# id is converted to string so need to convert back to int
# manipulate response if id is null so that front end knows what the error is
# SQL needs it to be a string, so id needs to change from int to string
# if error, (str(id),) comma needed


# raw sql without alchemy
# def get_post(id: int, response: Response):
#    cursor.execute("""SELECT * FROM posts WHERE id = %s """, (str(id)))
#    post = cursor.fetchone()

# find the index in the array that matches the delete request
#index = find_index_post(id)
# if they try to delete post that doesnt exist, raise exeption
# if index == None:
#    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                        detail=f"post with id: {id} does not exist")
# my_posts.pop(index)
# when deleting, you can't send any data out
# return Response(status_code=HTTP_204_NO_CONTENT)


# raw SQL without alchemy
#    cursor.execute(
#        """DELETE FROM posts WHERE id = %s RETURNING * """, (str(id),))
#    deleted_post = cursor.fetchone()
#    conn.commit()


# find the index in the array that matches the delete request
#index = find_index_post(id)
# if they try to delete post that doesnt exist, raise exeption
# if index == None:
#        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                        detail=f"post with id: {id} does not exist")
#post_dict = post.dict()
#post_dict['id'] = id
#my_posts[index] = post_dict
# return {"message": post_dict}


# raw sql without alchemy
#    cursor.execute("""UPDATE posts SET title = %s, content = %s, published = %s WHERE id = %s RETURNING * """,
#                   (post.title, post.content, post.published, str(id)))
#    updated_post = cursor.fetchone()
#    conn.commit()
