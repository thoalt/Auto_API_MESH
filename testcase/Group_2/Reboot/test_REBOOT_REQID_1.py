import time
import pytest
from APIObject.openssesion import openssesionClient
from APIObject.login import LoginClient
from APIObject.reboot import rebootClient
import Config.config as cfg
from base.SSHLib import SSH_Lib


@pytest.mark.usefixtures("create_shell")
class Test_Reboot():
    sesID, salt = "", ""
    reqID = 0

    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.exp = {"code": 0, "msg": "Success", "action": "reboot"}
        self.timeOut = 5
        self.rebootClt = rebootClient()
        self.mac = cfg.CAP_MAC
        self.data = [0, 1, 2147483646, 2147483647]


        SSHSes = SSH_Lib(SSHShell=self.SSHShell)
        SSHSes.start_mobile_agent()

    def test_REBOOT_REQID_1(self):
        time.sleep(self.timeOut)
        resBody_Lst = []
        for reqID in self.data:
            # Open Session
            self.ClientSes = openssesionClient()
            self.cookie = self.ClientSes.Open_Sesion_And_Get_Cookie()

            # Login
            self.LoginClt = LoginClient()
            self.LoginClt.login(self.cookie)

            #Reboot
            self.rebootClt = rebootClient()
            pload = self.rebootClt.Create_Reboot_Pload(reqID=reqID, macList=self.mac)
            resBody = self.rebootClt.reboot(self.cookie, pload=pload).body
            resBody_Lst.append(resBody)
            time.sleep(180)

        self.rebootClt.assert_response_list(resBody_Lst,
                                    self.exp['code'],
                                    self.exp['msg'],
                                    self.exp['action'])

