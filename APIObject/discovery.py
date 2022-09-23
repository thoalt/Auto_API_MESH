from APIObject.baseClient import BaseClient
from Config import config as cfg
from Utilities import Utility as utl
from base.APILib import API_lib


class discoveryClient(BaseClient):
    def __init__(self):
        super().__init__()
        self.url = cfg.url_Broadcast
        self.request = API_lib()

    def Create_Discovery_Pload(self, reqID=None):
        pload = cfg.req_discovery
        if reqID is None:
            reqID = utl.random_requestID()

        pload['clientMac'] = cfg.CLIENT_MAC
        pload['authenString'] = utl.md5_encrypt(cfg.STR_ENCRYPT + cfg.CLIENT_MAC, cfg.SALT)
        pload['requestId'] = reqID
        print("*********** PAYLOAD ***************")
        print(pload)
        return pload

    def discovery(self, reqID=None, pload=None):
        if pload is None:
            payload = self.Create_Discovery_Pload(reqID)
        else:
            payload = pload

        response = self.request.post(url=self.url, headers=self.headersCurl, pload=payload)
        return response
