import time
import pytest
from APIObject.passwordEdit import passwordEditClient


@pytest.mark.usefixtures("login")
class Test_DeviceInfoView():
    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.timeOut = 5
        self.exp = {"code": 8, "msg": "Invalid Action"}
        self.passwordedit = passwordEditClient()
        self.passWord = "VNPT@88Tech"
        self.data = ['passwordEdit1', 'passwordEdi']

    def test_DEV_INFO_VIEW_ACT_1(self):
        time.sleep(self.timeOut)
        resbody_Lst = []
        for item in self.data:
            pload = self.passwordedit.Create_passwordEdit_Pload(password=self.passWord,action=item)
            resBody = self.passwordedit.passwordEdit(self.cookie,pload).body
            resbody_Lst.append(resBody)
        self.passwordedit.assert_response_list(resbody_Lst,
                                        self.exp['code'],
                                        self.exp['msg'])
