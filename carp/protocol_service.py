"""
Copyright 2018 Copenhagen Center for Health Technology (CACHET) at the Technical University of Denmark (DTU).

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the ”Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED ”AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

from carp import carp_constants as const, carp_api as api

"""
[PROTOCOL]
 - The [protocol_service.py] is used to CREATE|UPDATE|GET| protocol in the CARP Platform.
"""


async def protocol_service(environment, access_token, protocol_body):
    """
    Function: [protocol_service]
    :param environment: The CARP [environment].
    :param access_token: The [access_token].
    :param protocol_body: The [protocol_body] to handle request.
    :return: The protocol service response.
    """
    request = ''.join([const.PROTOCOL_SERVICE])
    response = api.post(environment, request, protocol_body, access_token)
    return response


async def protocol_factory_service(environment, access_token, protocol_body):
    """
    Function: [protocol_factory_service]
    :param environment: The CARP [environment].
    :param access_token: The [access_token].
    :param protocol_body: The [protocol_body] to handle request.
    :return: The protocol factory service response.
    """
    request = ''.join([const.PROTOCOL_FACTORY_SERVICE])
    response = api.post(environment, request, protocol_body, access_token)
    return response

