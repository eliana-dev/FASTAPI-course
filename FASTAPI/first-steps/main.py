from fastapi import FastAPI, Query, HTTPException
from typing import Optional, List, Union
from pydantic import BaseModel, Field, field_validator, EmailStr
import uvicorn

app = FastAPI(title="Mini Blog")

BLOG_POST = [
    {
        "id": 1,
        "title": "Hola desde FastAPI",
        "content": "Mi primer post con fastAPI",
    },
    {
        "id": 2,
        "title": "Me gusta el chocolate",
        "content": "Mi segundo post con fastAPI",
    },
    {
        "id": 3,
        "title": "Holiwis yeii",
        "content": "Mi tercer post con fastAPI",
    },
]


class Tag(BaseModel):
    name: str = Field(
        ...,
        min_length=2,
        max_length=30,
        description="Nombre de la etiqueta",
    )


class Author(BaseModel):
    name: str = Field(
        ..., min_length=2, max_length=30, description="Nombre del autor del post"
    )
    email: EmailStr = Field(..., description="Email del autor del post")


BAD_WORDS = ["porn", "xxx", "tits", "boobs", "dick", "cock", "pussy", "coochie"]


class PostBase(BaseModel):
    title: str
    content: str
    tags: Optional[List[Tag]] = []
    author: Optional[Author] = None


class PostCreate(BaseModel):
    title: str = Field(
        ...,
        min_length=3,
        max_length=100,
        description="Titulo del post (min 3 caracteres y max 100 caracteres)",
        examples=["Mi primer post con FastAPI"],
    )  # elipsis = espera contenido
    content: Optional[str] = Field(
        default="Contenido no disponible",
        min_length=10,
        description="Contenido del Post",
        examples=["Este es un contenido valido por que tiene 10 caracteres o más"],
    )
    tags: List[Tag] = []
    author: Optional[Author] = None
    
    @field_validator("title")  # evalua el campo titulo
    @classmethod  # ocupa la clase (nombre del modelo, manipula el valor a nivel clase)
    def not_allowed_title(cls, value: str) -> str:
        for word in BAD_WORDS:
            if word in value.lower():
                raise ValueError(f"El titulo no puede contener la palabra: {word}")
        return value
        # if "spam" in value.lower():
        #     raise ValueError("El titulo no puede contener la palabra: spam")
        # return value


class PostUpdate(BaseModel):
    title: str
    content: Optional[str] = None


class PostPublic(PostBase):  # hereda title y content
    id: int


class PostSummary(BaseModel):
    id: int
    title: str


@app.get("/")
def home():
    return {"message": "Bienvenidos a mini blog!"}


@app.get(
    "/posts", response_model=List[PostPublic]
)  # una lista de muchos postPublic es la response
def list_posts(
    query: Optional[str] = Query(
        default=None, description="texto para buscar por titulo"
    ),
):
    if query:
        results = [post for post in BLOG_POST if query.lower() in post["title"].lower()]
        return results  # devuelve una List
    return BLOG_POST  # Aca tambien


@app.get(
    "/posts/{post_id}",
    response_model=Union[PostPublic, PostSummary],
    response_description="Post Encontrado",
)  # evalua ambos modelos con Union, para elegir el modelo de respuesta
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
            return post

    return HTTPException(status_code=404, detail="Post no encontrado")


@app.post("/posts", response_model=PostPublic, response_description="Post Creado(OK)")
def create_post(post: PostCreate):
    new_id = (BLOG_POST[-1]["id"] + 1) if BLOG_POST else 1
    new_post = {
        "id": new_id,
        "title": post.title,
        "content": post.content,
        "tags": [tag.model_dump() for tag in post.tags],
        "author": post.author.model_dump() if post.author else None,
    }
    BLOG_POST.append(new_post)
    return new_post


@app.put(
    "/posts/{post_id}",
    response_model=PostPublic,
    response_description="Post actualizado",
    response_model_exclude_none=True,
)
def update_post(post_id: int, data: PostUpdate):
    for post in BLOG_POST:
        if post["id"] == post_id:
            playload = data.model_dump(
                exclude_unset=True,
            )  # convierte a dict y excluye lo que no pones!(en vez de poner None)
            if "title" in playload:
                post["title"] = playload["title"]
            if "content" in playload:
                post["content"] = playload["content"]
            return post

    raise HTTPException(status_code=404, detail="Post no encontrado")


@app.delete("/posts/{post_id}", status_code=204)
def delete_post(post_id: int):
    for index, post in enumerate(BLOG_POST):
        if post["id"] == post_id:
            BLOG_POST.pop(index)
            return
    raise HTTPException(status_code=404, detail="Post no encontrado")


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

# clase autor, enlasarla con los post como los tags: autor = nombre y email
