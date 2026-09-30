from fastapi import FastAPI
from . import models
from .database import engine
from .routers import post, user, auth, vote
from.config import settings
from fastapi.middleware.cors import CORSMiddleware

"""
Why we need it: It automatically checks your PostgreSQL database
 to see if the posts table exists.
 If it does not exist, SQLAlchemy automatically generates the 
 SQL to create it for you!
 """



#models.Base.metadata.create_all(bind=engine) # if we want to reliy on alembic we can comment this line 

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)

@app.get("/")
def root():
    return {"message": "Welcome to my API!!!!!"}



# @app.get("/headers")
# def get_headers(authorization: str=Header()):
#     #print(authorization)
#     return {"authorization": authorization}


#used for testing
# @app.get("/sqlalchemy")
# def test_posts(db: Session = Depends(get_db)):
#     posts = db.query(models.Post).all()

#     return {"data": posts}

