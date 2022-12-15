import time

import pytest
from APIObject.logout import LogoutClient

@pytest.mark.usefixtures("login")
class Test_Login():
    sesID, salt = "", ""
    reqID = 0

    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.data = []
        self.exp = {"code": 0, "msg": "Success", "action": "logout"}
        self.timeLogout = 5
        # Logout
        self.LogoutClt = LogoutClient()


    def test_LOGOUT_ACT_1(self):
        time.sleep(self.timeLogout)
        resBody = self.LogoutClt.logout(cookies=self.cookie).body
        self.LogoutClt.assert_logout(resBody,
                                   self.exp['code'],
                                   self.exp['msg'],
                                   self.exp['action'])

