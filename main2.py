from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def ind():
    return 'This is a Test'