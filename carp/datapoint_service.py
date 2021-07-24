"""
Copyright 2018 Copenhagen Center for Health Technology (CACHET) at the Technical University of Denmark (DTU).

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the ”Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED ”AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""
from carp import carp_constants as const, carp_api as api

"""
[DATAPOINTS]
 - The [datapoint_service.py] is used to CREATE|UPDATE|GET|DELETE data points in the CARP Platform.
"""


async def create_data_point(environment, access_token, deployment_id, data_points_body):
    """
    Function: [create_data_point]
    :param environment: The CARP [environment].
    :param access_token: The [access_token].
    :param deployment_id: The [deployment_id].
    :param data_points_body: The [data_points_body].
    :return: The data point created.
    """
    request = ''.join([const.DATA_POINTS_STUDY, str(deployment_id), const.DATA_POINT])
    response = api.post(environment, request, data_points_body, access_token)
    return response


async def create_many_data_points(environment, access_token, deployment_id, data_points_body):
    """
    Function: [create_many_data_points]
    :param environment: The CARP [environment].
    :param access_token: The [access_token].
    :param deployment_id: The [deployment_id].
    :param data_points_body: The [data_points_body].
    :return: The data points created.
    """
    request = ''.join([const.DATA_POINTS_STUDY, str(deployment_id), const.DATA_POINT, const.DATA_BATCH])
    response = api.post(environment, request, data_points_body, access_token)
    return response


async def get_data_point(environment, access_token, deployment_id, data_point_id):
    """
    Function: [get_data_point]
    :param environment: The CARP [environment].
    :param access_token: The [access_token].
    :param deployment_id: The [deployment_id].
    :param data_point_id: The [data_point_id].
    :return: The data points for a given [deployment_id] and [data_point_id].
    """
    request = ''.join([const.DATA_POINTS_STUDY, str(deployment_id), const.DATA_POINT, const.SLASH, str(data_point_id)])
    response = api.get(environment, request, access_token)
    return response


async def get_all_data_points(environment, access_token, deployment_id):
    """
    Function: [get_all_data_points]
    :param environment: The CARP [environment].
    :param access_token: The [access_token].
    :param deployment_id: The [deployment_id].
    :return: All data points for a given [deployment_id].
    """
    request = ''.join([const.DATA_POINTS_STUDY, str(deployment_id), const.DATA_POINT])
    response = api.get(environment, request, access_token)
    return response


async def get_all_data_points_pageable(environment, access_token, deployment_id, page):
    """
    Function: [get_all_data_points_pageable]
    :param environment: The CARP [environment].
    :param access_token: The [access_token].
    :param page: The [page] number
    :param deployment_id: The [deployment_id].
    :return: All data points for a given [deployment_id].
    """
    request = ''.join([const.DATA_POINTS_STUDY, str(deployment_id), const.DATA_POINT, const.DATA_PAGE, str(page)])
    response = api.get(environment, request, access_token)
    return response


async def get_all_data_points_sorted(environment, access_token, deployment_id, sort):
    """
    Function: [get_all_data_points_sorted]
    :param environment: The CARP [environment].
    :param access_token: The [access_token].
    :param sort: the sort [variable, asc|desc]
    :param deployment_id: The [deployment_id].
    :return: All data points for a given [deployment_id].
    """
    request = ''.join([const.DATA_POINTS_STUDY, str(deployment_id), const.DATA_POINT, const.DATA_SORT, str(sort)])
    response = api.get(environment, request, access_token)
    return response


async def get_all_nested_query(environment, access_token, deployment_id, query):
    """
    Function: [get_all_nested_query]
    :param environment: The CARP [environment].
    :param access_token: The [access_token].
    :param query: The query examples: [{carp_header.data_format.name==}, {query=create_at>...;created_at<...]
    :param deployment_id: The [deployment_id].
    :return: The data points for specific [deployment_id] and [query].
    """
    request = ''.join([const.DATA_POINTS_STUDY, str(deployment_id), const.DATA_POINT_QUERY, str(query)])
    response = api.get(environment, request, access_token)
    return response


async def delete_data_point(environment, access_token, deployment_id, data_point_id):
    """
    Function: [delete_data_point]
    :param environment: The CARP [environment].
    :param access_token: The [access_token].
    :param deployment_id: The [deployment_id]
    :param data_point_id: The data point id
    :return: The deleted data point.
    """
    request = ''.join([const.DATA_POINTS_STUDY, str(deployment_id), const.DATA_POINT + const.SLASH, str(data_point_id)])
    response = api.delete(environment, request, access_token)
    return response


async def get_data_points_by_user_id(environment, access_token, deployment_id, user_id):
    """
    Function: [get_data_points]
    :param environment: The CARP [environment].
    :param access_token: The [access_token].
    :param deployment_id: The [deployment_id].
    :param user_id: The [user_id].
    :return: The data points  for a given [deployment_id] and [user_id].
    """
    request = ''.join([const.DATA_POINTS_STUDY, str(deployment_id), const.DATA_POINT_QUERY, str(user_id)])
    response = api.get(environment, request, access_token)
    return response


async def get_count_data_points(environment, access_token, deployment_id, query):
    """
    Function: [get_count_data_points]
    :param environment: The CARP [environment].
    :param access_token: The [access_token].
    :param query: The query examples: [{carp_header.data_format.name==}, {query=create_at>...;created_at<...]
    :param deployment_id: The [deployment_id].
    :return: The number of data points for specific [deployment_id] and [query].
    """
    request = ''.join([const.DATA_POINTS_STUDY, str(deployment_id), const.DATA_POINT_COUNT_QUERY, str(query)])
    response = api.get(environment, request, access_token)
    return response
