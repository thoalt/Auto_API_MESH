import time
import pytest
from APIObject.serviceAPI import ddnsViewClient
from pages.AdvancePage import AdvDDNSPage


@pytest.mark.usefixtures("login", "login_CAP_GUI")
class Test_Radio5GView():
    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.timeOut = 10
        self.exp = {"code": 0, "msg": "Success", "action": "ddnsView"}
        self.dataLst = ["dyndns.org", "changeip.com", "zoneedit.com", "free.editdns.net", "no-ip.com", "dnsmax.com",
                        "thatip.com", "he.ne", "dnsdynamic.org", "dnsexit.com", "ovh.com", "namecheap.com"]
        self.dataExp = ["dyndns.org", "changeip.com", "zoneedit.com", "free.editdns.net", "no-ip.com", "dnsmax.com",
                        "thatip.com", "he.ne", "dnsdynamic.org", "dnsexit.com", "ovh.com", "namecheap.com"]

        self.ddnsViewClt = ddnsViewClient()

        self.wrp = AdvDDNSPage(self.driver)
        self.wrp.navigation_to_add_ddns_page()

    def test_DDNSVIEW_RESULT_1(self):
        resBody_lst = []
        for data in self.dataLst:
            self.wrp.setting_DDNS(dataEnty="abc", DDNSServer=data, hostName="abc.abc",
                     userName="quan", password="123", clickApply=True)
            time.sleep(self.timeOut)

            #Call API Ddns view
            resBody = self.ddnsViewClt.ddnsView(self.cookie).body
            resBody_lst.append(resBody)

            self.wrp.click_delete_ddns()
            self.wrp.navigation_to_add_ddns_page()

        self.ddnsViewClt.assert_response_list(resBody_lst,
                                              self.exp['code'],
                                              self.exp['msg'])

        self.ddnsViewClt.assert_result_lst(resBody_lst,
                                       DDNSServerLst=self.dataExp)

