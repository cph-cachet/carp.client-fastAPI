"""
Copyright 2018 Copenhagen Center for Health Technology (CACHET) at the Technical University of Denmark (DTU).

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the ”Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED ”AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""
from carp import carp_constants as const, carp_api as api

"""
[STUDY]
 - The [study_service.py] is used to CREATE|UPDATE|GET| study in the CARP Platform.
"""


async def study_service(environment, access_token, study_body):
    """
    Function: [study_service]
    :param environment: The CARP [environment].
    :param study_body: The [study_body] object to handle request.
    :param access_token: The [access_token] parameter to grant request.
    :return: The study service response.
    """
    request = ''.join([const.STUDY_SERVICE])
    response = api.post(environment, request, study_body, access_token)
    return response


async def participant_service(environment, access_token, participant_body):
    """
    Function: [participant_service]
    :param environment: The CARP [environment].
    :param participant_body: The [participant_body] object to handle request.
    :param access_token: The [access_token] parameter to grant request.
    :return: The participant service response.
    """
    request = ''.join([const.STUDY_PARTICIPANTS])
    response = api.post(environment, request, participant_body, access_token)
    return response


async def add_researcher(environment, access_token, study_id, researcher_body):
    """
    Function: [add_researcher]
    :param environment: The CARP [environment].
    :param study_id: The [study_id] of the study deployment.
    :param researcher_body: The [researcher_body] object containing researcher details.
    :param access_token: The [access_token] parameter to grant request.
    :return: The researcher added to study.
    """
    request = ''.join([const.ADD_RESEARCHERS, str(study_id), const.STUDY_RESEARCHERS])
    response = api.post(environment, request, researcher_body, access_token)
    return response


async def get_participants_info(environment, access_token, study_id):
    """
    Function: [get_participants_info]
    :param environment: The CARP [environment].
    :param access_token: The [access_token] parameter to grant request.
    :param study_id: The [study_id] of the study deployment.
    @return: The participants information with a given [study_id].
    """
    request = ''.join([const.ADD_RESEARCHERS, str(study_id), const.PARTICIPANTS])
    response = api.get(environment, request, access_token)
    return response
