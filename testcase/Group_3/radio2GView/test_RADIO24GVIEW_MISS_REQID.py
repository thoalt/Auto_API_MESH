import time
import pytest
from APIObject.wifi24GAPI import radio24GViewClient

@pytest.mark.usefixtures("login")
class Test_radio24GView():
    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.timeOut = 2
        self.exp = {"code": 9, "msg": "Miss Request ID"}
        self.radio24GViewClt = radio24GViewClient()
        pload = self.radio24GViewClt.Create_radio24GView_Pload()
        self.data = [self.radio24GViewClt.Remove_Key_In_Pload(pload, 'requestId')]

    def test_RADIO24GVIEW_ACT_2(self):
        time.sleep(self.timeOut)
        resBody_Lst = []
        for item in self.data:
          resBody = self.radio24GViewClt.radio24GView(self.cookie, pload=item).body
          resBody_Lst.append(resBody)
        self.radio24GViewClt.assert_response_list(resBody_Lst,
                                        self.exp['code'],
                                        self.exp['msg'])
