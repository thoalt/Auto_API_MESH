import random
import time
import pytest

from APIObject.login import LoginClient
from APIObject.meshAPI import meshCreateClient, meshViewClient, MESH_MODE, AUTHEN_MODE
from APIObject.openssesion import openssesionClient
from APIObject.wifi5GAPI import ssid5GViewClient

from APIObject.reset import resetClient
from base.SerialLib import Serial_Lib
from base.WiFiLib import Wifi_lib
from pages.LoginPage import LoginPage
from pages.SettingWirelessPage import WirelessSSDIPage
from Config import config as cfg
from Utilities import Utility as utl

@pytest.mark.usefixtures("login")
class Test_Mesh_Create():
    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.timeOut = 10
        self.exp = {"code": 0, "msg": "Success"}
        self.meshViewClt = meshViewClient()


    # @pytest.mark.skip(reason="This is Manual Testcase")
    def test_MESH_CREATE_RES_1(self):
        # View Mesh
        resBody = self.meshViewClt.meshView(self.cookie).body

