from fastapi import FastAPI, Query
from typing import Optional

app = FastAPI(title="Mini Blog")

BLOG_POST = [
    {
        "id": 1,
        "title": "Hola desde FastAPI",
        "Content": "Mi primer post con fastAPI",
    },
    {
        "id": 2,
        "title": "Me gusta el chocolate",
        "Content": "Mi segundo post con fastAPI",
    },
    {
        "id": 3,
        "title": "Holiwis yeii",
        "Content": "Mi tercer post con fastAPI",
    },
]


@app.get("/")
def home():
    return {"message": "Bienvenidos a mini blog!"}


@app.get("/posts")
def list_posts(
    query: Optional[str] = Query(  
        default=None, description="texto para buscar por titulo" ##Optional[str] == str | None
    ),
):  # la query debe de ser de tipo str o none
    if query:
        results = [post for post in BLOG_POST if query.lower() in post["title"].lower()]
        # for post in BLOG_POST:
        #     if query.lower() in post["title"].lower():
        #         results.append(post)
        return {"data": results, "query": query}
    return {"data": BLOG_POST}


# http://127.0.0.1:8000/posts?query=fastapi

# .\.venv\Scripts\activate.ps1 -> activa el .venv
# uv run uvicorn main:app --reload - inicia el servidor
#  fastapi dev main.py
# evita usar run
