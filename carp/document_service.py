"""
Copyright 2018 Copenhagen Center for Health Technology (CACHET) at the Technical University of Denmark (DTU).

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the ”Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED ”AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

from carp import carp_constants as const, carp_api as api

"""
[DOCUMENTS]
 - The [document_service.py] is used to CREATE|UPDATE|GET|DELETE documents in the CARP Platform.
"""


async def create_documents(environment, access_token, study_id, document_body):
    """
    Function: [create_documents]
    :param environment: The CARP [environment].
    :param access_token: The [access_token] used for login.
    :param study_id: The [study_id] of the study is consent assigned.
    :param document_body: The [document_body] object containing document information.
    :return: The newly created documents.
    """
    request = ''.join([const.CREATE_DOCUMENTS, str(study_id), const.DOCUMENTS])
    response = api.post(environment, request, document_body, access_token)
    return response


async def get_document(environment, access_token, study_id, document_id):
    """
    Function: [get_document]
    :param environment: The CARP [environment].
    :param access_token: The [access_token] to grant the request.
    :param study_id: The [study_id] of the study is document assigned.
    :param document_id: The [document_id].
    :return: The retrieved document.
    """
    request = ''.join([const.CREATE_DOCUMENTS, str(study_id), const.DOCUMENT_ID, str(document_id)])
    response = api.get(environment, request, access_token)
    return response


async def get_all_documents(environment, access_token, study_id):
    """
    Function: [get_all_documents]
    :param environment: The CARP [environment].
    :param access_token: The [access_token] to grant the request.
    :param study_id: The [study_id].
    :return: All documents with the given [study_id].
    """
    request = ''.join([const.CREATE_DOCUMENTS, str(study_id), const.DOCUMENTS])
    response = api.get(environment, request, access_token)
    return response


async def get_all_documents_sorted(environment, access_token, study_id, sort):
    """
    Function: [get_all_documents_sorted]
    :param environment: The CARP [environment].
    :param access_token: The [access_token] to grant the request.
    :param study_id: The [study_id].
    :param sort: Sorting documents by given parameter [asc|desc]
    :return: All the documents sorted.
    """
    request = ''.join([const.CREATE_DOCUMENTS, str(study_id), const.DOCUMENT_SORT, str(sort)])
    response = api.get(environment, request, access_token)
    return response


async def get_all_documents_query(environment, access_token, study_id, query):
    """
    Function: [get_all_documents_query]
    :param environment: The CARP [environment].
    :param access_token: The [access_token] to grant the request.
    :param study_id: The [study_id].
    :param query: The document query.
    :return: All documents with a given [study_id] and [query].
    """
    request = ''.join([const.CREATE_DOCUMENTS, str(study_id), const.DOCUMENT_QUERY, str(query)])
    response = api.get(environment, request, access_token)
    return response


async def update_documents(environment, access_token, study_id, document_id, document_body):
    """
    Function: [update_documents]
    :param environment: The CARP [environment].
    :param document_body: The [document_body].
    :param document_id: The [document_id].
    :param study_id: The [study_id].
    :param access_token: The [access_token] to grant the request.
    :return: The updated document.
    """
    request = ''.join([const.CREATE_DOCUMENTS, str(study_id), const.DOCUMENT_ID, str(document_id)])
    response = api.put(environment, request, document_body, access_token)
    return response


async def append_documents(environment, access_token, study_id, document_id, document_body):
    """
    Function: [append_documents]
    :param environment: The CARP [environment].
    :param document_body: The [document_body].
    :param document_id: The [document_id].
    :param study_id: The [study_id].
    :param access_token: The [access_token] to grant the request.
    :return: The updated documents.
    """
    request = ''.join([const.CREATE_DOCUMENTS, str(study_id), const.DOCUMENT_ID, str(document_id), const.DOCUMENT_APPEND])
    response = api.put(environment, request, document_body, access_token)
    return response


async def delete_document(environment, access_token, study_id, document_id):
    """
    Function: [delete_document]
    :param environment: The CARP [environment].
    :param document_id: The [document_id].
    :param study_id: The [study_id].
    :param access_token: The [access_token] to grant the request.
    :return: The deleted document id.
    """
    request = ''.join([const.CREATE_DOCUMENTS, str(study_id), const.DOCUMENT_ID, str(document_id)])
    response = api.delete(environment, request, access_token)
    return response
