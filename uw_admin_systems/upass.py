# Copyright 2025 UW-IT, University of Washington
# SPDX-License-Identifier: Apache-2.0

"""
This is the interface for interacting with the UPass service.

"""

import json
from uw_admin_systems import DAO
from restclients_core.exceptions import DataFailureException
from uw_admin_systems.models import UPassStatus


def get_upass_status(netid):
    url = get_upass_url(netid)
    response = DAO.getURL(
        url, {'Accept': 'application/json', 'Connection': 'keep-alive'})
    data = (
        response.data.decode('UTF-8') if isinstance(response.data, bytes)
        else response.data)
    if response.status != 200:
        raise DataFailureException(url, response.status, data)
    return UPassStatus.create(json.loads(data))


def get_upass_url(netid):
    return "/upassdataws/api/person/v1/membershipstatus/{}".format(netid)
