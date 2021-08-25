"""
Copyright 2018 Copenhagen Center for Health Technology (CACHET) at the Technical University of Denmark (DTU).

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the ”Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED ”AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""
from fastapi import APIRouter, Request

from carp import summary_service as summary
from carp_fastapi.resources import carp_environment as env

from starlette.config import Config
config = Config(".env")
environment: str = config("ENVIRONMENT", default="local")

router = APIRouter()

"""
SUMMARIES :: GET
"""


@router.get("/studyId/{study_id}")
async def create_summaries(request: Request, study_id: str):
    """
    Function: [create_summaries]
    :param request: The [request] header.
    :param study_id: The [study_id].
    :return: The summary by it [studyId].
    """
    response = await summary.create_summary(env.BASE_URL[environment],
                                            access_token=request.headers['authorization'],
                                            study_id=study_id)
    return response


@router.get("/all")
async def get_all(request: Request):
    """
    Function: [get_all]
    :param request: The [request] header.
    :return: All the summaries.
    """
    response = await summary.create_summary(env.BASE_URL[environment],
                                            access_token=request.headers['authorization'])
    return response


@router.get("/{summary_id}/download")
async def download(request: Request, summary_id: str):
    """
    Function: [download]
    :param summary_id: The [summary_id].
    :param request: The [request] header.
    :return: Download summary data requested.
    """
    response = await summary.download_summaries(env.BASE_URL[environment],
                                                access_token=request.headers['authorization'],
                                                summary_id=summary_id)
    return response


@router.get("/{summary_id}")
async def get_by_summary_id(request: Request, summary_id: str):
    """
    Function: [get_by_summary_id]
    :param summary_id: The [summary_id].
    :param request: The [request] header.
    :return: Get the summaries by its summary id.
    """
    response = await summary.download_summaries(env.BASE_URL[environment],
                                                access_token=request.headers['authorization'],
                                                summary_id=summary_id)
    return response
