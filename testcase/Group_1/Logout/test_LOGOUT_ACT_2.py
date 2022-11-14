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
        self.data = ["logout1", "logou"]
        self.exp = {"code": 8, "msg": "Invalid Action"}
        self.timeLogout = 5

        # Logout
        self.LogoutClt = LogoutClient()

    def test_LOGOUT_ACT_2(self):
        time.sleep(self.timeLogout)
        resBodyLst = []
        for actionName in self.data:
            payload = self.LogoutClt.Create_Logout_Pload(action=actionName)
            resBody = self.LogoutClt.logout(cookies=self.cookie, pload=payload).body
            resBodyLst.append(resBody)
        self.LogoutClt.assert_logout_lst(resBodyLst, self.exp['code'], self.exp['msg'])


