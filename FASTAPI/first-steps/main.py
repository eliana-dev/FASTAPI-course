from fastapi import FastAPI

app = FastAPI(title="Mini Blog")

@app.get("/")
def home():
    return {'message': 'Bienvenidos a mini blog!'}

#  fastapi dev main.py
#evita usar run  