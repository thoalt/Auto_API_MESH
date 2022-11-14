import time
import pytest
from APIObject.serviceAPI import ddnsCreateEditClient


@pytest.mark.usefixtures("login")
class Test_DdnsCreate():
    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.timeOut = 5
        self.exp = {"code": 0, "msg": "Success", "action": "ddnsCreat"}
        self.data = ["dnsdynamic.org"]
        #"dyndns.org", "changeip.com", "zoneedit.com", "free.editdns.net", "no-ip.com",
        #"dnsmax.com", "thatip.com", "he.ne", "dnsdynamic.org", "dnsexit.com", "ovh.com", "namecheap.com"


        self.ddnsCreateClt = ddnsCreateEditClient()
        self.idx = 3
        self.serProvider = "dyndns.org"
        self.hostname = "test.com.vn"
        self.username = "thoalt"
        self.passW = "thoa12345"

    def test_DDNSEDIT_PROVIDER_1(self):
        resBody_lst = []
        for item in self.data:
            pload = self.ddnsCreateClt.Create_ddnsCreate_pload(index=self.idx,
                                                           serviceProvider=item,
                                                           hostname=self.hostname,
                                                           username=self.username,
                                                           password=self.passW)
            resBody = self.ddnsCreateClt.ddnsCreate(self.cookie, pload).body
            resBody_lst.append(resBody)
            time.sleep(self.timeOut)

        self.ddnsCreateClt.assert_response_list(resBody_lst,
                                         self.exp['code'],
                                         self.exp['msg'])


