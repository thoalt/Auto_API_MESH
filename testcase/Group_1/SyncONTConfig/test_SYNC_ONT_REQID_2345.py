import time
import pytest
from APIObject.syncONTConfig import syncONTConfigClient
from pages.MeshPage import MeshPage

@pytest.mark.usefixtures("login")
class Test_Sync_ONT():
    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.timeOut = 2
        self.exp = {"code": 11, "msg": "Verify Fail"}
        self.data = ['', 'true', 'false', 'TRUE', 'false', "true", "false", 'Enable', 'Disable', 0, 1]
        self.syncONTClt = syncONTConfigClient()


    def test_SYNC_ONT_ACT_1(self):
        resBody_lst = []
        for item in self.data:
            time.sleep(self.timeOut)
            pload = self.syncONTClt.Create_syncONTConfig_Pload(enable=item)
            resBody = self.syncONTClt.syncONTConfig(self.cookie, pload=pload).body
            resBody_lst.append(resBody)
        self.syncONTClt.assert_response_list(resBody_lst,
                                            self.exp['code'],
                                            self.exp['msg'])
