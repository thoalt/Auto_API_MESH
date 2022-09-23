from assertpy import assert_that, soft_assertions
from APIObject.baseClient import BaseClient
from Config import config as cfg
from Utilities import Utility as utl
from base.APILib import API_lib


class syncONTConfigClient(BaseClient):
    def __init__(self):
        super().__init__()
        self.url = cfg.url_Agent
        self.request = API_lib()

    def Create_syncONTConfig_Pload(self, action=None, reqID=None):
        pload = cfg.req_syncONTConfig
        payload = self.set_payload_with_action_reqID(pload=pload, action=action, reqID=reqID)
        return payload

    def syncONTConfig(self, cookies=None, pload=None):
        if pload is None:
            payload = self.Create_syncONTConfig_Pload()
        else:
            payload = pload

        response = self.request.post(url=self.url, headers=self.headersCurl, cookies=cookies, pload=payload)
        return response
