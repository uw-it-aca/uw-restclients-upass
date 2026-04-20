# Copyright 2026 UW-IT, University of Washington
# SPDX-License-Identifier: Apache-2.0

from restclients_core.exceptions import DataFailureException
from uw_admin_systems.dao import UPass_DAO, IDCard_DAO

upassDAO = UPass_DAO()
idcardDAO = IDCard_DAO()


def _get_response(dao, url):
    response = dao.getURL(
        url, {"Accept": "application/json", "Connection": "keep-alive"}
    )
    data = (
        response.data.decode("utf-8")
        if isinstance(response.data, bytes)
        else response.data
    )
    if response.status != 200:
        raise DataFailureException(url, response.status, data)
    return data


def get_upass_resource(url):
    return _get_response(upassDAO, url)


def get_idcard_resource(url):
    return _get_response(idcardDAO, url)
