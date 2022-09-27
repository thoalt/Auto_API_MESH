import time
import pytest
from APIObject.discovery import discoveryClient
from Config import config as cfg

class Test_Discovery():
    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.timeout = 2
        self.disClt = discoveryClient()
        self.exp = {"code": 11, "msg": "Verify Fail"}
        cltMAC = cfg.CLIENT_MAC
        self.data = [cltMAC[:-1],
                     cltMAC + 'AB',
                     cltMAC.replace(':', '-'),
                     cltMAC.replace(':', ' '),
                     cltMAC.replace(':', ''),
                     cltMAC.lower(),
                     "01:23:45:67:89:AH"]

    @pytest.mark.success
    def test_DISCOVER_ACT_1(self):
        resBody_Lst = []
        for item in self.data:
            pload = self.disClt.Create_Discovery_Pload(clientMac=item)
            resBody = self.disClt.discovery(pload=pload)
            resBody_Lst.append(resBody)
            time.sleep(self.timeout)

        self.disClt.assert_response_list(resBody_Lst,
                                    self.exp['code'],
                                    self.exp['msg'])
