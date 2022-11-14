import time
import pytest
from APIObject.serviceAPI import ddnsRemoveClient

@pytest.mark.usefixtures("login")
class Test_ddnsRemove():
    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.timeOut = 2
        self.exp = {"code": 8, "msg": "Invalid Action"}
        self.ddnsRemoveClt = ddnsRemoveClient()
        self.data = ["ă", "â", "đ", "ê", "ô", "ơ", "ư", "á", "à", "ạ", "ả", "ã",
                    "Ă", "Â", "Đ", "Ê", "Ô", "Ơ", "Ư", "Á", "À", "Ạ", "Ả", "Ã"]
        self.idx = 0

    @pytest.mark.success
    def test_ddnsRemove_RES_1(self):
        time.sleep(self.timeOut)
        resBody_Lst = []
        for item in self.data:
            pload = self.ddnsRemoveClt.Create_ddnsRemove_Pload(index=self.idx, action=item)
            resBody = self.ddnsRemoveClt.ddnsRemove(self.cookie, pload=pload).body
            resBody_Lst.append(resBody)

        self.ddnsRemoveClt.assert_response_list(resBody_Lst,
                                        self.exp['code'],
                                        self.exp['msg'])
