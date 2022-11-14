import time
import pytest
from APIObject.wifi5GAPI import ssid5GEditClient

@pytest.mark.usefixtures("login")
class Test_ssid5GEdit():
    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.timeOut = 10
        self.exp = {"code":0 , "msg": "Success", "action": "ssid5GEdit"}
        self.ssid5GEditClt = ssid5GEditClient()
        self.ssidIndex = 1
        self.enable = False
        self.ssid = "Test_Wifi"
        self.authenmode = "ASE"
        self.password = "1234567890"

    @pytest.mark.success
    def test_ssid5GEdit_RES_1(self):
        time.sleep(self.timeOut)
        pload = self.ssid5GEditClt.Create_ssid5GEdit_Pload(ssidIdx=self.ssidIndex,
                                                             enable=self.enable,
                                                             ssid = self.ssid,
                                                             autMode=self.authenmode,
                                                             passW=self.password)

        resBody = self.ssid5GEditClt.ssid5GEdit(self.cookie, pload=pload).body
        self.ssid5GEditClt.assert_response(resBody,
                                        self.exp['code'],
                                        self.exp['msg'],
                                        self.exp['action'])

