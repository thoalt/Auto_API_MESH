import time
import pytest
from APIObject.wanAPI import WanRemoveClient, WanViewConfigClient, WanCreateEditClient

@pytest.mark.usefixtures("login")
class Test_Wanview():
    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.timeOut = 5
        self.exp = {"code":11, "msg": "Verify Fail"}
        self.wanIdx = 1
        self.vlanID = 10
        self.wanViewClt = WanViewConfigClient()
        self.wanRemoveClt = WanRemoveClient()
        self.wanRemoveClt.Remove_All_WAN(cookies=self.cookie)

        self.wanCreateClt = WanCreateEditClient()
        self.wanCreateClt.Create_DHCP_Dual(cookies=self.cookie,
                                         index=self.wanIdx,
                                         vlanId=self.vlanID)

        self.wanViewClt = WanViewConfigClient()
        self.wanViewClt.wanViewConfig(self.cookie)


    def test_WAN_REMOVE_RES_1(self):
        for idx in range(2, 4):
            pload = self.wanRemoveClt.Create_WanRemove_Pload(wanIndex=idx)
            resBody = self.wanRemoveClt.wanRemove(self.cookie, pload=pload).body
            self.wanRemoveClt.assert_response(resBody,
                                            self.exp['code'],
                                            self.exp['msg'])
            time.sleep(5)

