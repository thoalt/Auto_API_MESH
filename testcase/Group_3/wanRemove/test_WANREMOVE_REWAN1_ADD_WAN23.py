import time
import pytest
from APIObject.wanAPI import WanRemoveClient, WanViewConfigClient, WanCreateEditClient

@pytest.mark.usefixtures("login")
class Test_Wanview():
    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.timeOut = 5
        self.exp = {"code":0, "msg": "Success"}
        self.wanViewClt = WanViewConfigClient()
        self.wanRemoveClt = WanRemoveClient()
        self.wanCreateClt = WanCreateEditClient()
        #
        # self.wanRemoveClt.Remove_All_WAN(cookies=self.cookie)
        self.wanCreateClt.Create_All_Wan(cookies=self.cookie)

        self.wanIdx = 2
        self.vlanID = 1000

    def test_WAN_REMOVE_RES_1(self):
        # Remove wan 1
        pload = self.wanRemoveClt.Create_WanRemove_Pload(wanIndex=1)
        resBody = self.wanRemoveClt.wanRemove(self.cookie, pload=pload).body
        self.wanRemoveClt.assert_response(resBody,
                                          self.exp['code'],
                                          self.exp['msg'])
        time.sleep(45)
        # Add WAN1
        for idx in [2, 3]:
            resBody = self.wanCreateClt.Create_DHCP_Dual(cookies=self.cookie,
                                                        index=idx,
                                                        vlanId=self.vlanID).body

            self.wanCreateClt.assert_response(resBody,
                                              11,
                                              "Verify Fail")
            time.sleep(5)

        # resBody = self.wanViewClt.wanViewConfig(self.cookie).body
        # results = self.wanViewClt.get_result(resBody)
        # self.wanViewClt.assert_val(4, len(results))
