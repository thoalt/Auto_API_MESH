import time
import pytest
from APIObject.wifi5GAPI import radio5GViewClient


@pytest.mark.usefixtures("login")
class Test_Radio5GView():
    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.timeOut = 5
        self.exp = {"code": 9, "msg": "Miss Request ID"}
        self.radio5G = radio5GViewClient()

        pload = self.radio5G.Create_radio5GView_Pload()
        self.data = [self.radio5G.Remove_Key_In_Pload(pload, 'requestId')]

    def test_RADIO_5G_ACT_1(self):
        time.sleep(self.timeOut)
        resBody_Lst = []
        for item in self.data:
            resBody =self.radio5G.radio5GView(self.cookie, pload=item).body
            resBody_Lst.append(resBody)

        self.radio5G.assert_response_list(resBody_Lst,
                                              self.exp['code'],
                                              self.exp['msg'])