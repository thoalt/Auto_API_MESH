from APIObject.baseClient import BaseClient
from Config import config as cfg
from base.APILib import API_lib


class UpdateDatabaseClient(BaseClient):
    def __init__(self):
        super().__init__()
        self.url = cfg.url_Agent
        self.request = API_lib()

    def Create_UpdateDatabase_Pload(self, action=None, reqID=None, status=None, fileName=None, md5sum=None):
        pload = cfg.req_updateDatabase

        payload = self.set_payload_with_action_reqID(pload=pload, action=action, reqID=reqID)

        if status is not None:
            payload['status'] = status

        if fileName is not None:
            payload['fileName'] = fileName

        if md5sum is not None:
            payload['md5sum'] = md5sum

        return payload

    def UpdateDatabase(self, cookies=None, pload=None):
        if pload is None:
            payload = self.Create_UpdateDatabase_Pload()
        else:
            payload = pload

        response = self.request.post(url=self.url, headers=self.headersCurl, cookies=cookies, pload=payload)

        return response
