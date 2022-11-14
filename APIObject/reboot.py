from assertpy import assert_that, soft_assertions

from APIObject.baseClient import BaseClient
from Config import config as cfg
from Utilities import Utility as utl
from base.APILib import API_lib


class rebootClient(BaseClient):
    def __init__(self):
        super().__init__()
        self.url = cfg.url_Agent
        self.request = API_lib()

    def Create_Reboot_Pload(self, action=None, macList=None, reqID=None):
        pload = cfg.req_reboot

        payload = self.set_payload_with_action_reqID(pload=pload, action=action, reqID=reqID)
        if macList is not None:
            payload['macList'] = macList
        return payload

    def reboot(self, cookies=None, pload=None):
        if pload is None:
            payload = self.Create_Reboot_Pload()
        else:
            payload = pload

        response = self.request.post(url=self.url, headers=self.headersCurl, cookies=cookies, pload=payload)

        return response

    def assert_result(self, resBody, macList):
        resultBody = self.get_result(resBody)
        macLst = macList.split(",")
        with soft_assertions():
            for idx, result in enumerate(resultBody):
                assert_that(result['macAddr'], macLst[idx])

    # def assert_reboot(self, resBody, status, msg, action=None):
    #     assert_that(resBody['status']).is_equal_to(status)
    #     assert_that(resBody['message']).is_equal_to(msg)
    #
    #     if action is not None:
    #         actionRes = utl.search_nodes_using_json_path(resBody, jsonPath="$..action")
    #         assert_that(actionRes).is_equal_to(action)