from assertpy import assert_that

from APIObject.baseClient import BaseClient
from Config import config as cfg
from base.APILib import API_lib


class restoreConfigClient(BaseClient):
    def __init__(self):
        super().__init__()
        self.url = cfg.url_Agent
        self.request = API_lib()

    def Create_restoreConfig_Pload(self, action=None, reqID=None, fileName=None, md5sum=None):
        pload = cfg.req_restoreConfig

        payload = self.set_payload_with_action_reqID(pload=pload, action=action, reqID=reqID)

        if fileName is not None:
            payload['fileName'] = fileName

        if md5sum is not None:
            payload['md5sum'] = md5sum

        return payload

    def restoreConfig(self, cookies=None, pload=None):
        if pload is None:
            payload = self.Create_restoreConfig_Pload()
        else:
            payload = pload

        response = self.request.post(url=self.url, headers=self.headersCurl, cookies=cookies, pload=payload)

        return response


class backupConfigClient(BaseClient):
    def __init__(self):
        super().__init__()
        self.url = cfg.url_Agent
        self.request = API_lib()

    def Create_backupConfig_Pload(self, action=None, reqID=None):
        pload = cfg.req_backupConfig

        payload = self.set_payload_with_action_reqID(pload=pload, action=action, reqID=reqID)
        return payload

    def backupConfig(self, cookies=None, pload=None):
        if pload is None:
            payload = self.Create_backupConfig_Pload()
        else:
            payload = pload

        response = self.request.post(url=self.url, headers=self.headersCurl, cookies=cookies, pload=payload)
        return response