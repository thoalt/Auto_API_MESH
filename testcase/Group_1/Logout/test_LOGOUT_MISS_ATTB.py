import time

import pytest
from assertpy import assert_that

from APIObject.logout import LogoutClient
from Utilities import Utility as utl

@pytest.mark.usefixtures("login")
class Test_Login():
    sesID, salt = "", ""
    reqID = 0

    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.exp = {"code": 10, "msg": "Miss Attribute"}
        self.timeLogout = 5
        # Logout
        self.LogoutClt = LogoutClient()
        payload = self.LogoutClt.Create_Logout_Pload()
        self.data = self.LogoutClt.Remove_Attribute_In_Pload(payload)

    def test_LOGOUT_ACT_2(self):
        time.sleep(self.timeLogout)
        resBodyLst = []
        for item in self.data:
            resBody = self.LogoutClt.logout(cookies=self.cookie, pload=item).body
            resBodyLst.append(resBody)
        self.LogoutClt.assert_logout_lst(resBodyLst, self.exp['code'], self.exp['msg'])


