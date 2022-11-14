import time
import pytest
from APIObject.wifi24GAPI import radio24GViewClient

@pytest.mark.usefixtures("login")
class Test_radio24GView():
    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.timeOut = 2
        self.exp = {"code":0 , "msg": "Success", "action": "radio2.4GView"}
        self.data = [0, 1, 2147483646, 2147483647]
        self.radio24GViewClt = radio24GViewClient()


    def test_RADIO24GVIEW_RES_1(self):
        time.sleep(self.timeOut)
        resBody_Lst = []
        for item in self.data:
          pload = self.radio24GViewClt.Create_radio24GView_Pload(reqID=item)
          resBody = self.radio24GViewClt.radio24GView(self.cookie, pload=pload).body
          resBody_Lst.append(resBody)
        self.radio24GViewClt.assert_response_list(resBody_Lst,
                                        self.exp['code'],
                                        self.exp['msg'],
                                        self.exp['action'])
