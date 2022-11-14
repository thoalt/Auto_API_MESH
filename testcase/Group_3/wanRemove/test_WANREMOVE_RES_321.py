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
        # self.wanRemoveClt.Remove_All_WAN(cookies=self.cookie)

        self.wanCreateClt = WanCreateEditClient()
        self.wanCreateClt.Create_All_Wan(cookies=self.cookie)

        self.wanIdx = 1

    def test_WAN_REMOVE_RES_1(self):
        for idx in [3, 2, 1]:
            pload = self.wanRemoveClt.Create_WanRemove_Pload(wanIndex=idx)
            resBody = self.wanRemoveClt.wanRemove(self.cookie, pload=pload).body
            self.wanRemoveClt.assert_response(resBody,
                                            self.exp['code'],
                                            self.exp['msg'])
            time.sleep(45)

        resBody = self.wanViewClt.wanViewConfig(self.cookie).body
        results = self.wanViewClt.get_result(resBody)
        self.wanViewClt.assert_val(1, len(results))
