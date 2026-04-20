# Copyright 2026 UW-IT, University of Washington
# SPDX-License-Identifier: Apache-2.0

from restclients_core.util.decorators import use_mock
from uw_admin_systems import upassDAO, idcardDAO

fdao_upass_override = use_mock(upassDAO)
fdao_idcard_override = use_mock(idcardDAO)
