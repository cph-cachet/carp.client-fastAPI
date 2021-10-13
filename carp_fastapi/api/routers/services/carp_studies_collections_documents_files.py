"""
Copyright 2018 Copenhagen Center for Health Technology (CACHET) at the Technical University of Denmark (DTU).

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the ”Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED ”AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""
from fastapi import APIRouter, Request, File, UploadFile
from pydantic import BaseModel

from carp import collection_service as collection, document_service as document, file_service as files, \
    study_service as study
from carp_fastapi.resources import carp_environment as env

from starlette.config import Config

config = Config(".env")
environment: str = config("ENVIRONMENT", default="local")

router = APIRouter()

"""
COLLECTION :: CREATE :: GET :: DELETE
"""


@router.post('/{study_id}/collections/{collection_name}/{document_name}')
async def create_collection(request: Request, study_id: str, collection_name: str, document_name: str):
    """
    Endpoint: [create_collection]
    :param request: The [request] body.
    :param study_id: The [study_id] of the study deployment.
    :param collection_name: The [collection_name] of the collection.
    :param document_name: The [document_name] of the collection.
    :return: The new created collection.
    """
    body: bytes = await request.body()
    request_body: str = bytes.decode(body)
    response = await collection.create_collections(env.BASE_URL[environment],
                                                   access_token=request.headers['authorization'],
                                                   study_id=study_id,
                                                   collection_name=collection_name,
                                                   document_name=document_name,
                                                   collections_body=request_body)
    return response


@router.get('/{study_id}/collections/{collection_name}/{document_name}')
async def get_collection_by_collection_name_and_document_name(request: Request, study_id: str, collection_name: str,
                                                              document_name: str):
    """
    Endpoint: [get_collection_by_collection_name_and_document_name]
    :param request: The [request] header.
    :param study_id: The [study_id] of the study deployment.
    :param collection_name: The [collection_name] of the collection.
    :param document_name: The [document_name] of the collection.
    :return: The collection by its [study_id], [collection_name], [document_name].
    """
    response = await collection.get_collection_by_collection_name_and_document_name(env.BASE_URL[environment],
                                                                                    access_token=request.headers[
                                                                                        'authorization'],
                                                                                    study_id=study_id,
                                                                                    collection_name=collection_name,
                                                                                    document_name=document_name)
    return response


@router.get('/{study_id}/collections/query/{query_param}')
async def get_collection_nested_query(request: Request, study_id: str, query_param: str):
    """
    Endpoint: [get_collection_nested_query]
    :param request: The [request] header.
    :param study_id: The [study_id] of the study deployment.
    :param query_param: The [query_param] parameters to retrieve the collection.
    :return: The collection by its [study_id] and the [query] parameters.
    """
    response = await collection.get_collection_with_nested_query(env.BASE_URL[environment],
                                                                 access_token=request.headers['authorization'],
                                                                 study_id=study_id,
                                                                 query=query_param)
    return response


@router.get('/{study_id}/collections/id/{collection_id}')
async def get_collection_by_study_id_and_collection_name(request: Request, study_id: str, collection_name: str):
    """
    Endpoint: [get_collection_by_collection_id]
    :param request: The [request] header.
    :param study_id: The [study_id] of the study deployment.
    :param collection_name: The [collection_name] assigned in collection.
    :return: The collection by its [study_id] and [collection_id].
    """
    response = await collection.get_collection_by_study_id_and_collection_name(env.BASE_URL[environment],
                                                                               access_token=request.headers['authorization'],
                                                                               study_id=study_id,
                                                                               collection_name=collection_name)
    return response


@router.get('/{study_id}/collections/id/{collection_id}')
async def get_collection_by_study_id_and_collection_id(request: Request, study_id: str, collection_id: str):
    """
    Endpoint: [get_collection_by_collection_id]
    :param request: The [request] header.
    :param study_id: The [study_id] of the study deployment.
    :param collection_id: The [collection_id] assigned in collection.
    :return: The collection by its [study_id] and [collection_id].
    """
    response = await collection.get_collection_by_study_id_and_collection_id(env.BASE_URL[environment],
                                                                             access_token=request.headers[
                                                                                 'authorization'],
                                                                             study_id=study_id,
                                                                             collection_id=collection_id)
    return response


@router.put('/{study_id}/collections/id/{collection_id}')
async def update_collection_name_by_study_id_and_collection_id(request: Request, study_id: str, collection_id: str):
    """
    Endpoint: [update_collection_name_by_study_id_and_collection_id]
    :param request: The [request] header.
    :param study_id: The [study_id] of the study deployment.
    :param collection_id: The [collection_id] assigned in collection.
    :return: The updated collection by its [study_id] and [collection_id].
    """
    response = await collection.update_collection_name(env.BASE_URL[environment],
                                                       access_token=request.headers['authorization'],
                                                       study_id=study_id,
                                                       collection_id=collection_id)
    return response


@router.delete('/{study_id}/collections/{collection_id}')
async def delete_collection_by_study_id_and_collection_id(request: Request, study_id: str, collection_id: str):
    """
    Endpoint: [delete_collection_by_study_id_and_collection_id]
    :param request: The [request] header.
    :param study_id: The [study_id] of the study deployment.
    :param collection_id: The [collection_id] assigned in collection.
    :return: This request doesn't return a response request_body.
    """
    response = await collection.delete_collection(env.BASE_URL[environment],
                                                  access_token=request.headers['authorization'],
                                                  study_id=study_id,
                                                  collection_id=collection_id)
    return response


"""
DOCUMENTS :: CREATE :: GET :: DELETE
"""


@router.post('/{study_id}/documents')
async def create_document(request: Request, study_id: str):
    """
    Endpoint: [create_document]
    :param request: The [request] body.
    :param study_id: The [study_id] of the study deployment.
    :return: The new created document.
    """
    body: bytes = await request.body()
    request_body: str = bytes.decode(body)
    response = await document.create_documents(env.BASE_URL[environment],
                                               access_token=request.headers['authorization'],
                                               study_id=study_id,
                                               document_body=request_body)
    return response


@router.get('/{study_id}/documents/{document_id}')
async def get_document(request: Request, study_id: str, document_id: str):
    """
    Endpoint: [get_document]
    :param request: The [request] header.
    :param study_id: The [study_id] of the study deployment.
    :param document_id: The [document_id] assigned to the document.
    :return: The document by its [study_id] and [document_id].
    """
    response = await document.get_document(env.BASE_URL[environment],
                                           access_token=request.headers['authorization'],
                                           study_id=study_id,
                                           document_id=document_id)
    return response


@router.get('/{study_id}/documents')
async def get_all_documents(request: Request, study_id: str):
    """
    Endpoint: [get_all_documents]
    :param request: The [request] header.
    :param study_id: The [study_id] of the study deployment.
    :return: The documents requested by their [study_id].
    """
    response = await document.get_all_documents(env.BASE_URL[environment],
                                                access_token=request.headers['authorization'],
                                                study_id=study_id)
    return response


@router.get('/{study_id}/documents/sort/{sort_param}')
async def get_all_documents_sorted(request: Request, study_id: str, sort_param: str):
    """
    Endpoint: [get_all_documents_sorted]
    :param request: The [request] header.
    :param study_id: The [study_id] of the study deployment.
    :param sort_param: The [sort_param] parameter to sort the document (asc, desc).
    :return: The documents by their [study_id] and [sort].
    """
    response = await document.get_all_documents_sorted(env.BASE_URL[environment],
                                                       access_token=request.headers['authorization'],
                                                       study_id=study_id,
                                                       sort=sort_param)
    return response


@router.get('/{study_id}/documents/query/{query_param}')
async def get_all_documents_by_query(request: Request, study_id: str, query_param: str):
    """
    Endpoint: [get_all_documents_by_query]
    :param request: The [request] header.
    :param study_id: The [study_id] of the study deployment.
    :param query_param: The [query_param] parameters to retrieve the document.
    :return: The documents by their [study_id] and the [query] parameters.
    """
    response = await document.get_all_documents_query(env.BASE_URL[environment],
                                                      access_token=request.headers['authorization'],
                                                      study_id=study_id,
                                                      query=query_param)
    return response


@router.put('/{study_id}/documents/{document_id}')
async def update_documents(request: Request, study_id: str, document_id: str):
    """
    Endpoint: [update_documents]
    :param request: The [request] body.
    :param study_id: The [study_id] of the study deployment.
    :param document_id: The [document_id] assigned to the document.
    :return: The updated documents by its [study_id] and [document_id].
    """
    body: bytes = await request.body()
    request_body: str = bytes.decode(body)
    response = await document.update_documents(env.BASE_URL[environment],
                                               access_token=request.headers['authorization'],
                                               study_id=study_id,
                                               document_id=document_id,
                                               document_body=request_body)
    return response


@router.put('/{study_id}/documents/{document_id}/append')
async def append_documents(request: Request, study_id: str, document_id: str):
    """
    Endpoint: [append_documents]
    :param request: The [request] body.
    :param study_id: The [study_id] of the study deployment.
    :param document_id: The [document_id] assigned to the document.
    :return: The updated documents with the list of documents by its [study_id] and [document_id].
    """
    body: bytes = await request.body()
    request_body: str = bytes.decode(body)
    response = await document.append_documents(env.BASE_URL[environment],
                                               access_token=request.headers['authorization'],
                                               study_id=study_id,
                                               document_id=document_id,
                                               document_body=request_body)
    return response


@router.delete('/{study_id}/documents/{document_id}')
async def delete_documents(request: Request, study_id: str, document_id: str):
    """
    Endpoint: [delete_documents]
    :param request: The [request] header.
    :param study_id: The [study_id] of the study deployment.
    :param document_id: The [document_id] assigned to the document.
    :return: The [document_id] of the delete document.
    """
    response = await document.delete_document(env.BASE_URL[environment],
                                              access_token=request.headers['authorization'],
                                              study_id=study_id,
                                              document_id=document_id)
    return response


"""
FILE :: CREATE :: GET :: DELETE
"""


class Metadata(BaseModel):
    metadata: str


@router.post('/{study_id}/files')
async def upload_file(request: Request, study_id: str, metadata: Metadata, file: UploadFile = File(...)):
    """
    Endpoint: [upload_file]
    :param file: The file set to upload.
    :param metadata: The [metadata] body.
    :param request: The [request] file.
    :param study_id: The [study_id] assigned to the file to the study deployment.
    :return: The uploaded file with a given [file_id].
    """
    response = await files.upload_file(env.BASE_URL[environment],
                                       access_token=request.headers['authorization'],
                                       file_to_upload=file,
                                       study_id=study_id,
                                       meta_data=metadata)
    return response


@router.post('/{study_id}/files/{file_id}/download')
async def download_file(request: Request, study_id: str, file_id: str):
    """
    Endpoint: [download_file]
    :param request: The [request] header.
    :param study_id: The [study_id] assigned to the file to the study deployment.
    :param file_id: The [file_id] assigned to the file.
    :return: The downloaded file.
    """
    response = await files.download_file(env.BASE_URL[environment],
                                         access_token=request.headers['authorization'],
                                         study_id=study_id,
                                         file_id=file_id)
    return response


@router.get('/{study_id}/files/{file_id}')
async def get_file(request: Request, study_id: str, file_id: str):
    """
    Endpoint: [get_file]
    :param request: The [request] header.
    :param study_id: The [study_id] assigned to the file to the study deployment.
    :param file_id: The [file_id] assigned to the file.
    :return: Retrieve the existing file.
    """
    response = await files.get_file(env.BASE_URL[environment],
                                    access_token=request.headers['authorization'],
                                    study_id=study_id,
                                    file_id=file_id)
    return response


@router.get('/{study_id}/files/{file_id}')
async def get_all_files(request: Request, study_id: str):
    """
    Endpoint: [get_file]
    :param request: The [request] header.
    :param study_id: The [study_id] assigned to the file to the study deployment.
    :return: Retrieve the existing file.
    """
    response = await files.get_all(env.BASE_URL[environment],
                                   access_token=request.headers['authorization'],
                                   study_id=study_id)
    return response


@router.get('/{study_id}/files/query/{meta_data_query}')
async def get_files_by_nested_query(request: Request, study_id: str, meta_data_query: str):
    """
    Endpoint: [get_files_by_query]
    :param request: The [request] header.
    :param study_id: The [study_id] assigned to the file to the study deployment.
    :param meta_data_query: The [meta_data_query] parameters to retrieve a file.
    :return: The file by their [study_id] and the [meta_data_query] parameter(s).
    """
    response = await files.get_files_nested_query(env.BASE_URL[environment],
                                                  access_token=request.headers['authorization'],
                                                  study_id=study_id,
                                                  query=meta_data_query)
    return response


@router.delete('/{study_id}/files/{file_id}')
async def delete_file(request: Request, study_id: str, file_id: str):
    """
    Endpoint: [delete_file]
    :param request: The [request] header.
    :param study_id: The [study_id] assigned to the file to the study deployment.
    :param file_id: The [file_id] assigned to the file.
    :return: The [file_id] of the deleted file.
    """
    response = await files.delete_file(env.BASE_URL[environment],
                                       access_token=request.headers['authorization'],
                                       study_id=study_id,
                                       file_id=file_id)
    return response


"""
STUDY :: CREATE :: GET :: DELETE
"""


@router.post('/{study_id}/researchers')
async def add_researcher(request: Request, study_id: str):
    """
    Endpoint: [add_researcher]
    :param request: The [request] body.
    :param study_id: The [study_id] of the study.
    :return: The new added participant into study deployment by its [study_id].
    """
    body: bytes = await request.body()
    request_body: str = bytes.decode(body)
    response = await study.add_researcher(env.BASE_URL[environment],
                                          access_token=request.headers['authorization'],
                                          study_id=study_id,
                                          researcher_body=request_body)
    return response


@router.post('/study-service')
async def study_service(request: Request):
    """
    Endpoint: [study_service]
    :param request: The [request] body.
    :return: The study service response according to its request.
    """
    body: bytes = await request.body()
    request_body: str = bytes.decode(body)
    response = await study.study_service(env.BASE_URL[environment],
                                         access_token=request.headers['authorization'],
                                         study_body=request_body)
    return response


@router.post('/participant-service')
async def participant_service(request: Request):
    """
    Endpoint: [participant_service]
    :param request: The [request] body.
    :return: The participant service response according to its request.
    """
    body: bytes = await request.body()
    request_body: str = bytes.decode(body)
    response = await study.participant_service(env.BASE_URL[environment],
                                               access_token=request.headers['authorization'],
                                               participant_body=request_body)
    return response


@router.get('/{study_id}/participants')
async def get_participants_info(request: Request, study_id: str):
    """
    Endpoint: [get_participant_info]
    :param request: The [request] header.
    :param study_id: The [study_id] assigned to the file to the study deployment.
    :return: The files by their [study_id] and the [query] parameter(s).
    """
    response = await study.get_participants_info(env.BASE_URL[environment],
                                                 access_token=request.headers['authorization'],
                                                 study_id=study_id)
    return response
