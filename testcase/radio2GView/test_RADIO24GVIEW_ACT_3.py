import time
import pytest
from APIObject.radio24GView import radio24GViewClient

@pytest.mark.usefixtures("login")
class Test_radio24GView():
    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.timeOut = 2
        self.exp = {"code": 8, "msg": "Invalid Action"}
        self.data = ['Radio2.4GView', 'RADIO2.4GVIEW']
        self.radio24GViewClt = radio24GViewClient()

    def test_RADIO24GVIEW_ACT_3(self):
        time.sleep(self.timeOut)
        resBody_Lst = []
        for item in self.data:
          pload = self.radio24GViewClt.Create_radio24GView_Pload(action=item)
          resBody = self.radio24GViewClt.radio24GView(self.cookie, pload=pload).body
          resBody_Lst.append(resBody)
        self.radio24GViewClt.assert_response_list(resBody_Lst,
                                        self.exp['code'],
                                        self.exp['msg'])
