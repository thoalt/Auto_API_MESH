import time
import pytest
from APIObject.passwordEdit import passwordEditClient


@pytest.mark.usefixtures("login")
class Test_DeviceInfoView():
    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.timeOut = 5
        self.exp = {"code": 0, "msg": "Success", "action": "passwordEdit"}
        self.passwordedit = passwordEditClient()
        self.passWord = "VNPT@88Tech"
        self.data = [0, 1, 2147483646, 2147483647]

    def test_DEV_INFO_VIEW_ACT_1(self):
        time.sleep(self.timeOut)
        resbody_Lst = []
        for idx, item in enumerate(self.data):
            pload = self.passwordedit.Create_passwordEdit_Pload(password=self.passWord + str(idx), reqID=item)
            resBody = self.passwordedit.passwordEdit(self.cookie,pload=pload).body
            resbody_Lst.append(resBody)
            time.sleep(10)
        self.passwordedit.assert_response_list(resbody_Lst,
                                        self.exp['code'],
                                        self.exp['msg'])
