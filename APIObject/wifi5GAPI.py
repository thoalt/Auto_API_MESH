"""
This module is enable for following APIs:
    - radio5GView
    - radio5GEdit
    - ssid5GView
    - ssid5GEdit
"""
from assertpy import assert_that, soft_assertions
from APIObject.baseClient import BaseClient
from Config import config as cfg
from base.APILib import API_lib

class CHANNEL_API():
    C_AUTO = 0
    C_36 = 36
    C_40 = 40
    C_44 = 44
    C_48 = 48
    C_52 = 52
    C_56 = 56
    C_60 = 60
    C_64 = 64
    C_100 = 100
    C_104 = 104
    C_112 = 112
    C_116 = 116
    C_120 = 120
    C_124 = 124
    C_128 = 128
    C_132 = 132
    C_136 = 136
    C_140 = 140
    C_144 = 144
    C_149 = 149
    C_153 = 153
    C_157 = 157
    C_161 = 161
    C_165 = 165

class BAND_WIDTH_API():
    B_20 = 0 # "20MHz"
    B_40 = 1 # "40MHz"
    B_80 = 3 # "80MHz"
    B_160 = 4 # "160MHz

class radio5GViewClient(BaseClient):
    def __init__(self):
        super().__init__()
        self.url = cfg.url_Agent
        self.request = API_lib()

    def Create_radio5GView_Pload(self, action=None, reqID=None):
        pload = cfg.req_radio5GView
        payload = self.set_payload_with_action_reqID(pload=pload, action=action, reqID=reqID)
        return payload

    def radio5GView(self, cookies=None, pload=None):
        if pload is None:
            payload = self.Create_radio5GView_Pload()
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


class radio5GEditClient(BaseClient):
    def __init__(self):
        super().__init__()
        self.url = cfg.url_Agent
        self.request = API_lib()

    def Create_Radio5GEdit_Pload(self, action=None, reqID=None, channel=None, bandW=None):
        pload = cfg.req_radio5GEdit
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

    def radio5GEdit(self, cookies=None, pload=None):
        if pload is None:
            payload = self.Create_Radio5GEdit_Pload()
        else:
            payload = pload
        response = self.request.post(url=self.url, headers=self.headersCurl, cookies=cookies, pload=payload)
        return response


class ssid5GViewClient(BaseClient):
    def __init__(self, url=None):
        super().__init__()
        if url != None:
            self.url = url
        else:
            self.url = cfg.url_Agent

        self.request = API_lib()

    def Create_ssid5GView_Pload(self, action=None, reqID=None):
        pload = cfg.req_ssid5GView
        payload = self.set_payload_with_action_reqID(pload=pload, action=action, reqID=reqID)
        return payload

    def ssid5GView(self, cookies=None, pload=None):
        if pload is None:
            payload = self.Create_ssid5GView_Pload()
        else:
            payload = pload

        response = self.request.post(url=self.url, headers=self.headersCurl, cookies=cookies, pload=payload)
        return response

    def assert_ssid5GView_result(self, resBody, ssidName=None, passWord=None):
        result = self.get_result(resBody)[0]
        with soft_assertions():
            assert_that(result['ssidIndex'], description="SSID Index").is_equal_to(0)
            assert_that(result['enable'], description="Enable").is_equal_to(True)
            assert_that(result['ssidName'], description="SSID Name").is_equal_to(ssidName)
            assert_that(result['authenMode'], description="AUTHEN MODE").is_equal_to("password")
            assert_that(result['password'], description="PASSWORD ").is_equal_to(passWord)


class ssid5GEditClient(BaseClient):
    def __init__(self):
        super().__init__()
        self.url = cfg.url_Agent
        self.request = API_lib()

    def Create_ssid5GEdit_Pload(self, action=None, reqID=None,
                                ssidIdx=None, enable=None, ssid=None, autMode=None, passW=None):
        pload = cfg.req_ssid5GEdit
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

    def ssid5GEdit(self, cookies=None, pload=None):
        if pload is None:
            payload = self.Create_ssid5GEdit_Pload()
        else:
            payload = pload

        response = self.request.post(url=self.url, headers=self.headersCurl, cookies=cookies, pload=payload)
        return response
