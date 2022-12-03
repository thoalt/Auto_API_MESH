import time
import pytest
from assertpy import soft_assertions

from APIObject.serviceAPI import ddnsViewClient
from pages.AdvancePage import AdvDDNSPage


@pytest.mark.usefixtures("login", "login_CAP_GUI")
class Test_DdnsCreate():
    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.timeOut = 15
        self.exp = {"code": 0, "msg": "Success", "action": "ddnsView"}
        self.dataLst = ["dyndns.org", "changeip.com", "zoneedit.com", "free.editdns.net", "no-ip.com", "dnsmax.com",
                        "thatip.com", "he.ne", "dnsdynamic.org", "dnsexit.com", "ovh.com", "namecheap.com"]
        self.dataExp = ["dyndns.org", "changeip.com", "zoneedit.com", "free.editdns.net", "no-ip.com", "dnsmax.com",
                        "thatip.com", "he.ne", "dnsdynamic.org", "dnsexit.com", "ovh.com", "namecheap.com"]

        self.ddnsViewClt = ddnsViewClient()

        self.wrp = AdvDDNSPage(self.driver)

    def test_DDNSVIEW_RESULT_1(self):
        resBody_lst = []
        with soft_assertions():
            for idx, data in enumerate(self.dataLst):
                self.wrp.setting_DDNS(dataEnty="abc" + str(idx),
                                      DDNSServer=data,
                                      hostName="10.10.10.1" + str(idx),
                                      userName="DDNS_User" + str(idx),
                                      password="DDNS_Pass" + str(idx),
                                      clickApply=True)
                time.sleep(self.timeOut)

                #Call API Ddns view
                resBody = self.ddnsViewClt.ddnsView(self.cookie).body
                resBody_lst.append(resBody)

                self.wrp.navigation_to_ddns()
                self.wrp.click_delete_ddns0()

                self.ddnsViewClt.assert_response(resBody,
                                                      self.exp['code'],
                                                      self.exp['msg'])

                self.ddnsViewClt.ddns_assert_result(resBody,
                                                    serviceProvider=data,
                                                    hostname="10.10.10.1" + str(idx),
                                                    username="DDNS_User" + str(idx),
                                                    password="DDNS_Pass" + str(idx),
                                                    )

