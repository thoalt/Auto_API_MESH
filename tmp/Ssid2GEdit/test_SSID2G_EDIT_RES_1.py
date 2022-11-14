import time
import pytest
from APIObject.wifi24GAPI import ssid24GEditClient

@pytest.mark.usefixtures("login")
class Test_ssid24GEdit():
    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.timeOut = 10
        self.exp = {"code":0 , "msg": "Success", "action": "ssid2.4GEdit"}
        self.ssid24GEditClt = ssid24GEditClient()
        self.ssidIndex = 1
        self.enable = True
        self.ssid = "Test_Wifi"
        self.authenmode = "ASE"
        self.password = "1234567890"

    @pytest.mark.success
    def test_ssid24GEdit_RES_1(self):
        time.sleep(self.timeOut)
        pload = self.ssid24GEditClt.Create_ssid24GEdit_Pload(ssidIdx=self.ssidIndex,
                                                             enable=self.enable,
                                                             ssid = self.ssid,
                                                             autMode=self.authenmode,
                                                             passW=self.password)

        resBody = self.ssid24GEditClt.ssid24GEdit(self.cookie, pload=pload).body
        self.ssid24GEditClt.assert_response(resBody,
                                        self.exp['code'],
                                        self.exp['msg'],
                                        self.exp['action'])

