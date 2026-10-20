# FastAPI Social Media API

A REST API built with FastAPI and PostgreSQL where users can register, log in, create posts and vote on posts.

Built while following Python API Development - FreeCodeCamp to learn backend development with FastAPI.

## Features

- User registration with bcrypt-hashed passwords
- JWT login (OAuth2 password flow)
- Create, read, update and delete posts; only the owner can update or delete a post
- Vote on posts, with vote counts returned alongside each post
- Pagination and title search on the posts list
- Database migrations with Alembic

## Project Status

- **Tests:** Automated tests are not included yet and will be added in a future update.
- **Deployment:** The app is containerized with Docker and was deployed to AWS and Render as part of learning deployment.

## Tech Stack

Python, FastAPI, PostgreSQL, SQLAlchemy, Pydantic, Alembic, python-jose (JWT), passlib (bcrypt), Docker

## Project Structure

```
app/
├── main.py          # Creates the FastAPI app and registers routers
├── config.py        # Loads settings from environment variables
├── database.py      # Database engine and session setup
├── models.py        # SQLAlchemy models (tables)
├── schemas.py       # Pydantic schemas (request/response validation)
├── oauth2.py        # JWT creation and verification
├── utils.py         # Password hashing
└── routers/
    ├── auth.py      # Login
    ├── user.py      # User endpoints
    ├── post.py      # Post endpoints
    └── vote.py      # Vote endpoint
alembic/             # Database migrations
```
