import time

from assertpy import assert_that

from APIObject.baseClient import BaseClient
from Config import config as cfg
from Utilities import Utility as utl
from base.APILib import API_lib


class resetClient(BaseClient):
    def __init__(self):
        super().__init__()
        self.url = cfg.url_Agent
        self.request = API_lib()

    def Create_reset_Pload(self, action=None, macList=None, reqID=None):
        pload = cfg.req_reset

        payload = self.set_payload_with_action_reqID(pload=pload, action=action, reqID=reqID)
        if macList is not None:
            payload['macList'] = macList
        return payload

    def reset(self, cookies=None, pload=None):
        if pload is None:
            payload = self.Create_reset_Pload()
        else:
            payload = pload

        response = self.request.post(url=self.url, headers=self.headersCurl, cookies=cookies, pload=payload)

        return response

    def reset_CAP(self, cookies=None):
        payload = self.Create_reset_Pload(macList=cfg.CAP_MAC)
        response = self.request.post(url=self.url, headers=self.headersCurl, cookies=cookies, pload=payload)
        time.sleep(240)
        return response