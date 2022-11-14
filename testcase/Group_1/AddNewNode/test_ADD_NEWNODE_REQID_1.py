import time
import pytest
from APIObject.addNewNode import addNewNodeClient

@pytest.mark.usefixtures("login")
class Test_TraceRoute():
    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.timeOut = 2
        self.exp = {"code": 0, "msg": "Success"}
        self.data = [0, 1, 2147483646, 2147483647]
        self.addnewnodeClt = addNewNodeClient()

    def test_TRACE_ROUTE_RES_1(self):
        time.sleep(self.timeOut)
        resBody_lst = []
        for item in self.data:
            pload = self.addnewnodeClt.Create_addNewNode_Pload(reqID=item)
            resBody = self.addnewnodeClt.addNewNode(cookies=self.cookie, pload=pload).body
            resBody_lst.append(resBody)
            time.sleep(150)
        self.addnewnodeClt.assert_response_list(resBody_lst,
                                           self.exp['code'],
                                           self.exp['msg'])


