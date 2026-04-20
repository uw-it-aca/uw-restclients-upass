# Copyright 2026 UW-IT, University of Washington
# SPDX-License-Identifier: Apache-2.0

import json
from uw_admin_systems import get_upass_resource
from uw_admin_systems.models import UPassStatus

UPASS_API = "/upassdataws/api/person/v1/membershipstatus/{}"


def get_upass_status(netid):
    url = UPASS_API.format(netid)
    data = get_upass_resource(url)
    return UPassStatus.create(json.loads(data))
