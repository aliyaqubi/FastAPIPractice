from fastapi import FastAPI

app = FastAPI()

@app.get('/hello')
def index():
    return {'message': 'Hello world!'}

@app.get('/blog/(id)')
def get_blog(id):
    return {'message': f'Blog ID {id}'}