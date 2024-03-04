from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/users")
async def get_users():
    return [
        {
            "firstName" : "Sora",
            "lastName" : "C",
            "email": "ss.best@outlook.com",
        }
    ]