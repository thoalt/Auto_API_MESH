import time
import pytest
from APIObject.reboot import rebootClient
import Config.config as cfg

@pytest.mark.usefixtures("login")
class Test_Reboot():
    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.timeOut = 5
        self.exp = {"code": 8, "msg": "Invalid Action"}
        self.rebootClt = rebootClient()
        self.mac = cfg.CAP_MAC
        self.data = ["ă", "â", "đ", "ê", "ô", "ơ", "ư", "á", "à", "ạ", "ả", "ã",
                    "Ă", "Â", "Đ", "Ê", "Ô", "Ơ", "Ư", "Á", "À", "Ạ", "Ả", "Ã"]

    def test_REBOOT_ACT_7(self):
        time.sleep(self.timeOut)
        resBody_Lst = []
        for item in self.data:
            pload = self.rebootClt.Create_Reboot_Pload(action=item, macList=self.mac)
            resBody = self.rebootClt.reboot(self.cookie, pload=pload).body
            resBody_Lst.append(resBody)

        self.rebootClt.assert_response_list(resBody_Lst,
                                    self.exp['code'],
                                    self.exp['msg'])

