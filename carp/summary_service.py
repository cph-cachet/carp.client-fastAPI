"""
Copyright 2018 Copenhagen Center for Health Technology (CACHET) at the Technical University of Denmark (DTU).

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the ”Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED ”AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""
from carp import carp_constants as const, carp_api as api

"""
[SUMMARY]
 - The [summary_service.py] is used to download the data stored in studies.
"""


async def create_summary(environment, access_token, study_id):
    """
    Function: [create_summary]
    :param environment: The CARP [environment].
    :param access_token: The access [access_token].
    :param study_id: The [study_id].
    :return: The created Summary for the given study id.
    """
    request = ''.join([const.CREATE_SUMMARY, str(study_id)])
    response = api.get(environment, request, access_token)

    return response


async def get_all_summaries(environment, access_token):
    """
    Function: [get_all_summaries]
    :param environment: The CARP [environment].
    :param access_token: The access [access_token].
    :return: All the summaries available.
    """
    request = ''.join([const.GET_ALL_SUMMARIES])
    response = api.get(environment, request, access_token)

    return response


async def download_summaries(environment, access_token, summary_id):
    """
    Function: [download_summaries]
    :param summary_id: The Summary ID.
    :param environment: The CARP [environment].
    :param access_token: The access [access_token].
    :return: The downloaded summaries file.
    """
    request = ''.join([const.DOWNLOAD_SUMMARY, str(summary_id), const.DOWNLOAD])
    response = api.get(environment, request, access_token)

    return response


async def get_summaries_by_id(environment, access_token, summary_id):
    """
    Function: [get_summaries_by_id]
    :param environment: The CARP [environment].
    :param access_token: The access [access_token].
    :param summary_id: The [summary_id].
    :return: The summary by the [summary_id].
    """
    request = ''.join([const.SUMMARY_ID, str(summary_id)])
    response = api.get(environment, request, access_token)

    return response
