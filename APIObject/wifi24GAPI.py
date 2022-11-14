"""
This module is enable for following APIs:
    - radio2.4GView
    - radio2.4GEdit
    - ssid2.4GView
    - ssid2.4GEdit
"""
from dataclasses import dataclass

from assertpy import assert_that, soft_assertions
from APIObject.baseClient import BaseClient
from Config import config as cfg
from base.APILib import API_lib

class CHANNEL_API():
    C_AUTO = "auto"
    C_1 = "1"
    C_2 = "2"
    C_3 = "3"
    C_4 = "4"
    C_5 = "5"
    C_6 = "6"
    C_7 = "7"
    C_8 = "8"
    C_9 = "9"
    C_10 = "10"
    C_11 = "11"

class BAND_WITH_API():
    B_20 = "20MHz"
    B_40 = "40MHz"
    B_20_40 = "20/40MHz"
    B_80 = "80MHz"


@dataclass
class RadioInfo:
    status: bool
    standard: str
    channel: str
    bandwith: str
    power: int
    countryCode: str

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

    def assert_result(self, resBody, enable=None, channel=None, bandW=None):
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


class radio24GEditClient(BaseClient):
    def __init__(self):
        super().__init__()
        self.url = cfg.url_Agent
        self.request = API_lib()

    def Create_radio24GEdit_Pload(self, action=None, reqID=None, channel=None, bandW=None):
        pload = cfg.req_radio2GEdit
        payload = self.set_payload_with_action_reqID(pload=pload, action=action, reqID=reqID)

        if channel is not None:
            payload['channel'] = channel
        else:
            payload['channel'] = pload['channel']

        if bandW is not None:
            payload['bandwidth'] = bandW
        else:
            payload['bandwidth'] = pload['bandwidth']

        return payload

    def radio24GEdit(self, cookies=None, pload=None):
        if pload is None:
            payload = self.Create_radio24GEdit_Pload()
        else:
            payload = pload

        response = self.request.post(url=self.url, headers=self.headersCurl, cookies=cookies, pload=payload)
        return response


class ssid24GViewClient(BaseClient):
    def __init__(self):
        super().__init__()
        self.url = cfg.url_Agent
        self.request = API_lib()

    def Create_ssid24GView_Pload(self, action=None, reqID=None):
        pload = cfg.req_ssid2GView
        payload = self.set_payload_with_action_reqID(pload=pload, action=action, reqID=reqID)
        return payload

    def ssid24GView(self, cookies=None, pload=None):
        if pload is None:
            payload = self.Create_ssid24GView_Pload()
        else:
            payload = pload

        response = self.request.post(url=self.url, headers=self.headersCurl, cookies=cookies, pload=payload)
        return response

    def assert_result(self, resBody, ssidIndex=None, enable=None, ssidName=None, authenMode=None, password=None):
        with soft_assertions():
            resResult = self.get_result(resBody=resBody)[0]

        if ssidIndex is not None:
            assert_that(resResult['ssidIndex'], description="SSID INDEX ERROR").is_equal_to(ssidIndex)

        if enable is not None:
            assert_that(resResult['enable'], description="ENABLE ERROR").is_equal_to(enable)

        if ssidName is not None:
            assert_that(resResult['ssidName'], description="SSID NAME ERROR").is_equal_to(ssidName)

        if authenMode is not None:
            assert_that(resResult['authenMode'], description="AUTHEN MODE ERROR").is_equal_to(authenMode)

        if password is not None:
            assert_that(resResult['password'], description="PASSWORD ERROR").is_equal_to(password)

    def assert_result_lst(self, resBodyLst, ssidIndex=None, enable=None, ssidName=None, authenMode=None,
                          password=None):
        with soft_assertions():
            for idx, resBody in enumerate(resBodyLst):
                if ssidIndex is not None:
                    self.assert_result(resBody=resBody, ssidIndex=ssidIndex[idx])

                if enable is not None:
                    self.assert_result(resBody=resBody, enable=enable[idx])

                if ssidName is not None:
                    self.assert_result(resBody=resBody, ssidName=ssidName[idx])

                if authenMode is not None:
                    self.assert_result(resBody=resBody, enable=authenMode[idx])

                if password is not None:
                    self.assert_result(resBody=resBody, ssidName=password[idx])


class ssid24GEditClient(BaseClient):
    def __init__(self):
        super().__init__()
        self.url = cfg.url_Agent
        self.request = API_lib()

    def Create_ssid24GEdit_Pload(self, action=None, reqID=None,
                                 ssidIdx=None, enable=None, ssid=None, autMode=None, passW=None):
        pload = cfg.req_ssid2GEdit
        payload = self.set_payload_with_action_reqID(pload=pload, action=action, reqID=reqID)

        if ssidIdx is not None:
            payload['ssidIndex'] = ssidIdx

        if enable is not None:
            payload['enable'] = enable

        if ssid is not None:
            payload['ssidName'] = ssid

        if autMode is not None:
            payload['authenMode'] = autMode

        if passW is not None:
            payload['password'] = passW

        return payload

    def ssid24GEdit(self, cookies=None, pload=None):
        if pload is None:
            payload = self.Create_ssid24GEdit_Pload()
        else:
            payload = pload

        response = self.request.post(url=self.url, headers=self.headersCurl, cookies=cookies, pload=payload)
        return response
