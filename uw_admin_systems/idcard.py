# Copyright 2026 UW-IT, University of Washington
# SPDX-License-Identifier: Apache-2.0

import json
from uw_admin_systems import get_idcard_resource
from uw_admin_systems.models import IDcardElig

IDCARD_API = "/idcarddataws/api/person/v1/eligibility/{}"


def get_idcard_elig(netid):
    url = IDCARD_API.format(netid)
    data = get_idcard_resource(url)
    return IDcardElig.create(json.loads(data))
