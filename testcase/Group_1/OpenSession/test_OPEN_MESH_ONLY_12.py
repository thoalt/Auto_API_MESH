import sys
import time

import pytest
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
    exp = {"code": 0, "msg": "Success"}

    @pytest.mark.skip(reason="This is Manual Testcase")
    def test_OPEN_MESH_ONLY(self):
        for bssid in cfg.BSSIDList_MeshOnly:
            try:
                # Connect to Mesh network via BSSID
                Network = Wifi_lib()
                Network.forget_wifi()
                Network.connect_wifi(ssid=cfg.SSID, auth=cfg.auth, encrypt=cfg.encrypt, passwd=cfg.PASSWORD, bssid=bssid, GUID=cfg.GUID, wifiName=cfg.CARD_WIFI_NAME)
                time.sleep(5)
                bssid_get = Network.get_BSSID_connected(cfg.CARD_WIFI_NAME)

                if bssid_get != bssid:
                    sys.exit()
                print(f"Connect to <{bssid}> Success!")

                # SSH to start Agent
                if Network.check_ping(cfg.IP_ADDR_CAP, count=10):
                    client = SSHClient(hostname=cfg.IP_ADDR_CAP, username=cfg.USER_SSH, password=cfg.PASS_SSH)
                    SSHShell = client.create_shell()
                    SSHSes = SSH_Lib(SSHShell=SSHShell)
                    SSHSes.start_mobile_agent()
                    SSHShell.close()
                else:
                    raise Exception(f"CANNOT PING TO {cfg.IP_ADDR_CAP}")

                # Open session
                self.ClientSes = openssesionClient()
                reqID, res = self.ClientSes.Open_Session()
                resBody = res.body
                self.ClientSes.assert_opensession(resBody,
                                                  self.exp['code'],
                                                    self.exp['msg'])
            except Exception as exc:
                print(exc)

