"""
Copyright 2018 Copenhagen Center for Health Technology (CACHET) at the Technical University of Denmark (DTU).

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the ”Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED ”AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

# SLASH
SLASH = "/"

# API
API_PREFIX = ''.join(["api", SLASH])

# ACCOUNTS
OAUTH_TOKEN = ''.join(["oauth", SLASH, "token"])
CURRENT_USER = ''.join([API_PREFIX, "users", SLASH, "current"])
REGISTER_USER = ''.join([API_PREFIX, "users", SLASH, "register"])

# ACCOUNT INVITATION
ACCOUNTS = "accounts"
USERS = "users"
STUDY_MANAGER = "study-manager"
PARTICIPANT = ''.join([API_PREFIX, ACCOUNTS, SLASH, "participant"])
STUDY_OWNER = ''.join([API_PREFIX, ACCOUNTS, SLASH, "study-owner"])
CARP_ADMINISTRATOR = ''.join([API_PREFIX, ACCOUNTS, SLASH, "carp-admin"])
SYSTEM_ADMINISTRATOR = ''.join([API_PREFIX, ACCOUNTS, SLASH, "system-admin"])
FORGOTTEN_PASSWORD = ''.join([API_PREFIX, SLASH, USERS, SLASH, "forgotten-password/send"])
SEND_PASSWORD = ''.join([API_PREFIX, SLASH, USERS, SLASH, "forgotten-password/save"])
UNLOCK_ACCOUNT = ''.join([API_PREFIX, SLASH, ACCOUNTS, SLASH, "unlock"])
CHANGE_PASSWORD = ''.join([API_PREFIX, SLASH, USERS, SLASH, "password"])
RESEARCHER_ACCOUNT = ''.join([API_PREFIX, SLASH, ACCOUNTS, SLASH])

# STUDIES"
STUDIES = "studies"
STUDY_RESEARCHERS = "/researchers"
PARTICIPANTS = "/participants"
CREATE_STUDY = ''.join([API_PREFIX, STUDIES])
ADD_RESEARCHERS = ''.join([CREATE_STUDY, SLASH])
STUDY_SERVICE = ''.join([API_PREFIX, "study-service"])
STUDY_PARTICIPANTS = ''.join([API_PREFIX, "participant-service"])

# DEPLOYMENTS
DEPLOYMENTS_SERVICE = ''.join([API_PREFIX, "deployment-service"])
DEPLOYMENTS_PARTICIPATION = ''.join([API_PREFIX, "participation-service"])
DEPLOYMENTS_STATISTICS = ''.join([API_PREFIX, "deployment-service/statistics"])

# PROTOCOL
PROTOCOL_SERVICE = ''.join([API_PREFIX, "protocol-service"])
PROTOCOL_FACTORY_SERVICE = ''.join([API_PREFIX, "protocol-factory-service"])

# FILE
FILE_STUDY = ''.join([API_PREFIX, STUDIES, SLASH])
FILES = ''.join([SLASH, "files"])
FILES_QUERY = ''.join([SLASH, "files?query="])
FILES_ID = ''.join([SLASH, "files", SLASH])
FILE_DOWNLOAD = ''.join([SLASH, "download"])

# DATA POINT
DATA_POINTS = "data-points"
DATA_POINTS_STUDY = ''.join([API_PREFIX, "deployments", SLASH])
DATA_POINT_QUERY = ''.join([SLASH, DATA_POINTS, "?query="])
DATA_POINT_COUNT_QUERY = ''.join([SLASH, DATA_POINTS, "/count?query="])
DATA_POINT = ''.join([SLASH, DATA_POINTS])
DATA_BATCH = ''.join([SLASH, "batch"])
DATA_PAGE = "?page="
DATA_SORT = "?sort="

# CONSENT DOCUMENT
CONSENT_DOCUMENT = "consent-documents"
CONSENT = ''.join([API_PREFIX, "deployments", SLASH])
CONSENT_ID = ''.join([SLASH, CONSENT_DOCUMENT, SLASH])
CONSENT_DOCUMENTS = ''.join([SLASH, CONSENT_DOCUMENT])

# DOCUMENTS
DOCUMENT = "documents"
CREATE_DOCUMENTS = ''.join([API_PREFIX, STUDIES, SLASH])
DOCUMENTS = ''.join([SLASH, DOCUMENT])
DOCUMENT_ID = ''.join([SLASH, DOCUMENT, SLASH])
DOCUMENT_QUERY = ''.join([SLASH, DOCUMENT, "?query="])
DOCUMENT_SORT = "?sort="
DOCUMENT_APPEND = ''.join([SLASH, "append"])

# COLLECTION
COLLECTIONS = "collections"
COLLECTION_CREATE = ''.join([API_PREFIX, STUDIES, SLASH])
COLLECTION_NAME = ''.join([SLASH, COLLECTIONS, SLASH])
COLLECTION_ID = ''.join([SLASH, COLLECTIONS, SLASH, "id", SLASH])
COLLECTION_QUERY = ''.join([SLASH, "query="])

# SUMMARY
SUMMARIES = "summaries"
CREATE_SUMMARY = ''.join([API_PREFIX, SUMMARIES, "?studyId="])
GET_ALL_SUMMARIES = ''.join([API_PREFIX, SUMMARIES, SLASH, "all"])
DOWNLOAD = "download"
DOWNLOAD_SUMMARY = ''.join([API_PREFIX, SUMMARIES, SLASH])
SUMMARY_ID = ''.join([API_PREFIX, SUMMARIES, SLASH])

# MONITORING
HEALTH_BASE = "status"
HEALTH_CURRENT = "health"
INFO = ''.join([API_PREFIX, HEALTH_BASE, SLASH, 'info'])
GIT_INFO = ''.join([API_PREFIX, HEALTH_BASE, SLASH, 'git'])
FLYWAY_INFO = ''.join([API_PREFIX, HEALTH_BASE, SLASH, 'flyway'])
HEALTH_INFO = ''.join([API_PREFIX, HEALTH_BASE, SLASH, 'health'])
HEALTH_DISK_SPACE = ''.join([API_PREFIX, HEALTH_BASE, SLASH, HEALTH_CURRENT, SLASH, 'diskSpace'])
HEALTH_DB = ''.join([API_PREFIX, HEALTH_BASE, SLASH, HEALTH_CURRENT, SLASH, 'db'])
HEALTH_RABBIT = ''.join([API_PREFIX, HEALTH_BASE, SLASH, HEALTH_CURRENT, SLASH, 'rabbit'])
HEALTH_PING = ''.join([API_PREFIX, HEALTH_BASE, SLASH, HEALTH_CURRENT, SLASH, 'ping'])
MAIL = ''.join([API_PREFIX, SLASH, 'mail'])

