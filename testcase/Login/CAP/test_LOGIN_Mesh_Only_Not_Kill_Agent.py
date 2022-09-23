import time
from sshaolin.client import SSHClient
from base.SSHLib import SSH_Lib
from base.WiFiLib import Wifi_lib
from APIObject.openssesion import openssesionClient
from APIObject.login import LoginClient
from APIObject.speedtest import SpeedTestClient
from Config import config as cfg


class Test_SpeedTest():
    sesID, salt = "", ""
    reqID = 0
    timeOut = 2
    exp = {"code": 0, "msg": "Success", "action": "login"}

    def test_OPEN_MESH_ONLY(self):
        for item in cfg.BSSIDList_MeshOnly:
            try:
                # Connect to Mesh network via BSSID
                Network = Wifi_lib()
                Network.connect_wifi(ssid=cfg.SSID, auth=cfg.auth, encrypt=cfg.encrypt, passwd=cfg.PASSWORD, bssid=item, GUID=cfg.GUID)

                time.sleep(10)
                print(f"Connect to <{item}> Success!")

                # Open session
                ClientSes = openssesionClient()
                cookie = ClientSes.Open_Sesion_And_Get_Cookie()

                LoginClt = LoginClient()
                resBody = LoginClt.login(cookie).body
                LoginClt.assert_login(resBody,
                                           self.exp['code'],
                                           self.exp['msg'],
                                           self.exp['action'])
            except Exception as exc:
                print(exc)

