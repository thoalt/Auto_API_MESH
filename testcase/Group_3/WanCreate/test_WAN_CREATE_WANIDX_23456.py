import time
import pytest
from APIObject.wanAPI import WanCreateEditClient, WAN_TYPE, IP_VER
from pages.SettingWANPage import SettingWANPage

@pytest.mark.usefixtures("login")
class Test_Wan_Create():
    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.timeOut = 5
        self.exp = {"code": 11, "msg": "Verify Fail"}
        self.wanCreateClt = WanCreateEditClient()
        self.data = ['', -1, 1.12, 0, 4, "abc", "1", "2", "3"]

    def test_WAN_CREATE_RES_1(self):
        time.sleep(self.timeOut)
        resBody_lst = []
        for idx, item in enumerate(self.data):
            ploadCom = self.wanCreateClt.Create_WanCreate_Common_Pload(
                wanIdx=item,
                wanType=WAN_TYPE().DHCP
            )
            pload = self.wanCreateClt.Create_WanCreate_Edit_DHCP_pload(
                pload=ploadCom,
                vlanID=10 + idx,
                IPVer=IP_VER().IPv4
            )

            resBody = self.wanCreateClt.wanCreateEdit(self.cookie, pload=pload).body
            resBody_lst.append(resBody)

        self.wanCreateClt.assert_response_list(resBody_lst,
                                               self.exp['code'],
                                               self.exp['msg'])