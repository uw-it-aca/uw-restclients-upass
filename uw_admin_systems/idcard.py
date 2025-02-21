# Copyright 2025 UW-IT, University of Washington
# SPDX-License-Identifier: Apache-2.0

"""
This is the interface for interacting with the UPass service.

"""

import json
from uw_admin_systems import get_resource
from uw_admin_systems.models import IDcardStatus


def get_idcard_status(netid):
    data = get_resource(get_upass_url(netid))
    return IDcardStatus.create(json.loads(data))


def get_upass_url(netid):
    return f"/idcarddataws/api/person/v1/eligibility/{netid}"
