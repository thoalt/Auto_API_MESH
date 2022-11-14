"""
This module is for following API:
    - meshView
    - meshCreate
    - meshChange
"""
import time

from assertpy import soft_assertions

from APIObject.baseClient import BaseClient
from Config import config as cfg
from base.APILib import API_lib
from Utilities import Utility as utl


class MESH_MODE():
    ROUTER = 0
    BRIDGE = 1
    REPEATER = 2

class AUTHEN_MODE():
    OPEN = "OPEN"
    WF5_WPA_PSK = "WPA-PSK"
    WF5_WPA2_PSK = "WPA2-PSK"
    WF5_MIX_MODE = "WPA-PSK/WPA2-PSK Mixed Mode"
    WF6_WPA3_SAE = "WPA3-SAE"
    WF6_MIX_MODE = "WPA2-PSK/WPA3-SAE Mixed Mode"
    WF6_WPA3_OWE = "WPA3-OWE"


class meshViewClient(BaseClient):
    def __init__(self, url=None):
        super().__init__()
        if url != None:
            self.url = url
        else:
            self.url = cfg.url_Agent

        self.request = API_lib()

    def Create_meshView_Pload(self, action=None, reqID=None):
        pload = cfg.req_meshView
        payload = self.set_payload_with_action_reqID(pload=pload, action=action, reqID=reqID)
        return payload

    def meshView(self, cookies=None, pload=None):
        if pload is None:
            payload = self.Create_meshView_Pload()
        else:
            payload = pload

        response = self.request.post(url=self.url, headers=self.headersCurl, cookies=cookies, pload=payload)
        return response

    def assert_meshmode(self, resBody, expectMode=None, loopAvoid=None):
        resultRes = self.get_result(resBody)[0]
        if expectMode is not None:
            self.assert_val(resultRes['meshMode'], expectMode)

        if loopAvoid is not None:
            self.assert_val(str(loopAvoid), str(resultRes['loopAvoidance']))
        else:
            self.assert_val(str(False),str(resultRes['loopAvoidance']))

    # def assert_loopAvoid(self, resBody, expectVal):
    #     loopAvoid = utl.search_nodes_using_json_path(resBody, jsonPath="$..results[*].loopAvoidance")[0]
    #     self.assert_val(loopAvoid, expectVal)

    def assert_repeater(self, resBody, reSSIDName=None, reAuthenMode=None, rePass=None):
        resultRes = self.get_result(resBody)[0]
        with soft_assertions():
            if reSSIDName is not None:
                self.assert_val(resultRes['repeaterSsidName'], reSSIDName)

            if reAuthenMode is not None:
                self.assert_val(resultRes['repeaterAuthenMode'], reAuthenMode)

            if rePass is not None:
                self.assert_val(resultRes['repeaterPassword'], rePass)

class meshCreateClient(BaseClient):
    def __init__(self):
        super().__init__()
        self.url = cfg.url_Agent
        self.request = API_lib()

    def Create_meshCreate_Pload(self, action=None, reqID=None, meshMode=None, ssidName=None, passW=None, addNode=None):
        pload = cfg.req_meshCreate
        payload = self.set_payload_with_action_reqID(pload=pload, action=action, reqID=reqID)

        if meshMode is not None:
            payload.update({'meshMode': meshMode})

        if ssidName is not None:
            payload.update({'ssidName': ssidName})

        if passW is not None:
            payload.update({'password': passW})

        if addNode is not None:
            payload.update({'addNode': addNode})
        return payload


    def Create_meshCreate_Mode_Repeater_Pload(self, payload, ReSsidName=None, ReAutheMode=None, RePass=None):
        if ReSsidName is not None:
            payload.update({'repeaterSsidName': ReSsidName})

        if ReAutheMode is not None:
            payload.update({'repeaterAuthenMode': ReAutheMode})

        if RePass is not None:
            payload.update({'repeaterPassword': RePass})

        return payload


    def Create_meshCreate_Mode_Brigde_Pload(self, payload, loopAvoid=None):
        if loopAvoid is not None:
            payload.update({'loopAvoidance': loopAvoid})

        return payload


    def meshCreate(self, cookies=None, pload=None):
        if pload is None:
            payload = self.Create_meshCreate_Pload()
        else:
            payload = pload

        response = self.request.post(url=self.url, headers=self.headersCurl, cookies=cookies, pload=payload)
        return response

    def Create_Mesh_Network_Default(self, cookies=None):
        pload = self.Create_meshCreate_Pload(meshMode=MESH_MODE.ROUTER, ssidName=cfg.SSID, passW=cfg.PASSWORD, addNode=True)
        response = self.request.post(url=self.url, headers=self.headersCurl, cookies=cookies, pload=pload)
        time.sleep(150)

class meshChangeClient(BaseClient):
    def __init__(self):
        super.__init__()
        self.url = cfg.url_Agent
        self.request = API_lib()

    def Create_meshChange_Pload(self, action=None, reqID=None, meshMode=None, ssidName=None, passW=None, addNode=None):
        pload = cfg.req_meshChange
        payload = self.set_payload_with_action_reqID(pload=pload, action=action, reqID=reqID)

        if meshMode is not None:
            payload.update({'meshMode': meshMode})

        if ssidName is not None:
            payload.update({'ssidName': ssidName})

        if passW is not None:
            payload.update({'password': passW})

        if addNode is not None:
            payload.update({'addNode': addNode})
        return payload

    def Create_meshChange_Mode_Brigde_Pload(self, payload, loopAvoid=None):
        if loopAvoid is not None:
            payload.update({'loopAvoidance': loopAvoid})

        return payload

    def Create_meshChange_Mode_Repeater_Pload(self, payload, ReSsidName=None, ReAutheMode=None, RePass=None):
        if ReSsidName is not None:
            payload.update({'repeaterSsidName': ReSsidName})

        if ReAutheMode is not None:
            payload.update({'repeaterAuthenMode': ReAutheMode})

        if RePass is not None:
            payload.update({'repeaterPassword': RePass})

        return payload

    def meshChange(self, cookies=None, pload=None):
        if pload is None:
            payload = self.Create_meshChange_Pload()
        else:
            payload = pload

        response = self.request.post(url=self.url, headers=self.headersCurl, cookies=cookies, pload=payload)
        return response