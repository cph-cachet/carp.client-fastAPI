"""
Copyright 2018 Copenhagen Center for Health Technology (CACHET) at the Technical University of Denmark (DTU).

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the ”Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED ”AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

from carp import carp_constants as const, carp_api as api

"""
[CONSENT]
 - The [consent_service.py] is used to CREATE|GET|DELETE consents documents in the CARP Platform.
"""


async def create_consent(environment, access_token, deployment_id, consent_body):
    """
    Function: [create_consent]
    :param environment: The CARP [environment].
    :param access_token: The [access_token].
    :param consent_body: The [consent_body] information and terms.
    :param deployment_id: The [deployment_id].
    :return: The consents document created.
    """
    request = ''.join([const.CONSENT, str(deployment_id), const.CONSENT_DOCUMENTS])
    response = api.post(environment, request, consent_body, access_token)
    return response


async def get_consent_document(environment, access_token, deployment_id, consent_id):
    """
    Function: [get_consent_document]
    :param environment: The CARP [environment].
    :param access_token: The [access_token].
    :param deployment_id: The [deployment_id].
    :param consent_id: The [consent_id].
    :return: The consents document by [deployment_id & consent_id].
    """
    request = ''.join([const.CONSENT, str(deployment_id), const.CONSENT_ID, str(consent_id)])
    response = api.get(environment, request, access_token)
    return response


async def get_all_consent_documents(environment, access_token, deployment_id):
    """
    Function: [get_all_consent_documents]
    :param environment: The CARP [environment].
    :param access_token: The [access_token].
    :param deployment_id: The [deployment_id].
    :return: Lists all consents documents by [deployment_id].
    """
    request = ''.join([const.CONSENT, str(deployment_id), const.CONSENT_DOCUMENTS])
    response = api.get(environment, request, access_token)
    return response


async def delete_consent(environment, access_token, deployment_id, consent_id):
    """
    Function: [delete_consent]
    :param environment: The CARP [environment].
    :param access_token: The [access_token].
    :param deployment_id: The [deployment_id].
    :param consent_id: The [consent_id].
    :return: The consents document deleted by [deployment_id & consent_id].
    """
    request = ''.join([const.CONSENT, str(deployment_id), const.CONSENT_ID, str(consent_id)])
    response = api.delete(environment, request, access_token)
    return response
