import time
import pytest
from APIObject.passwordEdit import passwordEditClient


@pytest.mark.usefixtures("login")
class Test_DeviceInfoView():
    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.timeOut = 5
        self.exp = {"code": 5, "msg": "Invalid password. Password need include number, uppercase, lowercase and specific character"}
        self.passwordedit = passwordEditClient()
        self.data = ['ttcn@99', 'ttcn@88CN111111111111111111111112', 'ttcn@CNA', 'ttcn@Cnabnmbbnnmmmjjiufusruhgshg', 'TTCN1@3C',
                     'TTCN@88ABNMKFHIUHTGIGFSJFGSJGJJJ', 'ttcn@vn12',' ttcn@88cnfhgksgbsgbsgbsgbsbgbbbb', 'ttcn11CNm', 'ttcnk88cnfhgksgbsgbsgbsgbsbgbbbb' ]

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
