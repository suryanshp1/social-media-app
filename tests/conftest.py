from fastapi.testclient import TestClient
from app import database
from app.main import app
from app.config import settings
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
# from alembic import command
import pytest
from app.oauth2 import create_access_token
from app import models


SQLALCHEMY_DATABASE_URL = f"postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}_test"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@pytest.fixture()
def session():
    print("My session fixtiire ran")
    database.Base.metadata.drop_all(bind=engine)
    database.Base.metadata.create_all(bind=engine)

    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

@pytest.fixture()
def client(session):
    def override_get_db():
        try:
            yield session
        finally:
            session.close()

    app.dependency_overrides[database.get_db] = override_get_db

    # command.upgrade("head")
    yield TestClient(app)
    # command.downgrade("base")


@pytest.fixture
def test_user(client):
    user_data = {"email": "xyz12@gmail.com", "password": "password"}
    res = client.post("/users/", json=user_data)

    assert res.status_code == 201
    new_user = res.json()
    new_user["password"] = user_data["password"]
    return new_user

@pytest.fixture
def test_user2(client):
    user_data = {"email": "xyz123@gmail.com", "password": "password"}
    res = client.post("/users/", json=user_data)

    assert res.status_code == 201
    new_user = res.json()
    new_user["password"] = user_data["password"]
    return new_user

@pytest.fixture
def token(test_user):
    return create_access_token({"user_id": test_user["id"]})

@pytest.fixture
def authorized_client(client, token):
    client.headers = {
        **client.headers,
        "Authorization": f"Bearer {token}"
    }

    return client


@pytest.fixture
def test_posts(test_user, session, test_user2):
    posts_data = [
        {
            "title": "first title",
            "content": "first content",
            "owner_id": test_user["id"]
        },
        {
            "title": "second title",
            "content": "second content",
            "owner_id": test_user["id"]
        },
        {
            "title": "third title",
            "content": "third content",
            "owner_id": test_user["id"]
        },
        {
            "title": "fourth title",
            "content": "fourth content",
            "owner_id": test_user2["id"]
        }
    ]

    def create_post_model(post):
        return models.Post(**post)

    post_map = map(create_post_model, posts_data)
    posts = list(post_map)

    session.add_all(posts)

    # session.add_all([models.Post(title="first title", content="first content", owner_id=test_user["id"]), models.Post(title="second title", content="second content", owner_id=test_user["id"]), models.Post(title="third title", content="third content", owner_id=test_user["id"])])

    session.commit()

    posts = session.query(models.Post).all()

    return posts