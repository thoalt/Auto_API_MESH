import time
import pytest
from APIObject.wifi5GAPI import radio5GViewClient


@pytest.mark.usefixtures("login")
class Test_Radio5GView():
    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.timeOut = 5
        self.exp = {"code": 8, "msg": "Invalid Action"}
        self.data = {"radio 5Gview", " radio5GView", "radio5GView "}
        self.radio5G = radio5GViewClient()


    def test_RADIO_5G_ACT_6(self):
        time.sleep(self.timeOut)
        for item in self.data:

            resBody_Lst = []
            pload = self.radio5G.Create_radio5GView_Pload(action=item)
            resBody =self.radio5G.radio5GView(self.cookie, pload=pload).body
            resBody_Lst.append(resBody)

        self.radio5G.assert_response_list(resBody_Lst,
                                              self.exp['code'],
                                              self.exp['msg'])