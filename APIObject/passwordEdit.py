from APIObject.baseClient import BaseClient
from Config import config as cfg
from base.APILib import API_lib


class passwordEditClient(BaseClient):
    def __init__(self):
        super().__init__()
        self.url = cfg.url_Agent
        self.request = API_lib()

    def Create_passwordEdit_Pload(self, action=None, reqID=None, userName=None, password=None):
        pload = cfg.req_passwordEdit
        payload = self.set_payload_with_action_reqID(pload=pload, action=action, reqID=reqID)

        if userName: payload.update({'username': userName})
        if password: payload.update({'password': password})

        return payload

    def passwordEdit(self, cookies=None, pload=None):
        if pload is None:
            payload = self.Create_passwordEdit_Pload()
        else:
            payload = pload

        response = self.request.post(url=self.url, headers=self.headersCurl, cookies=cookies, pload=payload)
        return response
