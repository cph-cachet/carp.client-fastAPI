"""
Copyright 2018 Copenhagen Center for Health Technology (CACHET) at the Technical University of Denmark (DTU).

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the ”Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED ”AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""
from fastapi import APIRouter, Request

from carp import protocol_service as protocol
from carp_fastapi.resources import carp_environment as env

from starlette.config import Config
config = Config(".env")
environment: str = config("ENVIRONMENT", default="local")

router = APIRouter()

"""
PROTOCOLS :: CREATE :: GET
"""


@router.post('/protocol-service')
async def protocol_service(request: Request):
    """
    Endpoint: [protocol_service]
    :param request: The [request] body.
    :return: The protocol related response.
    """
    body: bytes = await request.body()
    request_body: str = bytes.decode(body)
    response = await protocol.protocol_service(env.BASE_URL[environment],
                                               access_token=request.headers['authorization'],
                                               protocol_body=request_body)
    return response


@router.post('/protocol-factory-service')
async def protocol_factory_service(request: Request):
    """
    Endpoint: [protocol_factory_service]
    :param request: The [request] body.
    :return: The protocol related response.
    """
    body: bytes = await request.body()
    request_body: str = bytes.decode(body)
    response = await protocol.protocol_factory_service(env.BASE_URL[environment],
                                                       access_token=request.headers['authorization'],
                                                       protocol_body=request_body)
    return response
