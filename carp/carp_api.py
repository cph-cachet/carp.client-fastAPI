"""
Copyright 2018 Copenhagen Center for Health Technology (CACHET) at the Technical University of Denmark (DTU).

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the ”Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED ”AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

import requests
from requests.exceptions import ConnectionError
from requests.exceptions import HTTPError

from carp import carp_constants as const
import carp.carp_auth as auth
import carp.carp_utils as utils

"""
[CARP API] 
- The [carp_api.py] is used to handle the requests: |GET|POST|PUT|DELETE|.
"""


def url(environment, path):
    """
    Function: [url]
    :param path: The endpoint [path].
    :param environment: The environment [environment].
    :return: The environment path to forward the requests.
    """
    try:
        if utils.is_string_not_blank(environment):
            return ''.join([environment, const.SLASH, path])
    except ConnectionError as con_err:
        print(f'Connection error occurred: {con_err.response}')
        return None
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
        return None
    except Exception as err:
        print(f'Error occurred: {err}')
        return None


def delete(environment, path, access_token):
    """
    Function: [delete]
    :param access_token: The [access_token] used for login.
    :param path: The [files] to be deletes.
    :param environment: The environment [environment].
    :return: The delete source.
    """
    try:
        print(f'URL: {str(url(environment, path))}')
        response = requests.delete(url(environment, path), headers=build_access_token(access_token))
        response.raise_for_status()
    except ConnectionError as con_err:
        print(f'Connection error occurred: {con_err.response}')
        return None
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
        return None
    except Exception as err:
        print(f'Error occurred: {err}')
        return None
    else:
        return response


def post(environment, path, body, access_token, files=None):
    """
    Function: [post]
    :param path: The [path] endpoint request.
    :param body: The [body] object request.
    :param access_token: The [access_token] used for login.
    :param files: The [files] uploaded as multipart.
    :param environment: The environment [environment].
    :return: The response retrieved from the given parameters.
    """
    try:
        print(f'URL: {str(url(environment, path))}')
        response = requests.post(url(environment, path),
                                 files=files,
                                 json=body,
                                 headers=build_access_token(access_token))
        response.raise_for_status()
    except ConnectionError as con_err:
        print(f'Connection error occurred: {con_err.response}')
        return None
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
        return None
    except Exception as err:
        print(f'Error occurred: {err}')
        return None
    else:
        return response


def put(environment, path, body, access_token, files=None):
    """
    # Function: [put]
    :param path: The [path] endpoint request.
    :param body: The [body] object request.
    :param access_token: The [access_token] used for login.
    :param files: The existing [files] to update as multipart.
    :param environment: The environment [environment].
    :return: The response retrieved from the given parameters.
    """
    try:
        print(f'URL: {str(url(environment, path))}')
        response = requests.put(url(environment, path),
                                files=files,
                                json=body,
                                headers=build_access_token(access_token))
        response.raise_for_status()
    except ConnectionError as con_err:
        print(f'Connection error occurred: {con_err.response}')
        return None
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
        return None
    except Exception as err:
        print(f'Error occurred: {err}')
        return None
    else:
        return response.json()


# GET
def get(environment, path, access_token, stream=None):
    """
    Function: [get]
    :param stream: The [stream] for file reading.
    :param access_token: The [access_token] used for login.
    :param path: The [path] endpoint request.
    :param environment: The environment [environment].
    :return: json response / stream response
    """
    try:
        print(f'URL: {str(url(environment, path))}')
        response = requests.get(url(environment, path), headers=build_access_token(access_token))
        response.raise_for_status()
    except ConnectionError as con_err:
        print(f'Connection error occurred: {con_err.response}')
        return False
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
        return False
    except Exception as err:
        print(f'Error occurred: {err}')
        return False
    else:
        if stream:
            print(f'SUCCESS: {str(response.status_code)}.')
        else:
            return response.json()


"""
AUTHENTICATION
"""


def build_access_token(access_token):
    """
    Function: `build_access_token`
    :param access_token: The [access_token] used for login.
    :return: The authorization access token.
    """
    return {'Authorization': '' + access_token}


def build_refresh_token(refresh_token):
    """
    Function: `build_refresh_token`
    :param refresh_token: The [refresh_token] used for login.
    :return: The authorization refresh token.
    """
    return {'Authorization': '' + refresh_token}


def get_tokens(environment, token):
    """
    Function: [get_tokens]
    :param token: The access tokens (i.e., access-, refresh, and jti tokens)
    :param environment: The environment [environment].
    :return: The authentication tokens.
    """
    return auth.get_tokens(environment, token)


def get_refresh_token(environment, refresh_token):
    """
    Function: [get_refresh_token]
    :param refresh_token: The [refresh_token].
    :param environment: The environment [environment].
    :return: The new refresh token.
    """
    refresh_token = auth.get_refresh_token(environment, refresh_token)
    if utils.is_string_not_blank(refresh_token):
        return {'Authorization': 'Bearer ' + refresh_token}
    return ''
