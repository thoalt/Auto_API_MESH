import time
import pytest
from APIObject.syncONTConfig import syncONTConfigClient
from pages.MeshPage import MeshPage

@pytest.mark.usefixtures("login", "login_CAP_GUI")
class Test_Sync_ONT():
    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.timeOut = 5
        self.exp = {"code": 0, "msg": "Success"}
        self.syncONTClt = syncONTConfigClient()
        self.meshp = MeshPage(self.driver)
        self.status = True


    def test_SYNC_ONT_ACT_1(self):
        pload = self.syncONTClt.Create_syncONTConfig_Pload(enable=self.status)

        resBody = self.syncONTClt.syncONTConfig(self.cookie, pload=pload).body
        time.sleep(self.timeOut)
        self.meshp.navigate_to_mesh_tab()
        actualStatus = self.meshp.get_enable_sync_ONT_status()
        self.syncONTClt.assert_response(resBody,
                                        self.exp['code'],
                                        self.exp['msg'])

        self.syncONTClt.assert_val(self.status, actualStatus)
