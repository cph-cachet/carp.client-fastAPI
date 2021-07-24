"""
Copyright 2018 Copenhagen Center for Health Technology (CACHET) at the Technical University of Denmark (DTU).

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the ”Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED ”AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""
import carp.carp_utils as utils
from carp import carp_constants as const, carp_api as api

"""
[ACCOUNT]
 - The [account_service.py] is used to login, register, and invite users in the CARP Platform.
"""


async def login(environment, request):
    """
    Function: [login]
    :param environment: The CARP [environment].
    :param request: The user [request] sets the user credentials.
    :return: The access tokens.
    """
    authentication = utils.auth_credentials(request)
    response = api.get_tokens(environment, authentication)
    return response


async def refresh_token(environment, token):
    """
    Function: [refresh_token]
    :param token: The [token] parameter required to build request.
    :param environment: The CARP [environment].
    :return: The newly retrieved refresh token.
    """
    auth_request = utils.auth_refresh_token(token)
    response = api.get_refresh_token(environment, auth_request)
    return response


async def current_user(environment, access_token):
    """
    Function: [current_user]
    :param access_token: The [access_token] used for login.
    :param environment: The CARP [environment].
    :return: The user role and related information in CARP.
    """
    response = api.get(environment, const.CURRENT_USER, access_token)
    return response


async def register_user(environment, access_token, user_body):
    """
    Function: [register_user]
    :param environment: The CARP [environment].
    :param user_body: The [user_body] object to register the user.
    :param access_token: The [access_token] used for login.
    :return: The registered user.
    """
    response = api.post(environment, const.REGISTER_USER, user_body, access_token)
    return response


async def invite_user(environment, access_token, email_address, role):
    """
    Function: [invite_user]
    :param environment: The CARP [environment].
    :param access_token: The access [token] used for login.
    :param email_address: The invitation [email_address] of the user.
    :param role: The account [role]
           - roles: [PARTICIPANT|STUDY_OWNER|CARP_ADMINISTRATOR|SYSTEM_ADMINISTRATOR|]
    :return: The invited user by [email_address].
    """
    if 'PARTICIPANT' == role:
        response = api.post(environment, const.PARTICIPANT, email_address, access_token)
        print(f'Participant invited: {response}')
        return "Invitation email: " + email_address + " with the role " + role + " has been sent."
    elif 'STUDY_OWNER' == role:
        response = api.post(environment, const.STUDY_OWNER, email_address, access_token)
        print(f'Study Owner invited: {response}')
        return "Invitation email: " + email_address + " with the role " + role + " has been sent."
    elif 'CARP_ADMINISTRATOR' == role:
        response = api.post(environment, const.CARP_ADMINISTRATOR, email_address, access_token)
        print(f'CARP Admin invited: {response}')
        return "Invitation email: " + email_address + " with the role " + role + " has been sent."
    elif 'SYSTEM_ADMINISTRATOR' == role:
        response = api.post(environment, const.SYSTEM_ADMINISTRATOR, email_address, access_token)
        print(f'System Admin invited: {response}')
        return "Invitation email: " + email_address + " with the role " + role + " has been sent."
    else:
        return False


async def send_forgotten_password(environment, access_token, password_body):
    """
    Function: [send_forgotten_password]
    :param environment: The CARP [environment].
    :param password_body: The [password_body] object to recover the password.
    :param access_token: The [access_token] used for login.
    :return: The password recovery response.
    """
    response = api.post(environment, const.FORGOTTEN_PASSWORD, password_body, access_token)
    if not response:
        return response
    return "Recovery e-mail has been sent."


async def send_new_password_for_token(environment, access_token, password_body):
    """
    Function: [send_new_password_for_token]
    :param environment: The CARP [environment].
    :param access_token: The [access_token] used for login.
    :param password_body: The [password_body].
    :return: The password with the given token sent.
    """
    response = api.post(environment, const.SEND_PASSWORD, password_body, access_token)
    if not response:
        return response
    return "New password has been sent!"


async def unlock_account(environment, access_token, email_body):
    """
    Function: [unlock_account]
    :param environment: The CARP [environment].
    :param access_token: The [access_token] used for login.
    :param email_body: The [email_body].
    :return: The unlocked account.
    """
    response = api.post(environment, const.UNLOCK_ACCOUNT, email_body, access_token)
    if not response:
        return response
    return "Unlock email has been sent!"


async def change_password(environment, access_token, password_body):
    """
    Function: [change_password]
    :param environment: The CARP [environment].
    :param access_token: The [access_token] used for login.
    :param password_body: The [password_body] body.
    :return: The changed password.
    """
    response = api.put(environment, const.CHANGE_PASSWORD, password_body, access_token)
    if not response:
        return response
    return "Unlock email has been sent!"


async def get_studies_for_researcher(environment, access_token, account_id):
    """
    Function: [get_studies_for_researcher]
    :param environment: The CARP [environment].
    :param account_id: The researcher [account_id].
    :param access_token: The [access_token] used for login.
    :return: The studies for the given [account_id].
    """
    request = ''.join([const.RESEARCHER_ACCOUNT, const.ACCOUNTS, const.SLASH, str(account_id), const.SLASH, const.STUDY_MANAGER])
    response = api.get(environment, request, access_token)
    return response
