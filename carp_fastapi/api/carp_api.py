"""
Copyright 2018 Copenhagen Center for Health Technology (CACHET) at the Technical University of Denmark (DTU).

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the ”Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED ”AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""
from fastapi import APIRouter

from carp_fastapi.api.routers.auth import carp_auth, carp_users, carp_accounts
from carp_fastapi.api.routers.services import carp_deployments, carp_studies, carp_monitor, carp_protocols, carp_summaries

# Routes
router = APIRouter()

# Auth
router.include_router(carp_auth.router, tags=["oauth"], prefix="/oauth")
router.include_router(carp_users.router, tags=["users"], prefix="/api/users")
router.include_router(carp_accounts.router, tags=["accounts"], prefix="/api/accounts")

# Deployments, Data Points, and Consent Documents
router.include_router(carp_deployments.router, tags=["api-deployments"], prefix="/api/deployments")

# Study, Collection, Documents, and File
router.include_router(carp_studies.router, tags=["api-studies"], prefix="/api/studies")

# Protocol
router.include_router(carp_protocols.router, tags=["api-protocol"], prefix="/api/protocols")

# Summaries
router.include_router(carp_summaries.router, tags=["api-summaries"], prefix="/api/summaries")

# Monitor
router.include_router(carp_monitor.router, tags=["api-monitor"], prefix="/api")
