import pytest
from assertpy import assert_that
from base.SSHLib import SSH_Lib
from APIObject.openssesion import openssesionClient


@pytest.mark.usefixtures("create_shell")
class Test_OpenSession():
    ### Data Test
    val_Time = [605]
    inval_Time = [10, 590]
    val_reqID = [0, 1, 2147483646, 2147483647]
    inval_reqID = [-1, 1.12, 2147483648]

    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        session = SSH_Lib(SSHShell=self.SSHShell)
        session.start_mobile_agent()
        self.client = openssesionClient()



    def test_Openssesion_Success_first(self):
        reqID, res = self.client.Open_Session()
        resBody = res.body
        self.client.assert_opensession(resBody, 0, "Success")

    # def test_OPEN_ACT_2(self):
    #     payload = self.client.Create_OpenSession_Pload(action="openSession1")
    #     reqID, res = self.client.Open_Session(pload=payload)
    #     resBody = res.body
    #     self.client.assert_opensession(resBody, 8, "Invalid Action")

    # def test_Openssesion_Success_Valid_Time(self):
    #     num = 2
    #     resBody = {}
    #     reqID = 0
    #     for i in range(0, num):
    #         reqID, resBody = self.Open_Session()
    #
    #         if i != num:
    #             time.sleep(self.val_Time[0])
    #
    #     assert_that(resBody['status']).is_equal_to(0)
    #     assert_that(resBody['message']).is_equal_to("Success")
    #     assert_that(resBody['requestId']).is_equal_to(reqID)
    #
    # def test_Openssesion_Fail_Invalid_Time_Min(self):
    #     num = 2
    #     resBody = {}
    #     reqID = 0
    #     for i in range(0, num):
    #         reqID, resBody = self.Open_Session()
    #
    #         if i != num:
    #             time.sleep(self.inval_Time[0])
    #
    #     assert_that(resBody['status']).is_equal_to(14)
    #     assert_that(resBody['message']).is_equal_to("Open Session Failed")
    #     assert_that(resBody['requestId']).is_equal_to(reqID)
    #
    # def test_Openssesion_Fail_Invalid_Time_Max(self):
    #     num = 2
    #     resBody = {}
    #     reqID = 0
    #     for i in range(0, num):
    #         reqID, resBody = self.Open_Session()
    #
    #         if i != num:
    #             time.sleep(self.inval_Time[1])
    #
    #     assert_that(resBody['status']).is_equal_to(14)
    #     assert_that(resBody['message']).is_equal_to("Open Session Failed")
    #     assert_that(resBody['requestId']).is_equal_to(reqID)
    #
    # def test_Openssesion_Success_Valid_ReqID_0(self):
    #     reqID, resBody = self.Open_Session(reqID=self.val_reqID[0])
    #     print(resBody)
    #     assert_that(resBody['status']).is_equal_to(0)
    #     assert_that(resBody['message']).is_equal_to("Success")
    #     assert_that(resBody['requestId']).is_equal_to(reqID)
    #
    # def test_Openssesion_Success_Valid_ReqID_1(self):
    #     reqID, resBody = self.Open_Session(reqID=self.val_reqID[1])
    #     print(resBody)
    #     assert_that(resBody['status']).is_equal_to(0)
    #     assert_that(resBody['message']).is_equal_to("Success")
    #     assert_that(resBody['requestId']).is_equal_to(reqID)
    #
    # def test_Openssesion_Success_Valid_ReqID_2(self):
    #     reqID, resBody = self.Open_Session(reqID=self.val_reqID[2])
    #     print(resBody)
    #     assert_that(resBody['status']).is_equal_to(0)
    #     assert_that(resBody['message']).is_equal_to("Success")
    #     assert_that(resBody['requestId']).is_equal_to(reqID)
    #
    # def test_Openssesion_Success_Valid_ReqID_3(self):
    #     reqID, resBody = self.Open_Session(reqID=self.val_reqID[3])
    #     print(resBody)
    #     assert_that(resBody['status']).is_equal_to(0)
    #     assert_that(resBody['message']).is_equal_to("Success")
    #     assert_that(resBody['requestId']).is_equal_to(reqID)
    #
    # def test_Openssesion_Success_InValid_ReqID_1(self):
    #     reqID, resBody = self.Open_Session(reqID=self.inval_reqID[0])
    #     print(resBody)
    #     assert_that(resBody['status']).is_equal_to(0)
    #     assert_that(resBody['message']).is_equal_to("Success")
    #     assert_that(resBody['requestId']).is_equal_to(reqID)
    #
    #     # time.sleep(self.val_Time[0])
    #
    # def test_Openssesion_Success_InValid_ReqID_2(self):
    #
    #     reqID, resBody = self.Open_Session(reqID=self.inval_reqID[1])
    #     print(resBody)
    #     assert_that(resBody['status']).is_equal_to(0)
    #     assert_that(resBody['message']).is_equal_to("Success")
    #     assert_that(resBody['requestId']).is_equal_to(reqID)
    #
    # def test_Openssesion_Success_InValid_ReqID_3(self):
    #     reqID, resBody = self.Open_Session(reqID=self.inval_reqID[2])
    #     print(resBody)
    #     assert_that(resBody['status']).is_equal_to(0)
    #     assert_that(resBody['message']).is_equal_to("Success")
    #     assert_that(resBody['requestId']).is_equal_to(reqID)