import time
import pytest
from APIObject.radio5GView import radio5GViewClient


@pytest.mark.usefixtures("login")
class Test_Radio5GView():
    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.timeOut = 5
        self.exp = {"code": 0, "msg": "Success", "action": "radio2.4GView"}
        #self.data = {"radio 5Gview", " radio5GView", "radio5GView "}
        self.radio5G = radio5GViewClient()

    @pytest.mark.success
    def test_RADIO_5G_RES_1(self):
        time.sleep(self.timeOut)
        #for item in self.data:

            #resBody_Lst = []
        pload = self.radio5G.Create_radio5GView_Pload()
        resBody =self.radio5G.radio5GView(self.cookie, pload=pload).body
        self.radio5G.assert_response_list(resBody,
                                          self.exp['code'],
                                          self.exp['msg'],
                                          self.exp['action'])
