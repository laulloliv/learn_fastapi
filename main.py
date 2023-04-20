from fastapi import FastAPI
from typing import Optional
import uvicorn
from schemas import Blog


app = FastAPI()


@app.get('/')
def index():
    return 'Hello'


@app.get('/blog')
def index(limit=10, published: bool = True, sort: Optional[str] = None):
    if published:
        return {'data': f'{limit} published blogs from the db'}
    else:
        return {'data': f'{limit} blogs from the db'}

@app.get('/blog/{id}')
def index(id):
    return f'ID: {id}'

@app.get('/comments')
def comments(limit):
    if limit == '10'        :
        return {'1','2','3','4','5','6','7','8','9','10','11','12'}
    else:
        return 'Menor'

@app.post('/blog')
def create_blog(request: Blog):
    return request


# if __name__ == "__main__":
#     uvicorn.run(app,host='127.0.0.1',port=9000)