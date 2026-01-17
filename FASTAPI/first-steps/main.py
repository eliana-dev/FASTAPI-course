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
        default=None, description="texto para buscar por titulo"
    ),
):
    if query:
        results = [post for post in BLOG_POST if query.lower() in post["title"].lower()]
        return {"data": results, "query": query}
    return {"data": BLOG_POST}


@app.get("/posts/{post_id}")  ##query parameter: include_content=false
def get_post(
    post_id: int,
    include_content: Optional[bool] = Query(
        default=None, description="Bool para filtrar contenido"
    ),
):
    for post in BLOG_POST:
        if post["id"] == post_id:
            if not include_content:
                return {"id": post["id"], "title": post["title"]}
            return {"data": post}

    return {"error": "post no encontrado"}


# .\.venv\Scripts\activate.ps1 -> activa el .venv
# uv run uvicorn main:app --reload - inicia el servidor
#  fastapi dev main.py
# evita usar run
