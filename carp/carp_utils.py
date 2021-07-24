"""
Copyright 2018 Copenhagen Center for Health Technology (CACHET) at the Technical University of Denmark (DTU).

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the ”Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED ”AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

import re
from requests.exceptions import ConnectionError
from requests.exceptions import HTTPError

from pandas._libs import json

"""
EMAIL UTILS
"""


def is_valid_email(email):
    """
    Function: [is_valid_email]
    :param email: The [email] account.
    :return: [boolean] `true` if [email] is valid, `false` otherwise.
    """
    return bool(re.search(r"^[\w\.\+\-]+\@[\w]+\.[a-z]{2,3}$", email))


def validate_json_email(email):
    """
    Function: [validate_json_email]
    :param email: The [email] array.
    :return: [boolean] `true` if [email] is valid, `false` otherwise.
    """
    data = json.loads(json.dumps(email))
    return bool(re.search(r"^[\w\.\+\-]+\@[\w]+\.[a-z]{2,3}$", data["email"]))


"""
RESPONSE UTILS
"""


def is_response_blank(response):
    """
    Function: [is_response_blank]
    :param response: The [response] to check whether the response is blank.
    :return: [boolean] `true` if [response] is blank, `false` otherwise.
    """
    return bool(response and response.strip())


def is_response_not_blank(response):
    """
    Function: [is_response_not_blank]
    :param response: The [response] to check whether the response is empty.
    :return: [boolean] `true` if [response] is not blank, `false` otherwise.
    """
    return bool(response and response.strip())


def is_string_not_blank(value):
    """
    Function: [is_string_not_blank]
    :param value: The [value] to check whether is not blank.
    :return: [boolean] `true` if the string [value] is not empty, `false` otherwise.
    """
    return bool(len(value) != 0)


def url_email_encoded(value):
    """
    Function: [url_encode]
    :param value: The [value] to check
    :return: The encoded string value.
    """
    return value.replace("%40", "@")


"""
AUTH - USING CREDENTIALS
"""


def auth_credentials(request):
    """
    Function: [auth_credentials]
    :param request: The authentication [request].
    :return: The [authentication] access token built for [request].
    """
    try:
        for req in (request.split('&')):
            split_request = req.split('=')
            if split_request[0] == 'client_id':
                client_id = split_request[1]
            if split_request[0] == 'client_secret':
                client_secret = split_request[1]
            if split_request[0] == 'grant_type':
                grant_type = split_request[1]
            if split_request[0] == 'username':
                username = url_email_encoded(split_request[1])
            if split_request[0] == 'password':
                password = split_request[1]

        authentication = {"client_id": client_id,
                          "client_secret": client_secret,
                          "grant_type": grant_type,
                          "username": username,
                          "password": password}

    except ConnectionError as con_err:
        print(f'Connection error occurred: {con_err.response}')
        return False
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
        return False
    except Exception as err:
        print(f'Other error occurred: {err}')
        return False

    return authentication


"""
AUTH - USING ACCESS TOKEN
"""


def auth_access_token(request):
    """
    Function: [auth_access_token]
    :param request: The authentication [request].
    :return: The [authentication] access token built from [request].
    """
    try:
        for req in (request.split('&')):
            split_request = req.split('=')
            if split_request[0] == 'client_id':
                client_id = split_request[1]
            if split_request[0] == 'client_secret':
                client_secret = split_request[1]
            if split_request[0] == 'grant_type':
                grant_type = split_request[1]
            if split_request[0] == 'access_token':
                access_token = split_request[1]

        authentication = {"client_id": client_id,
                          "client_secret": client_secret,
                          "grant_type": grant_type,
                          "access_token": access_token}

    except ConnectionError as con_err:
        print(f'Connection error occurred: {con_err.response}')
        return False
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
        return False
    except Exception as err:
        print(f'Other error occurred: {err}')
        return False

    return authentication


"""
AUTH - USING REFRESH TOKEN
"""


def auth_refresh_token(request):
    """
    Function: [auth_refresh_token]
    :param request: The authentication [request].
    :return: The [authentication] refresh token built from [request].
    """
    try:
        for req in (request.split('&')):
            split_request = req.split('=')
            if split_request[0] == 'client_id':
                client_id = split_request[1]
            if split_request[0] == 'client_secret':
                client_secret = split_request[1]
            if split_request[0] == 'grant_type':
                grant_type = split_request[1]
            if split_request[0] == 'refresh_token':
                refresh_token = split_request[1]

        authentication = {"client_id": client_id,
                          "client_secret": client_secret,
                          "grant_type": grant_type,
                          "refresh_token": refresh_token}

    except ConnectionError as con_err:
        print(f'Connection error occurred: {con_err.response}')
        return False
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
        return False
    except Exception as err:
        print(f'Other error occurred: {err}')
        return False

    return authentication
