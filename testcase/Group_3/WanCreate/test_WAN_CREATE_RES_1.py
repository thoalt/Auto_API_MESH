import time
import pytest
from APIObject.wanAPI import WanCreateEditClient, WAN_TYPE, IP_VER

@pytest.mark.usefixtures("login")
class Test_Wan_Create():
    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.timeOut = 5
        self.exp = {"code": 11, "msg": "Verify Fail"}
        self.wanCreateClt = WanCreateEditClient()
        self.data = ['', -3, 1.12, 2, 88, 4001, "abc", "3", "4", "3999", "4000"]

    def test_WAN_CREATE_RES_1(self):
        time.sleep(self.timeOut)
        resBody_lst = []
        for idx, item in enumerate(self.data):
            ploadCom = self.wanCreateClt.Create_WanCreate_Common_Pload(
                wanIdx=1,
                wanType=WAN_TYPE().DHCP
            )
            pload = self.wanCreateClt.Create_WanCreate_Edit_DHCP_pload(
                pload=ploadCom,
                vlanID=item,
                IPVer=IP_VER().IPv4
            )

            resBody = self.wanCreateClt.wanCreateEdit(self.cookie, pload=pload).body
            resBody_lst.append(resBody)

        self.wanCreateClt.assert_response_list(resBody_lst,
                                        self.exp['code'],
                                        self.exp['msg'])