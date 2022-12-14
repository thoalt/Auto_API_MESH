import random
import time
import pytest
from sshaolin.client import SSHClient

from APIObject.login import LoginClient
from APIObject.meshAPI import meshCreateClient, meshViewClient, MESH_MODE, AUTHEN_MODE
from APIObject.openssesion import openssesionClient
from APIObject.wifi5GAPI import ssid5GViewClient

from APIObject.reset import resetClient
from base.SSHLib import SSH_Lib
from base.SerialLib import Serial_Lib
from base.WiFiLib import Wifi_lib
from Utilities import Utility as utl
from Config import config as cfg

@pytest.mark.usefixtures("login_without_create_mesh")
class Test_Mesh_Create():

    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.timeOut = 10
        self.exp = {"code": 0, "msg": "Success"}
        self.meshCreateClt = meshCreateClient()
        self.meshViewClt = meshViewClient()
        self.ssidViewClt = ssid5GViewClient()
        self.resetClt = resetClient()
        self.serialClt = Serial_Lib()
        self.wifiClt = Wifi_lib()

        self.mode = MESH_MODE.REPEATER
        self.REAUTH = AUTHEN_MODE.WF5_MIX_MODE

        self.ssidName = "ThoaTest_" + str(random.randint(1, 2000))
        self.password = "1234567890_" + str(random.randint(1, 200))

        self.ssidNameLst = ["e", "5", "%", "`", "t!", "gh", "3#",
                            "test@hec", " wireless@hec", "wireless@hec ", "wireless@ hec", "wireless@  hec",
                            "wireless@ test hec",
                            "uidwvgNleD1234567890`~!@#$%^*()_",
                            "uidwvgNleD1234567890-=+{[]}|;:<",
                            "uidwvgNleD1234567890.>?/txblaudp"]
        self.passLst = ["test@hec",
                        " wireless@hec",
                        "wireless@hec ",
                        "wireless@ hec",
                        "wireless@  hec",
                        "wireless@ test hec",
                        "uidwvgNleD1234567890`~!@#$%^*()_uidwvgNleD1234567890`~!@#$%^*()",
                        "uidwvgNleD1234567890-=+{[]}|;:<,uidwvgNleD1234567890-=+{[]}|;:<",
                        "uidwvgNleD1234567890.>?/txblaudpuidwvgNleD1234567890.>?/txblaud",
                        "test@hec",
                        " wireless@hec",
                        "wireless@hec ",
                        "wireless@ hec",
                        "wireless@  hec",
                        "wireless@ test hec",
                        "uidwvgNleD1234567890`~!@#$%^*()_uidwvgNleD1234567890`~!@#$%^*()"
                        ]
        modeMesh = self.serialClt.Get_Mode_Mesh()
        if modeMesh != "FACTORY":
            self.serialClt.Reset_Factory()

    @pytest.mark.skip(reason="This is Manual Testcase")
    def test_MESH_CREATE_RES_1(self):
        numTC = len(self.ssidNameLst)
        ploadLst = []
        for idx in range(numTC):
            pload = self.meshCreateClt.Create_meshCreate_Pload(meshMode=self.mode,
                                                               ssidName=self.ssidName,
                                                               passW=self.password)

            pload = self.meshCreateClt.Create_meshCreate_Mode_Repeater_Pload(payload=pload,
                                                                             ReSsidName=self.ssidNameLst[idx],
                                                                             ReAutheMode=self.REAUTH,
                                                                             RePass=self.passLst[idx])

            ploadLst.append(pload)

        for pload in ploadLst:
            ClientSes = openssesionClient()
            cookieAfter = ClientSes.Open_Sesion_And_Get_Cookie()
            LoginClt = LoginClient()
            LoginClt.login(cookieAfter)

            # Create Mesh
            resBody = self.meshCreateClt.meshCreate(cookieAfter, pload=pload).body
            time.sleep(180)

            # View Mesh
            resBody = self.meshViewClt.meshView(cookieAfter).body
            self.meshViewClt.assert_meshmode(resBody, expectMode=self.mode)
            self.meshViewClt.assert_repeater(resBody, reSSIDName=self.ssidNameLst[idx],
                                             reAuthenMode=self.REAUTH,
                                             rePass=self.passLst[idx])
            time.sleep(2)
            # View SSID
            resBody = self.ssidViewClt.ssid5GView(cookieAfter).body
            self.ssidViewClt.assert_ssid5GView_result(resBody, ssidName=self.ssidName, passWord=self.password)

            # # Get SSID in GUI
            # self.ssidp.navigation_to_SSID_page()
            # gui_SSID = self.ssidp.Get_SSID_Info()
            # print(gui_SSID)
            # self.ssid5GEditClt.assert_val(self.ssidNameLst[idx], gui_SSID.ssidName)
            # self.ssid5GEditClt.assert_val(self.passLst[idx], gui_SSID.password)
            #
            # # GET SSID in driver
            # client = SSHClient(hostname=cfg.IP_ADDR_CAP, username=cfg.USER_SSH, password=cfg.PASS_SSH, timeout=300)
            # SSHShell = client.create_shell()
            # self.session = SSH_Lib(SSHShell=SSHShell)
            #
            # driver_SSID_5G = self.session.get_ssid_name(cfg.WIFI_INT_5G)
            # print(driver_SSID_5G)
            # self.ssid5GEditClt.assert_val(self.ssidNameLst[idx], driver_SSID_5G)

            # Tear down
            self.serialClt.Reset_Factory()
