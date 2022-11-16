from assertpy import assert_that, soft_assertions

from APIObject.baseClient import BaseClient
from Config import config as cfg
from Utilities import Utility as utl
from base.APILib import API_lib


class LogoutClient(BaseClient):
    def __init__(self):
        super().__init__()
        self.url = cfg.url_Agent
        self.request = API_lib()

    def Create_Logout_Pload(self, action=None, reqID=None):
        pload = cfg.req_logout
        payload = self.set_payload_with_action_reqID(pload=pload, action=action, reqID=reqID)
        return payload

    def logout(self, cookies=None, pload=None):
        if pload is None:
            payload = self.Create_Logout_Pload()
        else:
            payload = pload
        #print("**********Payload *****")
        #print(payload)

        response = self.request.post(url=self.url, headers=self.headersCurl, cookies=cookies, pload=payload)

        return response

    def assert_logout(self, resBody, status, msg, action=None):
        with soft_assertions():
            assert_that(resBody['status']).is_equal_to(status)
            assert_that(resBody['message']).is_equal_to(msg)

            if action is not None:
                actionRes = utl.search_nodes_using_json_path(resBody, jsonPath="$..action")
                assert_that(actionRes).is_equal_to(action)


    def assert_logout_lst(sefl, resBodyLst, status, msg, action=None):
        with soft_assertions():
            for resBody in resBodyLst:
                assert_that(resBody['status']).is_equal_to(status)
                assert_that(resBody['message']).is_equal_to(msg)

                if action is not None:
                    actionRes = utl.search_nodes_using_json_path(resBody, jsonPath="$..action")
                    assert_that(actionRes).is_equal_to(action)