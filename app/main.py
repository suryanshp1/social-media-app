import logging
# import models
# import uvicorn
from fastapi import FastAPI
# from database import engine
from routers import post, user, auth, vote
from fastapi.middleware.cors import CORSMiddleware
# import config

logger = logging.getLogger("__name__")

# models.Base.metadata.create_all(bind=engine)

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
    return {"message": "Hello, Welcome !!"}


# if __name__ == "__main__":
#     uvicorn.run(app='test:app', reload=True, debug=True)

# 11:51:45