from APIObject.baseClient import BaseClient
from Config import config as cfg
from base.APILib import API_lib


class UpdateFWClient(BaseClient):
    def __init__(self):
        super().__init__()
        self.url = cfg.url_Agent
        self.request = API_lib()

    def Create_UpdateFW_Pload(self, action=None, reqID=None, macList=None, fileName=None, md5sum=None):
        pload = cfg.req_upgradeFirmware

        payload = self.set_payload_with_action_reqID(pload=pload, action=action, reqID=reqID)

        if macList is not None:
            payload['macList'] = macList

        if fileName is not None:
            payload['fileName'] = fileName

        if md5sum is not None:
            payload['md5sum'] = md5sum

        return payload

    def UpdateFirmware(self, cookies=None, pload=None):
        if pload is None:
            payload = self.Create_UpdateFW_Pload()
        else:
            payload = pload

        response = self.request.post(url=self.url, headers=self.headersCurl, cookies=cookies, pload=payload)

        return response
