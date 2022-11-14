import time
import pytest
from APIObject.passwordEdit import passwordEditClient


@pytest.mark.usefixtures("login")
class Test_DeviceInfoView():
    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.timeOut = 10
        self.exp = {"code": 0, "msg": "Success"}
        self.passwordedit = passwordEditClient()
        self.passWord = "VNPT@88Tech"

    def test_DEV_INFO_VIEW_ACT_1(self):
        time.sleep(self.timeOut)
        pload = self.passwordedit.Create_passwordEdit_Pload(password=self.passWord)
        resBody = self.passwordedit.passwordEdit(self.cookie,pload).body
        self.passwordedit.assert_response(resBody,
                                        self.exp['code'],
                                        self.exp['msg'])
