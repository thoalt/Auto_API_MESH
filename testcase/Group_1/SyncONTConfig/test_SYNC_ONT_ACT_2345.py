import time
import pytest
from APIObject.syncONTConfig import syncONTConfigClient
from pages.MeshPage import MeshPage

@pytest.mark.usefixtures("login")
class Test_Sync_ONT():
    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.timeOut = 2
        self.exp = {"code": 8, "msg": "Invalid Action"}
        self.data = ['syncONTConfig1', 'syncONTConfi', 'SyncONTConfig', 'syncOntConfig', 'SYNCONTCONFIG' ,'syncontconfig' ,'',
                     'SyncONTConfig122144124141241241241']

        self.syncONTClt = syncONTConfigClient()


    def test_SYNC_ONT_ACT_1(self):
        resBody_lst = []
        for item in self.data:
            time.sleep(self.timeOut)
            pload = self.syncONTClt.Create_syncONTConfig_Pload(action=item)
            resBody = self.syncONTClt.syncONTConfig(self.cookie, pload=pload).body
            resBody_lst.append(resBody)
        self.syncONTClt.assert_response_list(resBody_lst,
                                            self.exp['code'],
                                            self.exp['msg'])
