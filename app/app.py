from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
<<<<<<< HEAD
    return {"status": "healthy-v2"}
=======
    return {"status": "healthy"}
>>>>>>> 991618368070d0a36e5dadcddd0e81572c187222
    