"""
This module is enable for following APIs:
    - radio2.4GView
    - radio2.4GEdit
    - ssid2.4GView
    - ssid2.4GEdit
"""

from assertpy import assert_that, soft_assertions
from APIObject.baseClient import BaseClient
from Config import config as cfg
from Utilities import Utility as utl
from base.APILib import API_lib


class radio24GViewClient(BaseClient):
    def __init__(self):
        super().__init__()
        self.url = cfg.url_Agent
        self.request = API_lib()

    def Create_radio24GView_Pload(self, action=None, reqID=None):
        pload = cfg.req_radio2GView
        payload = self.set_payload_with_action_reqID(pload=pload, action=action, reqID=reqID)
        return payload

    def radio24GView(self, cookies=None, pload=None):
        if pload is None:
            payload = self.Create_radio24GView_Pload()
        else:
            payload = pload

        response = self.request.post(url=self.url, headers=self.headersCurl, cookies=cookies, pload=payload)
        return response

    def assert_result(self, resBody, enable=None, channel= None, bandW=None):
        with soft_assertions():
            resResult = self.get_result(resBody=resBody)[0]

            if enable is not None:
                assert_that(resResult['enable'], description="ENABLE ERROR").is_equal_to(enable)

            if channel is not None:
                assert_that(resResult['channel'], description="channel ERROR").is_equal_to(channel)

            if bandW is not None:
                assert_that(resResult['bandwidth'], description="bandwidth ERROR").is_equal_to(bandW)

    def assert_result_lst(self, resBodyLst, enableLst=None, channelLst=None, bandWLst=None):
        with soft_assertions():
                for idx, resBody in enumerate(resBodyLst):
                    if enableLst is not None:
                        self.assert_result(resBody=resBody, enable=enableLst[idx])

                    if channelLst is not None:
                        self.assert_result(resBody=resBody, channel=channelLst[idx])

                    if bandWLst is not None:
                        self.assert_result(resBody=resBody, bandW=bandWLst[idx])
