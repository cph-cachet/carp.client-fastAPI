"""
Copyright 2018 Copenhagen Center for Health Technology (CACHET) at the Technical University of Denmark (DTU).

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the ”Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED ”AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

from fastapi import APIRouter, Request

from carp import account_service as account
from carp_fastapi.resources import carp_environment as env

router = APIRouter()


@router.post("/{role}")
async def invite_account(request: Request, role_param: str):
    """
    Endpoint: [invite_account]
    :param request: The [request] body.
    :param role_param: The role to assign the account.
        i.e. roles: PARTICIPANT, STUDY_OWNER
    :return: This request doesn't return a response body.
    """
    body: bytes = await request.body()
    request_body: str = bytes.decode(body)
    access_token = request.headers['authorization']
    response = await account.invite_user(env.BASE_URL["production"],
                                         access_token=access_token,
                                         email_address=request_body,
                                         role=role_param)
    return response


@router.post("/unlock")
async def unlock_account(request: Request):
    """
    Endpoint: [unlock_account]
    :param request: The [request] body.
    :return: This request doesn't return a response request_body.
    """
    body: bytes = await request.body()
    request_body: str = bytes.decode(body)
    access_token = request.headers['authorization']
    response = await account.unlock_account(env.BASE_URL["production"],
                                            access_token=access_token,
                                            email_body=request_body)
    return response


@router.put("/{account_id}/study-manager")
async def get_studies_for_researcher_accounts(request: Request, account_id: str):
    """
    Endpoint: [get_studies_for_researcher_accounts]
    :param account_id: The [account_id].
    :param request: The [request] body.
    @param: The existing [account_id] of the researcher.
    :return: This request doesn't return a response request_body.
    """
    access_token = request.headers['authorization']
    response = await account.get_studies_for_researcher(env.BASE_URL["production"],
                                                        access_token=access_token,
                                                        account_id=account_id)
    return response
