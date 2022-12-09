"""
This module is for these API:
    - ddnsView
    - ddnsCreate
    - ddnsEdit
    - ddnsRemove
    - portforwardView
    - portforwardCreate
    - portforwardEdit
    - portforwardRemove
"""
import time

from assertpy import soft_assertions

from APIObject.baseClient import BaseClient
from Config import config as cfg
from base.APILib import API_lib


class ddnsViewClient(BaseClient):
    def __init__(self):
        super().__init__()
        self.url = cfg.url_Agent
        self.request = API_lib()

    def Create_ddnsView_Pload(self, action=None, reqID=None):
        pload = cfg.req_ddnsView
        payload = self.set_payload_with_action_reqID(pload=pload, action=action, reqID=reqID)
        return payload

    def ddnsView(self, cookies=None, pload=None):
        if pload is None:
            payload = self.Create_ddnsView_Pload()
        else:
            payload = pload

        response = self.request.post(url=self.url, headers=self.headersCurl, cookies=cookies, pload=payload)
        return response

    def ddns_assert_result(self, resBody, serviceProvider=None, hostname=None, username=None, password=None):
        resultRes = self.get_result(resBody)[0]
        with soft_assertions():
            if serviceProvider is not None:
                self.assert_val(resultRes['serviceProvider'], serviceProvider, desc='serviceProvider')

            if hostname is not None:
                self.assert_val(resultRes['hostname'], hostname, desc='hostname')

            if username is not None:
                self.assert_val(resultRes['username'], username, desc='username')

            if password is not None:
                self.assert_val(resultRes['password'], password, desc='password')

    def ddns_assert_result_lst(self, resBodyLst, serviceProvider=None, hostname=None, username=None, password=None ):
        with soft_assertions():
            for resBody in resBodyLst:
                self.ddns_assert_result(resBody,
                                        serviceProvider=serviceProvider,
                                        hostname=hostname,
                                        username=username,
                                        password=password)

class ddnsCreateEditClient(BaseClient):
    def __init__(self):
        super().__init__()
        self.url = cfg.url_Agent
        self.request = API_lib()

    def Add_Create_Edit_pload(self, payload, index=None, serviceProvider=None, hostname=None, username=None,
                              password=None):
        if index is not None:
            payload.update({'index': index})
            # payload['index'] = index

        if serviceProvider is not None:
            payload.update({'serviceProvider': serviceProvider})
            # payload['serviceProvider'] = serviceProvider

        if hostname is not None:
            payload['hostname'] = hostname

        if username is not None:
            payload['username'] = username

        if password is not None:
            payload['password'] = password
        return payload

    def Create_ddnsCreate_pload(self, action=None, reqID=None, index=None, serviceProvider=None, hostname=None,
                                username=None, password=None):
        pload = cfg.req_ddnsCreate
        payload = self.set_payload_with_action_reqID(pload=pload, action=action, reqID=reqID)
        return self.Add_Create_Edit_pload(payload, index=index, serviceProvider=serviceProvider,
                                          hostname=hostname, username=username, password=password)

    def Create_ddnsEdit_Pload(self, action=None, reqID=None, index=None, serviceProvider=None, hostname=None,
                              username=None, password=None):

        pload = cfg.req_ddnsEdit
        payload = self.set_payload_with_action_reqID(pload=pload, action=action, reqID=reqID)

        return self.Add_Create_Edit_pload(payload, index=index, serviceProvider=serviceProvider,
                                          hostname=hostname, username=username, password=password)

    def ddnsCreate(self, cookies=None, pload=None):
        if pload is None:
            payload = self.Create_ddnsCreate_pload()
        else:
            payload = pload

        response = self.request.post(url=self.url, headers=self.headersCurl, cookies=cookies, pload=payload)
        return response

    def ddnsEdit(self, cookies=None, pload=None):
        if pload is None:
            payload = self.Create_ddnsEdit_Pload()
        else:
            payload = pload

        response = self.request.post(url=self.url, headers=self.headersCurl, cookies=cookies, pload=payload)
        return response

class ddnsRemoveClient(BaseClient):
    def __init__(self):
        super().__init__()
        self.url = cfg.url_Agent
        self.request = API_lib()

    def Create_ddnsRemove_Pload(self, action=None, reqID=None, index=None):
        pload = cfg.req_ddnsRemove
        payload = self.set_payload_with_action_reqID(pload=pload, action=action, reqID=reqID)

        if index is not None:
            payload.update({'index': index})

        return payload

    def ddnsRemove(self, cookies=None, pload=None):
        if pload is None:
            payload = self.Create_ddnsRemove_Pload()
        else:
            payload = pload

        response = self.request.post(url=self.url, headers=self.headersCurl, cookies=cookies, pload=payload)
        return response

    def ddns_remove_all(self, cookies=None):
        viewClt = ddnsViewClient()
        resBody = viewClt.ddnsView(cookies).body
        ddnsResult = viewClt.get_result(resBody)

        for idx in range(len(ddnsResult), 0, -1):
            ddnsIdx = ddnsResult[idx]['index']
            pload = self.Create_ddnsRemove_Pload(index=ddnsIdx)
            response = self.ddnsRemove(cookies=cookies, pload=pload)
            time.sleep(15)


class portforwardViewClient(BaseClient):
    def __init__(self):
        super().__init__()
        self.url = cfg.url_Agent
        self.request = API_lib()

    def Create_portforwardView_Pload(self, action=None, reqID=None):
        pload = cfg.req_portforwardView
        payload = self.set_payload_with_action_reqID(pload=pload, action=action, reqID=reqID)
        return payload

    def portforwardView(self, cookies=None, pload=None):
        if pload is None:
            payload = self.Create_portforwardView_Pload()
        else:
            payload = pload

        response = self.request.post(url=self.url, headers=self.headersCurl, cookies=cookies, pload=payload)
        return response


class portforwardCreateEditClient(BaseClient):
    def __init__(self):
        super().__init__()
        self.url = cfg.url_Agent
        self.request = API_lib()

    def Add_Create_Edit_pload(self, payload, ruleIndex=None, wanIndex=None, protocol=None, startRemotePort=None,
                              ipAddr=None, startLocalPort=None, serviceName=None):
        if ruleIndex is not None:
            payload.update({'ruleIndex': ruleIndex})
            # payload['index'] = index

        if wanIndex is not None:
            payload.update({'wanIndex': wanIndex})
            # payload['serviceProvider'] = serviceProvider

        if protocol is not None:
            payload['protocol'] = protocol

        if startRemotePort is not None:
            payload['startRemotePort'] = startRemotePort

        if ipAddr is not None:
            payload['ipAddr'] = ipAddr

        if startLocalPort is not None:
            payload['startLocalPort'] = startLocalPort
        if serviceName is not None:
            payload['serviceName'] = serviceName

        return payload

    def Create_portforwardCreate_pload(self, action=None, reqID=None,
                                       ruleIndex=None, wanIndex=None, protocol=None,
                                       startRemotePort=None,
                                       ipAddr=None, startLocalPort=None, serviceName=None):

        pload = cfg.req_portforwardCreate
        payload = self.set_payload_with_action_reqID(pload=pload, action=action, reqID=reqID)
        return self.Add_Create_Edit_pload(payload, ruleIndex=ruleIndex, wanIndex=wanIndex, protocol=protocol,
                                          startRemotePort=startRemotePort, ipAddr=ipAddr, startLocalPort=startLocalPort,
                                          serviceName=serviceName)

    def Create_portforwardEdit_Pload(self, action=None, reqID=None,
                                     ruleIndex=None, wanIndex=None, protocol=None,
                                     startRemotePort=None,
                                     ipAddr=None, startLocalPort=None, serviceName=None):

        pload = cfg.req_portforwardEdit
        payload = self.set_payload_with_action_reqID(pload=pload, action=action, reqID=reqID)

        return self.Add_Create_Edit_pload(payload, ruleIndex=ruleIndex, wanIndex=wanIndex, protocol=protocol,
                                          startRemotePort=startRemotePort, ipAddr=ipAddr, startLocalPort=startLocalPort,
                                          serviceName=serviceName)

    def portforwardCreateEdit(self, cookies=None, pload=None):
        response = self.request.post(url=self.url, headers=self.headersCurl, cookies=cookies, pload=pload)
        return response

    def portForward_Create_Default(self, cookie=None):
        idx = 0
        wanIndex = 0
        protocol = "TCP"
        startRePort = 1
        ipAddr = "192.168.1.5"
        startLoPort = 2
        serviceName = "Portforward_Default"

        pload = self.Create_portforwardCreate_pload(ruleIndex=idx, wanIndex=wanIndex,
                                                    protocol=protocol, startRemotePort=startRePort,
                                                    ipAddr=ipAddr, startLocalPort=startLoPort,
                                                    serviceName=serviceName)
        respone = self.portforwardCreateEdit(cookies=cookie, pload=pload)
        time.sleep(60)

class portforwardRemoveClient(BaseClient):
    def __init__(self):
        super().__init__()
        self.url = cfg.url_Agent
        self.request = API_lib()

    def Create_portforwardRemove_Pload(self, action=None, reqID=None, ruleIndex=None):
        pload = cfg.req_portforwardRemove
        payload = self.set_payload_with_action_reqID(pload=pload, action=action, reqID=reqID)

        if ruleIndex is not None:
            payload.update({'ruleIndex': ruleIndex})

        return payload

    def portforwardRemove(self, cookies=None, pload=None):
        if pload is None:
            payload = self.Create_portforwardRemove_Pload()
        else:
            payload = pload

        response = self.request.post(url=self.url, headers=self.headersCurl, cookies=cookies, pload=payload)
        return response

    def remove_all_port(self,  cookies=None):
        viewClt = portforwardViewClient()
        resBody = viewClt.portforwardView(cookies).body
        portResult = viewClt.get_result(resBody)
        for idx in range(len(portResult), 0, -1):
            pload = self.Create_portforwardRemove_Pload(ruleIndex=0)
            self.portforwardRemove(cookies=cookies, pload=pload)
            time.sleep(15)
