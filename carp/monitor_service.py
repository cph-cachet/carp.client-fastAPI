"""
Copyright 2018 Copenhagen Center for Health Technology (CACHET) at the Technical University of Denmark (DTU).

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the ”Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED ”AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

from carp import carp_constants as const, carp_api as api


async def get_monitor_info(environment, access_token):
    """
    Function: [get_monitor_info]
    :param environment: The CARP [environment].
    :param access_token: The [access_token].
    :return: The overall information.
    """
    request = ''.join([const.INFO])
    response = api.get(environment, request, access_token)
    return response


async def get_git_info(environment, access_token):
    """
    Function: [get_git_info]
    :param environment: The CARP [environment].
    :param access_token: The [access_token].
    :return: The GIT information.
    """
    request = ''.join([const.GIT_INFO])
    response = api.get(environment, request, access_token)
    return response


async def get_flyway_info(environment, access_token):
    """
    Function: [get_flyway_info]
    :param environment: The CARP [environment].
    :param access_token: The [access_token].
    :return: The flyway information.
    """
    request = ''.join([const.FLYWAY_INFO])
    response = api.get(environment, request, access_token)
    return response


async def get_health_info(environment, access_token):
    """
    Function: [get_health_info]
    :param environment: The CARP [environment].
    :param access_token: The [access_token].
    :return: The health information.
    """
    request = ''.join([const.HEALTH_INFO])
    response = api.get(environment, request, access_token)
    return response


async def get_disk_space_info(environment, access_token):
    """
    Function: [get_disk_space_info]
    :param environment: The CARP [environment].
    :param access_token: The [access_token].
    :return: The disk space information.
    """
    request = ''.join([const.HEALTH_DISK_SPACE])
    response = api.get(environment, request, access_token)
    return response


async def get_health_db_info(environment, access_token):
    """
    Function: [get_health_db_info]
    :param environment: The CARP [environment].
    :param access_token: The [access_token].
    :return: The health database info.
    """
    request = ''.join([const.HEALTH_DB])
    response = api.get(environment, request, access_token)
    return response


async def get_health_rabbit_info(environment, access_token):
    """
    Function: [get_health_rabbit_info]
    :param environment: The CARP [environment].
    :param access_token: The [access_token].
    :return: The health rabbit info.
    """
    request = ''.join([const.HEALTH_RABBIT])
    response = api.get(environment, request, access_token)
    return response


async def get_ping_info(environment, access_token):
    """
    Function: [get_health_rabbit_info]
    :param environment: The CARP [environment].
    :param access_token: The [access_token].
    :return: The ping information.
    """
    request = ''.join([const.HEALTH_PING])
    response = api.get(environment, request, access_token)
    return response


async def get_mail_server_info(environment, access_token):
    """
    Function: [get_mail_server_info]
    :param environment: The CARP [environment].
    :param access_token: The [access_token].
    :return: The mail server information.
    """
    request = ''.join([const.MAIL])
    response = api.get(environment, request, access_token)
    return response
