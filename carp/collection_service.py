"""
Copyright 2018 Copenhagen Center for Health Technology (CACHET) at the Technical University of Denmark (DTU).

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the ”Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED ”AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

from carp import carp_constants as const, carp_api as api

"""
[COLLECTIONS]
 - The [collection_service.py] is used to CREATE|UPDATE|GET|DELETE collections in the CARP Platform.
"""


async def create_collections(environment, access_token, study_id, collection_name, document_name, collections_body):
    """
    Function: [create_collections]
    :param environment: The CARP [environment].
    :param access_token: The [access_token].
    :param study_id: The [study_id].
    :param collection_name: The [collection_name].
    :param document_name: The [document_name].
    :param collections_body: The [collections_body].
    :return: The created collection(s).
    """
    request = ''.join([const.COLLECTION_CREATE, str(study_id), const.COLLECTION_NAME, str(collection_name), const.SLASH, str(document_name)])
    response = api.post(environment, request, collections_body, access_token)
    return response


async def get_collection_by_collection_name_and_document_name(environment, access_token, study_id, collection_name, document_name):
    """
    Function: [get_collection_by_collection_and_document]
    :param environment: The CARP [environment].
    :param access_token: The [access_token].
    :param study_id: The [study_id].
    :param document_name: The [document_name].
    :param collection_name: The [collection_name].
    :return: The requested document by its [study_id], [collection_name] and [document_name].
    """
    request = ''.join([const.COLLECTION_CREATE, str(study_id), const.COLLECTION_NAME, str(collection_name), const.SLASH, str(document_name)])
    response = api.get(environment, request, access_token)
    return response


async def get_collection_by_study_id_and_collection_name(environment, access_token, study_id, collection_name):
    """
    Function: [get_collection_by_collection_name]
    :param environment: The CARP [environment].
    :param access_token: The [access_token].
    :param study_id: The [study_id].
    :param collection_name: The [collection_name].
    :return: The requested document by its [study_id] and [collection_name].
    """
    request = ''.join([const.COLLECTION_CREATE, str(study_id), const.COLLECTION_NAME, str(collection_name)])
    response = api.get(environment, request, access_token)
    return response


async def get_collection_by_study_id_and_collection_id(environment, access_token, study_id, collection_id):
    """
    Function: [get_collection_by_id]
    :param environment: The CARP [environment].
    :param access_token: The [access_token].
    :param study_id: The [study_id].
    :param collection_id: The [collection_id].
    :return: The requested document by its [study_id] and [collection_id].
    """
    request = ''.join([const.COLLECTION_CREATE, str(study_id), const.COLLECTION_ID, str(collection_id)])
    response = api.get(environment, request, access_token)
    return response


async def get_collection_with_nested_query(environment, access_token, study_id, query):
    """
    Function: [get_nested_collection]
    :param environment: The CARP [environment].
    :param access_token: The [access_token].
    :param study_id: The [study_id]
    :param query: The [query].
    :return: The requested document by study id and document id
    """
    request = ''.join([const.COLLECTION_CREATE, str(study_id), const.COLLECTIONS, const.COLLECTION_QUERY, str(query)])
    response = api.get(environment, request, access_token)
    return response


async def update_collection_name(environment, access_token, study_id, collection_id, collection_body):
    """
    Function: [update_collection]
    :param environment: The CARP [environment].
    :param access_token: The [access_token].
    :param study_id: The [study_id].
    :param collection_id: The [collection_id].
    :param collection_body: The [collection_body].
    :return: The updated collection.
    """
    request = ''.join([const.COLLECTION_CREATE, str(study_id), const.COLLECTION_ID, str(collection_id)])
    response = api.put(environment, request, collection_body, access_token)
    return response


async def delete_collection(environment, access_token, study_id, collection_id):
    """
    Function: [delete_collection]
    :param environment: The CARP [environment].
    :param access_token: The [access_token].
    :param study_id: The [study_id].
    :param collection_id: The [collection_id].
    :return: The deleted collection.
    """
    request = ''.join([const.COLLECTION_CREATE, str(study_id), const.COLLECTION_NAME, str(collection_id)])
    response = api.delete(environment, request, access_token)
    return response
