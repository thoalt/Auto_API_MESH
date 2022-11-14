import time
import pytest
from APIObject.serviceAPI import ddnsCreateEditClient



@pytest.mark.usefixtures("login")
class Test_ddnsEdit():
    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.timeOut = 5
        self.exp = {"code": 0, "msg": "Success", "action": "ddnsEdit"}
        self.data = ["dnsdynamic.org", "dnsexit.com", "ovh.com", "namecheap.com" ]
        # "dyndns.org", "changeip.com", "zoneedit.com", "free.editdns.net", "no-ip.com",
        #"dnsmax.com", "thatip.com", "he.ne", "dnsdynamic.org", "dnsexit.com", "ovh.com", "namecheap.com"]


        self.ddnsEditClt = ddnsCreateEditClient()
        self.idx = 0
        #self.serProvider = "dyndns.org"
        self.hostname = "test.com.vn"
        self.username = "thoalt"
        self.passW = "thoa12345"

    def test_DDNSEDIT_PROVIDER_1(self):
        resBody_lst = []
        for idx, item in enumerate(self.data):
            pload = self.ddnsEditClt.Create_ddnsEdit_Pload(index=idx,
                                                           serviceProvider=item,
                                                           hostname=self.hostname,
                                                           username=self.username,
                                                           password=self.passW)
            resBody = self.ddnsEditClt.ddnsEdit(self.cookie, pload).body
            resBody_lst.append(resBody)
            time.sleep(self.timeOut)

        self.ddnsEditClt.assert_response_list(resBody_lst,
                                         self.exp['code'],
                                         self.exp['msg'])


