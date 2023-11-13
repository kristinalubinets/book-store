from fastapi import FastAPI

app = FastAPI()

@app.get("/hello")
def read_root():
    return {"message": "Hello, World!!!!"}


@app.get("/menu")
def read_root():
    return {"message": "Check the MENU"}

@app.get("/exit")
def read_root():
    return {"message": "byee"}