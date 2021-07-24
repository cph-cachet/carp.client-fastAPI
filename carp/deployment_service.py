"""
Copyright 2018 Copenhagen Center for Health Technology (CACHET) at the Technical University of Denmark (DTU).

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the ”Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED ”AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""
from carp import carp_constants as const, carp_api as api

"""
[DEPLOYMENT]
 - The [deployment_service.py] is used to CREATE|UPDATE|GET|DELETE deployments in the CARP Platform.
"""


async def deployment_service(environment, access_token, deployment_body):
    """
    Function: [deployment_service]
    :param environment: The CARP [environment].
    :param deployment_body: The [deployment_body] to handle request.
    :param access_token: The [access_token] to grant request.
    :return: The deployment service response.
    """
    request = ''.join([const.DEPLOYMENTS_SERVICE])
    response = api.post(environment, request, deployment_body, access_token)
    return response


async def deployment_participation(environment, access_token, deployment_body):
    """
    Function: [deployment_participation]
    :param environment: The CARP [environment].
    :param deployment_body: The [deployment_body] to handle request.
    :param access_token: The [access_token] to grant request.
    :return: The deployment participation response.
    """
    request = ''.join([const.DEPLOYMENTS_PARTICIPATION])
    response = api.post(environment, request, deployment_body, access_token)
    return response


async def deployment_statistics(environment, access_token, deployment_body):
    """
    Function: [deployment_statistics]
    :param environment: The CARP [environment].
    :param access_token: The [access_token] to grant request.
    :param deployment_body: The [deployment_body] to handle request.
    :return: The deployment participation response.
    """
    request = ''.join([const.DEPLOYMENTS_STATISTICS])
    response = api.post(environment, request, deployment_body, access_token)
    return response
