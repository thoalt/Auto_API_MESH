import copy
import json

from APIObject.baseClient import BaseClient
from Config import config as cfg
from Utilities import Utility as utl
from base.APILib import API_lib
from base.UDPLib import UDP_Lib


class discoveryClient(BaseClient):
    def __init__(self):
        super().__init__()
        self.url = cfg.url_Broadcast
        self.Client = UDP_Lib()

    def Create_Discovery_Pload(self, action=None, clientMac=None, authen=None, reqID=None):
        ploadOrg = cfg.req_discovery
        pload = copy.deepcopy(ploadOrg)

        if action is not None:
            pload['action'] = action
        else:
            pload['action'] = ploadOrg['action']

        if clientMac is not None:
            pload['clientMac'] = clientMac
        else:
            pload['clientMac'] = cfg.CLIENT_MAC

        if authen is not None:
            pload['authenString'] = authen
        else:
            pload['authenString'] = utl.md5_encrypt(cfg.STR_ENCRYPT + pload['clientMac'], cfg.SALT)

        if reqID is None:
            pload['requestId'] = utl.random_requestID()
        elif reqID == "Empty":
            pload['requestId'] = None
        else:
            pload['requestId'] = reqID

        print("\n ****************** DISCOVERY REQUEST *****************")
        print(json.dumps(pload, indent=4))
        return pload

    def discovery(self, reqID=None, pload=None):
        if pload is None:
            payload = self.Create_Discovery_Pload(reqID)
        else:
            payload = pload
        #print(payload)
        bytesPload = bytes(json.dumps(payload), "utf-8")
        #print(bytesPload)
        response = self.Client.Send_To(byteToSend=bytesPload)
        print("*****************RESPONSE ************")
        print(response)
        return response
