import time
import pytest
from APIObject.reboot import rebootClient
import Config.config as cfg

@pytest.mark.usefixtures("login")
class Test_Reboot():
    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.timeOut = 5
        self.exp = {"code": 10, "msg": "Miss Attribute"}
        self.rebootClt = rebootClient()
        self.mac = cfg.CAP_MAC
        pload = self.rebootClt.Create_Reboot_Pload(macList=self.mac)
        self.data = [self.rebootClt.Remove_Key_In_Pload(pload, 'action'),
                     self.rebootClt.Remove_Key_In_Pload(pload, 'macList')]


    def test_REBOOT_ACT_2(self):
        time.sleep(self.timeOut)
        resBody_Lst = []
        for item in self.data:
            resBody = self.rebootClt.reboot(self.cookie, pload=item).body
            resBody_Lst.append(resBody)

        self.rebootClt.assert_response_list(resBody_Lst,
                                    self.exp['code'],
                                    self.exp['msg'])

