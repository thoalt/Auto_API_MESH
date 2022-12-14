import time
import pytest
from APIObject.serviceAPI import ddnsViewClient, ddnsRemoveClient, ddnsCreateEditClient


@pytest.mark.usefixtures("login")
class Test_ddnsView():
    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.timeOut = 2
        self.exp = {"code": 0, "msg": "Success", "action": "ddnsView"}
        self.ddnsViewClt = ddnsViewClient()

        self.ddnsRevClt = ddnsRemoveClient()
        self.ddnsRevClt.ddns_remove_all(self.cookie)

        self.ddnsCreateClt = ddnsCreateEditClient()
        pload = self.ddnsCreateClt.Create_ddnsCreate_pload(index=1,
                                                           serviceProvider="ddndns.org.com",
                                                           hostname="abc.com.vn",
                                                           username="user_1",
                                                           password="pass_1")
        resBody = self.ddnsCreateClt.ddnsCreate(self.cookie, pload).body
        time.sleep(15)

    def test_DDNSVIEW_ACT_1(self):
        time.sleep(self.timeOut)
        resBody = self.ddnsViewClt.ddnsView(self.cookie).body
        result = self.ddnsViewClt.get_result(resBody)

        self.ddnsViewClt.assert_response(resBody,
                                        self.exp['code'],
                                        self.exp['msg'],
                                        self.exp['action'])

        self.ddnsViewClt.assert_val(1, len(result))
