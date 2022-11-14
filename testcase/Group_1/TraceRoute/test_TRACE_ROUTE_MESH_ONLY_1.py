import sys
import time
import pytest
from sshaolin.client import SSHClient

from APIObject.login import LoginClient
from APIObject.openssesion import openssesionClient
from APIObject.traceroute import TracerouteClient
from Config import config as cfg
from base.SSHLib import SSH_Lib
from base.WiFiLib import Wifi_lib


class Test_TraceRoute():
    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.timeOut = 2
        self.exp = {"code": 0, "msg": "Success", "action": "traceroute", "traceCode": 3}
        self.host = "8.8.8.8"
        self.traceClt = TracerouteClient()
    def test_TRACE_ROUTE_MESH_ONLY_1(self):
        resBody_lst = []
        for bssid in cfg.BSSIDList_MeshOnly:
            # Connect to Mesh network via BSSID
            Network = Wifi_lib()
            Network.connect_wifi(ssid=cfg.SSID, auth=cfg.auth, encrypt=cfg.encrypt, passwd=cfg.PASSWORD,
                                 bssid=bssid, GUID=cfg.GUID, wifiName=cfg.CARD_WIFI_NAME)
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

        # Check
            ClientSes = openssesionClient()
            cookie = ClientSes.Open_Sesion_And_Get_Cookie()

            LoginClt = LoginClient()
            LoginClt.login(cookie)


            time.sleep(self.timeOut)
            pload = self.traceClt.Create_TraceRoute_Pload(host=self.host)
            resBody = self.traceClt.traceroute(cookies=cookie, pload=pload).body
            resBody_lst.append(resBody)
            time.sleep(5)

        self.traceClt.assert_response_list(resBody_lst,
                                        self.exp['code'],
                                        self.exp['msg'],
                                        self.exp['action'])
        self.traceClt.assert_trace_result_lst(resBody_lst, traceCode=self.exp['traceCode'])


