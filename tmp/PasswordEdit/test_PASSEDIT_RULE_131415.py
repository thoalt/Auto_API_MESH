import time
import pytest
from APIObject.passwordEdit import passwordEditClient


@pytest.mark.usefixtures("login")
class Test_DeviceInfoView():
    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.timeOut = 5
        self.exp = {"code": 0, "msg": "Success"}
        self.passwordedit = passwordEditClient()
        self.data = ['ttcn@99C', 'ttcn@88CN11111111111111111111111', 'ttcn@88CNmmmmmmmmmmm']

    def test_DEV_INFO_VIEW_ACT_1(self):
        time.sleep(self.timeOut)
        resbody_Lst = []
        for item in self.data:
            pload = self.passwordedit.Create_passwordEdit_Pload(password=item)
            resBody = self.passwordedit.passwordEdit(self.cookie,pload).body
            resbody_Lst.append(resBody)
        self.passwordedit.assert_response_list(resbody_Lst,
                                        self.exp['code'],
                                        self.exp['msg'])
