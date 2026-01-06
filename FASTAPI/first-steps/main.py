from fastapi import FastAPI

app = FastAPI(title="Mini Blog")

BLOG_POST = [
    {"id": 1, "title": "Hola desde FastAPI", "Content": "Mi primer post con fastAPI"},
    {"id": 2, "title": "Me gusta el chocolate", "Content": "Mi segundo post con fastAPI"},
    {"id": 3, "title": "Holiwis yeii", "Content": "Mi tercer post con fastAPI"},
]
@app.get("/")
def home():
    return {'message': 'Bienvenidos a mini blog!'}

@app.get("/posts")
def list_posts():
    return {"data": BLOG_POST}


#  fastapi dev main.py
#evita usar run  
#uv run uvicorn main:app --reload
