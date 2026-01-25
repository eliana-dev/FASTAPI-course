from fastapi import FastAPI, Query, Body, HTTPException
from typing import Optional
from pydantic import BaseModel

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


class Post(BaseModel):
    title: str
    content: str


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


@app.post("/posts")
def create_post(post:Post):
    return {"data": post}# (...): obligatorio
    # if "title" not in post or "content" not in post:
    #     return {"error": "Title y Content son requeridos"}

    # if not str(post["title"]).strip():
    #     return {"error": "title no puede estar vacio"}

    # new_id = (BLOG_POST[-1]["id"] + 1) if BLOG_POST else 1
    # new_post = {"id": new_id, "title": post["title"], "content": post["content"]}
    # BLOG_POST.append(new_post)
    # return {"message": "Post creado", "data": new_post}


@app.put("/posts/{post_id}")
def update_post(post_id: int, data: dict = Body(...)):
    for post in BLOG_POST:
        if post["id"] == post_id:
            if "title" in data:
                post["title"] = data["title"]
            if "content" in data:
                post["content"] = data["content"]
            return {"message": "Post actualizado", "data": post}

        raise HTTPException(status_code=404, detail="Post no encontrado")


@app.delete("/posts/{post_id}", status_code=204)
def delete_post(post_id: int):
    for index, post in enumerate(BLOG_POST):
        if post["id"] == post_id:
            BLOG_POST.pop(index)
            return
    raise HTTPException(status_code=404, detail="Post no encontrado")


# .\.venv\Scripts\activate.ps1 -> activa el .venv
# uv run uvicorn main:app --reload - inicia el servidor
#  fastapi dev main.py
# evita usar run
# curl -X POST http://127.0.0.1:8000/posts -H "Content-Type: application/json" -d '{"title": "Nuevo post desde curl", "content": "Mi nuevo post desde curl"}'
