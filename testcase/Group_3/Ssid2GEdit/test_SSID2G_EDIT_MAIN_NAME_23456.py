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
class Test_ssid2GEdit():
    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.timeOut = 10
        self.exp = {"code": 11, "msg": "Verify Fail"}
        self.ssid2GEditClt = ssid24GEditClient()


        self.ssidIndex = 0
        self.enable = True
        self.ssid = "Test_Wifi_Main_SSID_" + str(random.randint(1, 20000))
        self.authenmode = "password"
        self.password = "0987654321_"

        self.data = ["á1", "à2", "ã3", "ạ4", "ă1", "ắ2", "ằ3", "ặ4", "ẵ5", "â1", "ấ2", "ầ3", "ẫ4", "ậ5", "é1", "è2",
                     "ẽ3", "ẹ4", "ê1", "ế2", "ề3", "ễ4", "ệ5", "ô1", "ố2", "ồ3", "ỗ4", "ộ5", "ơ1", "ớ2", "ờ3",
                     "ỡ4", "ợ5", "ư1", "ứ2", "ừ3", "ữ4", "ự5",
                     "1&", "3'", "4\"", "5\\", " ",
                     "uidwvgNleD1234567890`~!@#$%^*()_1",
                     "uidwvgNleD1234567890-=+{[]}|;:<,2",
                     "uidwvgNleD1234567890.>?/txblaudp3",
                     '  ',
                     '                              ',
                     ]

    def test_ssid2GEdit_RES_1(self):
        resBody_lst = []
        for idx, item in enumerate(self.data):
            if idx % 2 == 0:
                pload = self.ssid2GEditClt.Create_ssid24GEdit_Pload(ssidIdx=self.ssidIndex,
                                                                   enable=self.enable,
                                                                   ssid=item,
                                                                   autMode="password",
                                                                   passW=self.password + str(random.randint(1, 20000)))
            else:
                pload = self.ssid2GEditClt.Create_ssid24GEdit_Pload(ssidIdx=self.ssidIndex,
                                                                   enable=self.enable,
                                                                   ssid=item,
                                                                   autMode="open",
                                                                   passW=self.password + str(random.randint(1, 20000)))

            resBody = self.ssid2GEditClt.ssid24GEdit(self.cookie, pload=pload).body
            resBody_lst.append(resBody)
            time.sleep(1)

        self.ssid2GEditClt.assert_response_list(resBody_lst,
                                                   self.exp['code'],
                                                   self.exp['msg'])


