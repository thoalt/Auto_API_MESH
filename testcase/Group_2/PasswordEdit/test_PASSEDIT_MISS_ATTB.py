import time
import pytest
from APIObject.passwordEdit import passwordEditClient


@pytest.mark.usefixtures("login")
class Test_DeviceInfoView():
    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.timeOut = 5
        self.exp = {"code": 10, "msg": "Miss Attribute"}
        self.passwordedit = passwordEditClient()
        self.passWord = "VNPT"
        pload = self.passwordedit.Create_passwordEdit_Pload(password=self.passWord)
        self.data = [self.passwordedit.Remove_Key_In_Pload(pload, 'action'),
                     self.passwordedit.Remove_Key_In_Pload(pload, 'username'),
                     self.passwordedit.Remove_Key_In_Pload(pload, 'password')]

    def test_DEV_INFO_VIEW_ACT_1(self):
        time.sleep(self.timeOut)
        resbody_Lst = []
        for item in self.data:
            resBody = self.passwordedit.passwordEdit(self.cookie,pload=item).body
            resbody_Lst.append(resBody)
        self.passwordedit.assert_response_list(resbody_Lst,
                                        self.exp['code'],
                                        self.exp['msg'])
