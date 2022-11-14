import time
import pytest
from APIObject.serviceAPI import ddnsRemoveClient

@pytest.mark.usefixtures("login")
class Test_ddnsRemove():
    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.timeOut = 2
        self.exp = {"code": 11, "msg": "Verify Fail"}
        self.ddnsRemoveClt = ddnsRemoveClient()
        self.data = ['', -1, 1.12, 2147483648, 'abc']
        self.idx = 0


    def test_ddnsRemove_RES_1(self):
        time.sleep(self.timeOut)
        resBody_Lst = []
        for item in self.data:
            pload = self.ddnsRemoveClt.Create_ddnsRemove_Pload(index=self.idx, reqID=item)
            resBody = self.ddnsRemoveClt.ddnsRemove(self.cookie, pload=pload).body
            resBody_Lst.append(resBody)

        self.ddnsRemoveClt.assert_response_list(resBody_Lst,
                                        self.exp['code'],
                                        self.exp['msg'])

