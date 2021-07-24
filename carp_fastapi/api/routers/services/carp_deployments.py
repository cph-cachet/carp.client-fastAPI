"""
Copyright 2018 Copenhagen Center for Health Technology (CACHET) at the Technical University of Denmark (DTU).

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the ”Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED ”AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""
from fastapi import APIRouter, Request

from carp import datapoint_service as datapoint, consent_service as consent, deployment_service as deployment
from carp_fastapi.resources import carp_environment as env

router = APIRouter()

"""
DATAPOINT :: CREATE :: GET :: DELETE
"""


@router.post("/{deployment_id}/data-points")
async def create_data_point(request: Request, deployment_id: str):
    """
    Endpoint: [create_data_point]
    :param request: The [request] body.
    :param deployment_id: The [deployment_id] assigned in the deployment.
    :return: The new create data point by its [deployment_id].
    """
    body: bytes = await request.body()
    request_body: str = bytes.decode(body)
    response = await datapoint.create_data_point(env.BASE_URL["production"],
                                                 access_token=request.headers['authorization'],
                                                 deployment_id=deployment_id,
                                                 data_points_body=request_body)
    return response


@router.post("/{deployment_id}/data-points/batch")
async def create_many_data_point(request: Request, deployment_id: str):
    """
    Endpoint: [create_many_data_points]
    :param request: The [request] body.
    :param deployment_id: The [deployment_id] assigned in the deployment.
    :return: The new created data points.
    """
    body: bytes = await request.body()
    request_body: str = bytes.decode(body)
    response = await datapoint.create_many_data_points(env.BASE_URL["production"],
                                                       access_token=request.headers['authorization'],
                                                       deployment_id=deployment_id,
                                                       data_points_body=request_body)
    return response


@router.get('/{deployment_id}/data-points/{data_point_id}')
async def get_one_data_point(request: Request, deployment_id: str, data_point_id: str):
    """
    Endpoint: [get_one_data_point]
    :param request: The [request] header.
    :param deployment_id: The [deployment_id] assigned in the deployment.
    :param data_point_id: The [data_point_id] assigned in the data point.
    :return: The data point by its [data_point_id] and [data_point_id].
    """
    response = await datapoint.get_data_point(env.BASE_URL["production"],
                                              access_token=request.headers['authorization'],
                                              deployment_id=deployment_id,
                                              data_point_id=data_point_id)
    return response


@router.get('/{deployment_id}/data-points')
async def get_all_data_points(request: Request, deployment_id: str):
    """
    Endpoint: [get_all_data_points]
    :param request: The [request] header.
    :param deployment_id: The [deployment_id] assigned in the deployment.
    :return: The data points by their [deployment_id].
    """
    response = await datapoint.get_all_data_points(env.BASE_URL["production"],
                                                   access_token=request.headers['authorization'],
                                                   deployment_id=deployment_id)
    return response


@router.get('/{deployment_id}/data-points/page/{page_id}')
async def get_all_data_points_pageable(request: Request, deployment_id: str, page_id: int = 0):
    """
    Endpoint: [get_all_data_points_pageable]
    :param request: The [request] header.
    :param deployment_id: The [deployment_id] assigned in the deployment.
    :param page_id: The [page_id] of the data point.
    :return: The data points by their [deployment_id] and [page_number].
    """
    response = await datapoint.get_all_data_points_pageable(env.BASE_URL["production"],
                                                            access_token=request.headers['authorization'],
                                                            deployment_id=deployment_id,
                                                            page=page_id)
    return response


@router.get('/{deployment_id}/data-points/sort/{sort_param}')
async def get_all_data_points_sorted(request: Request, deployment_id: str, sort_param: str):
    """
    Endpoint: [get_all_data_points_sorted]
    :param request: The [request] header.
    :param deployment_id: The [deployment_id] assigned in the deployment.
    :param sort_param: The [sort_param] parameter to order the data points (asc, desc).
    :return: The data points sorted by their [deployment_id] and the [sort_param] parameter.
    """
    response = await datapoint.get_all_data_points_sorted(env.BASE_URL["production"],
                                                          access_token=request.headers['authorization'],
                                                          deployment_id=deployment_id,
                                                          sort=sort_param)
    return response


@router.get('/{deployment_id}/data-points/query/{query_param}')
async def get_all_data_points_with_query(request: Request, deployment_id: str, query_param: str):
    """
    Endpoint: [get_all_data_points_with_query]
    :param request: The [request] header.
    :param deployment_id: The [deployment_id] assigned in the deployment.
    :param query_param: The [query_param] parameters to retrieve the data point.
    :return: The data points by their [deployment_id] and the [query_param].
    """
    response = await datapoint.get_all_nested_query(env.BASE_URL["production"],
                                                    access_token=request.headers['authorization'],
                                                    deployment_id=deployment_id,
                                                    query=query_param)
    return response


@router.get('/{deployment_id}/data-points/count/query/{query_param}')
async def get_count_of_data_points(request: Request, deployment_id: str, query_param: str):
    """
    Endpoint: [get_all_data_points_with_query]
    :param request: The [request] header.
    :param deployment_id: The [deployment_id] assigned in the deployment.
    :param query_param: The [query_param] parameters to retrieve the data point.
    :return: The data points by their [deployment_id] and the [query] parameter.
    """
    response = await datapoint.get_count_data_points(env.BASE_URL["production"],
                                                     access_token=request.headers['authorization'],
                                                     deployment_id=deployment_id,
                                                     query=query_param)
    return response


@router.delete('/{deployment_id}/data-points/{data_point_id}')
async def delete_data_point(request: Request, deployment_id: str, data_point_id: str):
    """
    Endpoint: [delete_data_point]
    :param request: The [request] header.
    :param deployment_id: The [deployment_id] assigned in the deployment.
    :param data_point_id: The [data_point_id] assigned in the data point.
    :return: The [data_point_id] of the delete data point.
    """
    response = await datapoint.delete_data_point(env.BASE_URL["production"],
                                                 access_token=request.headers['authorization'],
                                                 deployment_id=deployment_id,
                                                 data_point_id=data_point_id)
    return response


"""
 CONSENT DOCUMENT :: CREATE :: GET :: DELETE
"""


@router.post('/{deployment_id}/consent-documents')
async def create_collection(request: Request, deployment_id: str):
    """
    Endpoint: [create_consent]
    :param request: The [request] body.
    :param deployment_id: The [deployment_id] of the consent document.
    :return: The newly created consent document by its [deployment_id].
    """
    body: bytes = await request.body()
    request_body: str = bytes.decode(body)
    response = await consent.create_consent(env.BASE_URL["production"],
                                            access_token=request.headers['authorization'],
                                            deployment_id=deployment_id,
                                            consent_body=request_body)
    return response


@router.get('/{deployment_id}/consent-documents/{consent_id}')
async def get_consent_document(request: Request, deployment_id: str, consent_id: str):
    """
    Endpoint: [get_consent_document]
    :param request: The [request] header.
    :param deployment_id: The [deployment_id] of the consent document.
    :param consent_id: The [consent_id] of the consent document.
    :return: The consent document by its [deployment_id] and [consent_id].
    """
    response = await consent.get_consent_document(env.BASE_URL["production"],
                                                  access_token=request.headers['authorization'],
                                                  deployment_id=deployment_id,
                                                  consent_id=consent_id)
    return response


@router.get('/{deployment_id}/consent-documents')
async def get_all_consent_documents(request: Request, deployment_id: str):
    """
    Endpoint: [get_all_consent_documents]
    :param request: The [request] header.
    :param deployment_id: The [deployment_id] of the deployment.
    :return: The consent documents by its [deployment_id].
    """
    response = await consent.get_all_consent_documents(env.BASE_URL["production"],
                                                       access_token=request.headers['authorization'],
                                                       deployment_id=deployment_id)
    return response


@router.delete('/{deployment_id}/consent-documents/{consent_id}')
async def delete_consent_document(request: Request, deployment_id: str, consent_id: str):
    """
    Endpoint: [delete_consent_document]
    :param request: The [request] header.
    :param deployment_id: The [deployment_id] of the study deployment.
    :param consent_id: The [consent_id] of the consent document.
    :return: The deleted deployment.
    """
    response = await consent.delete_consent(env.BASE_URL["production"],
                                            access_token=request.headers['authorization'],
                                            deployment_id=deployment_id,
                                            consent_id=consent_id)
    return response


"""
 DEPLOYMENTS :: CREATE :: GET :: DELETE
"""


@router.post('/deployment-service')
async def deployment_service(request: Request):
    """
    Endpoint: [deployment_service]
    :param request: The [request] body.
    :return: The deployment response.
    """
    body: bytes = await request.body()
    request_body: str = bytes.decode(body)
    response = await deployment.deployment_service(env.BASE_URL["production"],
                                                   access_token=request.headers['authorization'],
                                                   deployment_body=request_body)
    return response


@router.post('/participation-service')
async def deployment_participation(request: Request):
    """
    Endpoint: [deployment_participation]
    :param request: The [request] body.
    :return: The deployment response.
    """
    body: bytes = await request.body()
    request_body: str = bytes.decode(body)
    response = await deployment.deployment_participation(env.BASE_URL["production"],
                                                         access_token=request.headers['authorization'],
                                                         deployment_body=request_body)
    return response


@router.post('/participation-service')
async def deployment_statistics(request: Request):
    """
    Endpoint: [deployment_statistics]
    :return: The deployment statistics response.
    """
    body: bytes = await request.body()
    request_body: str = bytes.decode(body)
    response = await deployment.deployment_statistics(env.BASE_URL["production"],
                                                      access_token=request.headers['authorization'],
                                                      deployment_body=request_body)
    return response

