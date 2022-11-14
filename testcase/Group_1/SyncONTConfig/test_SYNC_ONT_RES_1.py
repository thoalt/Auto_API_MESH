import time
import pytest
from APIObject.syncONTConfig import syncONTConfigClient
from pages.MeshPage import MeshPage

@pytest.mark.usefixtures("login")
class Test_Sync_ONT():
    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.timeOut = 10
        self.exp = {"code": 0, "msg": "Success"}
        self.syncONTClt = syncONTConfigClient()


    def test_SYNC_ONT_ACT_1(self):
        time.sleep(self.timeOut)
        resBody = self.syncONTClt.syncONTConfig(self.cookie).body
        self.syncONTClt.assert_response(resBody,
                                        self.exp['code'],
                                        self.exp['msg'])
