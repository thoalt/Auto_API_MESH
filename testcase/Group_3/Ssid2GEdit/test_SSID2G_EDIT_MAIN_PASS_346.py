import random
import time
import pytest
from assertpy import soft_assertions
from sshaolin.client import SSHClient

from APIObject.wifi24GAPI import ssid24GEditClient
from pages.SettingWirelessPage import WirelessSSDIPage, WirelessGuestSSDIPage

from base.SSHLib import SSH_Lib
from Config import config as cfg


@pytest.mark.usefixtures("login")
class Test_ssid24GEdit():
    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.timeOut = 10
        self.exp = {"code": 11, "msg": "Verify Fail"}
        self.ssid24GEditClt = ssid24GEditClient()


        self.ssidIndex = 0
        self.enable = True
        self.ssid = "Test_Wifi_Main_SSID_" + str(random.randint(1, 20000))
        self.authenmode = "password"
        self.password = "0987654321_"

        self.data = ["1234&abcd",
                    "1234'abcd",
                    "1234\"abcd",
                    "1234\\abcd",
                     "abcABed",
                     "5368231",
                     "%@#)(*_",
                     "?~!<,./",
                     "`123gj%",
                     " ",
                     '  ',
                     '                              '
                     ]

    def test_ssid24GEdit_RES_1(self):
        resBody_lst = []
        for idx, item in enumerate(self.data):
            pload = self.ssid24GEditClt.Create_ssid24GEdit_Pload(ssidIdx=self.ssidIndex,
                                                               enable=self.enable,
                                                               ssid=self.ssid + str(random.randint(1, 20000)),
                                                               autMode="password",
                                                               passW=item)


            resBody = self.ssid24GEditClt.ssid24GEdit(self.cookie, pload=pload).body
            resBody_lst.append(resBody)
            time.sleep(1)

        self.ssid24GEditClt.assert_response_list(resBody_lst,
                                                   self.exp['code'],
                                                   self.exp['msg'])


