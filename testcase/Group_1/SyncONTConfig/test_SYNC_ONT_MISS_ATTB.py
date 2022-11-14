import time
import pytest
from APIObject.syncONTConfig import syncONTConfigClient
from pages.MeshPage import MeshPage

@pytest.mark.usefixtures("login")
class Test_Sync_ONT():
    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.timeOut = 2
        self.exp = {"code": 10, "msg": "Miss Attribute"}
        self.syncONTClt = syncONTConfigClient()
        pload = self.syncONTClt.Create_syncONTConfig_Pload()
        self.data = [self.syncONTClt.Remove_Key_In_Pload(pload, 'action')]


    def test_SYNC_ONT_ACT_1(self):
        resBody_lst = []
        for item in self.data:
            resBody = self.syncONTClt.syncONTConfig(self.cookie, pload=item).body
            resBody_lst.append(resBody)
        self.syncONTClt.assert_response_list(resBody_lst,
                                            self.exp['code'],
                                            self.exp['msg'])
