"""
Copyright 2018 Copenhagen Center for Health Technology (CACHET) at the Technical University of Denmark (DTU).

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the ”Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED ”AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

import json
import urllib
import urllib.parse
import requests
from carp import carp_constants as const, carp_api as api

"""
[CARP API]
 - The [auth.py] is used to handle Authentication.
"""


def get_tokens(environment, credentials):
    """
    Function: get the login information <access_token, refresh_token, jti, scope, expires_in, and token_type>
    :param credentials: The [credentials] object containing the credentials.
    :param environment: The [environment].
    :return: The login information.
    """
    # Request
    request_payload = json.loads(json.dumps(credentials))
    # Session
    session = requests.Session()
    session.auth = (request_payload["client_id"], request_payload["client_secret"])
    # Payload
    payload = {
        'client_id': request_payload["client_id"],
        'client_secret': request_payload["client_secret"],
        'grant_type': request_payload["grant_type"],
        'username': request_payload["username"],
        'password': request_payload["password"]
    }
    # Headers
    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    # Response
    response = session.post(api.url(environment, const.OAUTH_TOKEN),
                            data=urllib.parse.urlencode(payload),
                            headers=headers)
    return response.json()


def get_refresh_token(environment, request):
    """
    Function: get a new refresh token
    :param request: The [request] object used to retrieve new refresh token.
    :param environment: The [environment].
    :return: The newly retrieved refresh token
    """
    # Request
    request_payload = json.loads(json.dumps(request))
    # Session
    session = requests.Session()
    session.auth = (request_payload["client_id"], request_payload["client_secret"])
    # Payload
    payload = {
        'client_id': request_payload["client_id"],
        'client_secret': request_payload["client_secret"],
        'grant_type': request_payload["grant_type"],
        'refresh_token': request_payload["refresh_token"]
    }
    # Headers
    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    # Response
    response = session.post(api.url(environment, const.OAUTH_TOKEN),
                            data=urllib.parse.urlencode(payload),
                            headers=headers)

    if response.status_code == 200:
        return response.json()['refresh_token']
    return ''
