"""
Copyright 2018 Copenhagen Center for Health Technology (CACHET) at the Technical University of Denmark (DTU).

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the ”Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED ”AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""
from fastapi import APIRouter, Request

from carp_fastapi.resources import carp_environment as env
from carp import account_service as accounts

from starlette.config import Config

config = Config(".env")
environment: str = config("ENVIRONMENT", default="local")

router = APIRouter()

"""
AUTHENTICATION | AUTHORIZATION
"""


@router.post("/token")
async def login(request: Request):
    """
    Endpoint: [login]
    :return: The access
    """
    body: bytes = await request.body()
    request_body: str = bytes.decode(body)
    response = await accounts.login(env.BASE_URL[environment], request=request_body)
    return response


@router.post("/refresh/token")
async def refresh_token(request: Request):
    """
    Endpoint: [refresh_token]
    :return: The refresh token.
    """
    body: bytes = await request.body()
    request_body: str = bytes.decode(body)
    response = await accounts.refresh_token(env.BASE_URL[environment], token=request_body)
    return response
