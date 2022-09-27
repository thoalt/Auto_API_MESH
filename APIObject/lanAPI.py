from assertpy import assert_that, soft_assertions
from APIObject.baseClient import BaseClient
from Config import config as cfg
from Utilities import Utility as utl
from base.APILib import API_lib


class LanViewClient(BaseClient):
    def __init__(self):
        super().__init__()
        self.url = cfg.url_Agent
        self.request = API_lib()

    def Create_LanView_Pload(self, action=None, reqID=None):
        pload = cfg.req_lanview
        payload = self.set_payload_with_action_reqID(pload=pload, action=action, reqID=reqID)
        return payload

    def lanView(self, cookies=None, pload=None):
        if pload is None:
            payload = self.Create_LanView_Pload()
        else:
            payload = pload

        response = self.request.post(url=self.url, headers=self.headersCurl, cookies=cookies, pload=payload)
        return response

    def assert_result(self, resBody, ipAddr=None, netMask=None):
        with soft_assertions():
            resResult = self.get_result(resBody=resBody)[0]

            if ipAddr is not None:
                assert_that(resResult['ipAddr'], description="IPADDR ERROR").is_equal_to(ipAddr)

            if netMask is not None:
                assert_that(resResult['subnetMask'], description="NETMASK ERROR").is_equal_to(netMask)


    def assert_result_lst(self, resBody_Lst, ipAddr_Lst=None, netMask_Lst=None):
        with soft_assertions():
            if ipAddr_Lst is not None:
                for idx, resBody in enumerate(resBody_Lst):
                    self.assert_result(resBody, ipAddr=ipAddr_Lst[idx])

            if netMask_Lst is not None:
                for idx, resBody in enumerate(resBody_Lst):
                    self.assert_result(resBody, netMask=netMask_Lst[idx])


class LanEditClient(BaseClient):
    def __init__(self):
        super().__init__()
        self.url = cfg.url_Agent
        self.request = API_lib()

    def Create_LanEdit_Payload(self, action=None, ipAddr=None, netMask=None, reqID=None):
        pload = cfg.req_lanEdit
        payload = self.set_payload_with_action_reqID(pload=pload, action=action, reqID=reqID)

        if ipAddr is not None:
            payload['ipAddr'] = ipAddr
        else:
            payload['ipAddr'] = pload['ipAddr']

        if netMask is not None:
            payload['subnetMask'] = netMask
        else:
            payload['subnetMask'] = pload['subnetMask']

        return payload


    def lanEdit(self, cookies=None, pload=None):
        if pload is None:
            payload = self.Create_LanEdit_Payload()
        else:
            payload = pload

        response = self.request.post(url=self.url, headers=self.headersCurl, cookies=cookies, pload=payload)
        return response
    