"""
Copyright 2018 Copenhagen Center for Health Technology (CACHET) at the Technical University of Denmark (DTU).

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the ”Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED ”AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""
from fastapi import APIRouter, Request
from carp import account_service as account
from carp_fastapi.resources import carp_environment as env

from starlette.config import Config
config = Config(".env")
environment: str = config("ENVIRONMENT", default="local")

router = APIRouter()

"""
USER
"""


@router.get("/current")
async def current_user(request: Request):
    """
    Endpoint: [get_current_user]
    :return: The current user account information.
    """
    access_token = request.headers['authorization']
    response = await account.current_user(env.BASE_URL[environment], access_token=access_token)
    return response


@router.post("/register")
async def register_user(request: Request):
    """
    Endpoint: [register_user]
    :param request: The [request] body.
    :return: The registered user.
    """
    body: bytes = await request.body()
    request_body: str = bytes.decode(body)
    access_token = request.headers['authorization']
    response = await account.register_user(env.BASE_URL[environment],
                                           access_token=access_token,
                                           user_body=request_body)
    return response


@router.post("/forgotten-password/send")
async def send_forgotten_password_email(request: Request):
    """
    Endpoint: [password_recovery]
    :param request: The [request] header.
    :return: This request doesn't return a response request_body.
    """
    body: bytes = await request.body()
    request_body: str = bytes.decode(body)
    access_token = request.headers['authorization']
    response = await account.send_forgotten_password(env.BASE_URL[environment],
                                                     access_token=access_token,
                                                     password_body=request_body)
    return response


@router.post("/forgotten-password/save")
async def send_new_password_for_token(request: Request):
    """
    Endpoint: [send_new_password_for_token]
    :param request: The [request] body.
    :return: This request doesn't return a response request_body.
    """
    body: bytes = await request.body()
    request_body: str = bytes.decode(body)
    access_token = request.headers['authorization']
    response = await account.send_new_password_for_token(env.BASE_URL[environment],
                                                         access_token=access_token,
                                                         password_body=request_body)
    return response


@router.put("/password")
async def change_password(request: Request):
    """
    Endpoint: [change_password]
    :param request: The [request] body.
    :return: This request doesn't return a response request_body.
    """
    body: bytes = await request.body()
    request_body: str = bytes.decode(body)
    access_token = request.headers['authorization']
    response = await account.change_password(env.BASE_URL[environment],
                                             access_token=access_token,
                                             password_body=request_body)
    return response
