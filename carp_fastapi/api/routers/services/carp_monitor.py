"""
Copyright 2018 Copenhagen Center for Health Technology (CACHET) at the Technical University of Denmark (DTU).

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the ”Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED ”AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""
from fastapi import APIRouter, Request

from carp import monitor_service as monitor
from carp_fastapi.resources import carp_environment as env

router = APIRouter()

"""
MONITOR :: GET
"""


@router.get('/status/info')
async def get_instance_info(request: Request):
    """
    Endpoint: [get_instance_info]
    :param request: The [request] header.
    :return: Overall instance information.
    """
    response = await monitor.get_monitor_info(env.BASE_URL["production"],
                                              access_token=request.headers['authorization'])
    return response


@router.get('/status/git')
async def get_git_info(request: Request):
    """
    Endpoint: [get_git_info]
    :param request: The [request] header.
    :return: The git commit information.
    """
    response = await monitor.get_git_info(env.BASE_URL["production"],
                                          access_token=request.headers['authorization'])
    return response


@router.get('/status/flyway')
async def get_flyway_info(request: Request):
    """
    Endpoint: [get_flyway_info]
    :param request: The [request] header.
    :return: The flyway information.
    """
    response = await monitor.get_flyway_info(env.BASE_URL["production"],
                                             access_token=request.headers['authorization'])
    return response


@router.get('/status/health')
async def get_health_info(request: Request):
    """
    Endpoint: [get_health_info]
    :param request: The [request] header.
    :return: Only health information.
    """
    response = await monitor.get_health_info(env.BASE_URL["production"],
                                             access_token=request.headers['authorization'])
    return response


@router.get('/status/health/disk-space')
async def get_disk_space_info(request: Request):
    """
    Endpoint: [get_disk_space_info]
    :param request: The [request] header.
    :return: The only disk space information.
    """
    response = await monitor.get_disk_space_info(env.BASE_URL["production"],
                                                 access_token=request.headers['authorization'])
    return response


@router.get('/status/health/db')
async def get_db_info(request: Request):
    """
    Endpoint: [get_db_info]
    :param request: The [request] header.
    :return: The database information.
    """
    response = await monitor.get_health_db_info(env.BASE_URL["production"],
                                                access_token=request.headers['authorization'])
    return response


@router.get('/status/health/rabbitmq')
async def get_health_rabbitmq_info(request: Request):
    """
    Endpoint: [get_health_rabbitmq_info]
    :param request: The [request] header.
    :return: The rabbitmq information.
    """
    response = await monitor.get_health_rabbit_info(env.BASE_URL["production"],
                                                    access_token=request.headers['authorization'])
    return response


@router.get('/status/health/ping')
async def get_health_ping_info(request: Request):
    """
    Endpoint: [get_health_ping_info]
    :param request: The [request] header.
    :return: The ping health information.
    """
    response = await monitor.get_ping_info(env.BASE_URL["production"],
                                           access_token=request.headers['authorization'])
    return response


@router.get('/status/health/mail')
async def get_mail_server_info(request: Request):
    """
    Endpoint: [get_mail_server_info]
    :param request: The [request] header.
    :return: The mail server health information.
    """
    response = await monitor.get_mail_server_info(env.BASE_URL["production"],
                                                  access_token=request.headers['authorization'])
    return response
