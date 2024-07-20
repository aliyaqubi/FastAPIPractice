from router.blog_post import required_functionality
from typing import Optional
from fastapi import APIRouter, status, Response, Depends
from enum import Enum


router = APIRouter(
    prefix = '/blog',
    tags = ['blog']
)

#@router.get('/all')
#def get_all_blog():
#    return {'message':'All blog provides'}


@router.get(
        '/all',
        summary = 'Retrieve all blogs',
        description = 'This api call simulates fetching all blogs',
        response_description='The list of avilable blogs'
        )
def get_all_blog(page=1, 
                 page_size: Optional[int] = None, 
                 req_parameter: dict = Depends(required_functionality)
                 ):
    return {'message': f'All {page_size} blogs on page {page}', 'req': req_parameter}


@router.get(
        '/{id}/comments/{comment_id}',
        tags = ['comment']
        )
def get_comment(
    id: int, comment_id: int, 
    valid: bool = True, 
    username: Optional[str] = None
    ):
    """
    Simulates retriving a comment of a blog

    - **id** mandetory path parameter
    - **valid** optional query parameter
    """
    return {'message': f'ID: {id}, Comments: {comment_id}, Valid: {valid}, Username: {username}'}


class BlogType(str, Enum):
    short = 'short'
    medium = 'medium'
    long = 'long'
@router.get('/type/{type}')
def get_blog_type(type: BlogType):
    return {'message': f'Blog type {type}'}


@router.get('/{id}', status_code = status.HTTP_200_OK)
def get_blog(id:int, response: Response):
    if id > 5:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {'error': f'Blog {id} not found'}
    elif id > 1 and id <= 5:
        response.status_code = status.HTTP_402_PAYMENT_REQUIRED
        return {'payment': f'Blog {id} requires payment'}
    else:
        response.status_code = status.HTTP_200_OK
        return {'message': f'Blog with ID {id}'}