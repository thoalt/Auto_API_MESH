from assertpy import assert_that, soft_assertions

from APIObject.baseClient import BaseClient
from Config import config as cfg
from Utilities import Utility as utl
from base.APILib import API_lib


class LoginClient(BaseClient):
    def __init__(self):
        super().__init__()
        self.url = cfg.url_Login
        self.request = API_lib()

    def login(self, cookies):
        response = self.request.post(url=self.url, headers=self.headersCurl, cookies=cookies)
        return response

    def assert_login(self, resBody, status, msg, action=None, result=None):
        with soft_assertions():
            assert_that(resBody['status']).is_equal_to(status)
            assert_that(resBody['message']).is_equal_to(msg)

            if action is not None:
                actionRes = utl.search_nodes_using_json_path(resBody, jsonPath="$..action")
                assert_that(actionRes).is_equal_to(action)

            if result is not None:
                resResult = utl.search_nodes_using_json_path(resBody, jsonPath="$..results[*].configuredHSIServices")

                if result is True:
                    assert_that(resResult).is_true()
                else:
                    assert_that(resResult).is_false()

    def assert_login_list(self, resBodyLst, status, msg, action=None, result=None):
        with soft_assertions():
            for resBody in resBodyLst:
                assert_that(resBody['status']).is_equal_to(status)
                assert_that(resBody['message']).is_equal_to(msg)
                if action is not None:
                    actionRes = utl.search_nodes_using_json_path(resBody, jsonPath="$..action")
                    assert_that(actionRes).is_equal_to(action)

                if result is not None:
                    resResult = utl.search_nodes_using_json_path(resBody, jsonPath="$..results[*].configuredHSIServices")
                    if result is True:
                        assert_that(resResult).is_true()
                    else:
                        assert_that(resResult).is_false()