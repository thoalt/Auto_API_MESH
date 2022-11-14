import time
import pytest
from APIObject.serviceAPI import ddnsRemoveClient

@pytest.mark.usefixtures("login")
class Test_ddnsRemove():
    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.timeOut = 5
        self.exp = {"code": 0, "msg": "Success", "action": "ddnsRemove"}
        self.ddnsRemoveClt = ddnsRemoveClient()
        self.data = [0, 1, 2147483646, 2147483647]
        self.idx = 0


    def test_ddnsRemove_RES_1(self):
        resBody_Lst = []
        for item in self.data:
            pload = self.ddnsRemoveClt.Create_ddnsRemove_Pload(index=self.idx, reqID=item)
            resBody = self.ddnsRemoveClt.ddnsRemove(self.cookie, pload=pload).body
            resBody_Lst.append(resBody)
            time.sleep(self.timeOut)

        self.ddnsRemoveClt.assert_response_list(resBody_Lst,
                                        self.exp['code'],
                                        self.exp['msg'])

