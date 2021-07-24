"""
Copyright 2018 Copenhagen Center for Health Technology (CACHET) at the Technical University of Denmark (DTU).

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the ”Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED ”AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

from carp import carp_constants as const, carp_api as api
import json

"""
[FILE]
 - The [file_service.py] is used to CREATE|UPDATE|GET|DELETE file in the CARP Platform.
"""


async def upload_file(environment, access_token, file_to_upload, study_id, meta_data):
    """
    Function: [upload_file]
    :param environment: The CARP [environment].
    :param meta_data: The file [meta_data].
    :param access_token: The [access_token] to grant access.
    :param file_to_upload: The file to upload.
    :param study_id: The [study_id].
    :return: The uploaded file name.
    """
    metadata = {"metadata": meta_data}
    file_to_upload = {
        'file': open(file_to_upload, 'rb'),
        'metadata': (None, json.dumps(metadata), 'application/json'),
    }
    request = ''.join([const.FILE_STUDY, str(study_id), const.FILES])
    response = api.post(environment, request, file_to_upload, access_token)
    return response['id']


async def download_file(environment, access_token, study_id, file_id):
    """
    Function: [download_file]
    :param environment: The CARP [environment].
    :param access_token: The [access_token].
    :param study_id: The [study_id].
    :param file_id: The [file_id].
    :return: The file name downloaded.
    """
    file_object = api.get(environment, const.FILE_STUDY + str(study_id) + const.FILES_ID + str(file_id), access_token)
    local_filename = file_object['original_name']
    file_stream = api.get(environment, const.FILE_STUDY + str(study_id) + const.FILES_ID + str(file_id) + const.FILE_DOWNLOAD, access_token)

    with open(local_filename, 'wb') as destination:
        for chunk in file_stream.iter_content(chunk_size=1024):
            if chunk:
                destination.write(chunk)
    return str(local_filename)


async def get_file(environment, access_token, study_id, file_id):
    """
    Function: [get_file]
    :param environment: The CARP [environment].
    :param access_token: The [access_token] to grant request.
    :param study_id: The [study_id].
    :param file_id: The [file_id].
    :return: The file meta data with a given study_id and file_id.
    """
    request = ''.join([const.FILE_STUDY, str(study_id), const.FILES_ID, str(file_id)])
    response = api.get(environment, request, access_token)
    return response


async def get_all(environment, access_token, study_id):
    """
    Function: [get_all]
    :param environment: The CARP [environment].
    :param access_token: The [access_token].
    :param study_id: The [study_id].
    :return: The files for specific [study_id].
    """
    request = ''.join([const.FILE_STUDY, str(study_id), const.FILES])
    response = api.get(environment, request, access_token)
    return response


async def get_files_nested_query(environment, access_token, study_id, query):
    """
    Function: [get_files]
    :param environment: The CARP [environment].
    :param query: The file query.
    :param access_token: The [access_token] to grant access.
    :param study_id: The [study_id].
    :return: The files for specific study id and given query.
    """
    request = ''.join([const.FILE_STUDY, str(study_id), const.FILES_QUERY, str(query)])
    response = api.get(environment, request, access_token)
    return response


async def delete_file(environment, access_token, study_id, file_id):
    """
    Function: [delete_file]
    :param environment: The CARP [environment].
    :param access_token: The [access_token].
    :param study_id: The [study_id].
    :param file_id: The [file_id].
    :return: The deleted file name.
    """
    request = ''.join([const.FILE_STUDY, str(study_id), const.FILES_ID, str(file_id)])
    response = api.delete(environment, request, access_token)
    return response
