import time
import pytest
from APIObject.syncONTConfig import syncONTConfigClient


@pytest.mark.usefixtures("login")
class Test_Sync_ONT():
    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.timeOut = 5
        self.exp = {"code": 0, "msg": "Success", "action": "syncONTConfig"}
        self.syncONTClt = syncONTConfigClient()

    @pytest.mark.success
    def test_SYNC_ONT_ACT_1(self):
        time.sleep(self.timeOut)
        resBody = self.syncONTClt.syncONTConfig(self.cookie).body
        self.syncONTClt.assert_response(resBody,
                                        self.exp['code'],
                                        self.exp['msg'],
                                        self.exp['action'])