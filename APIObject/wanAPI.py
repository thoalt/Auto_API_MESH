"""
This moudle is for following API:
    - wanViewConfig
    - wanViewStatus
    - wanCreate
    - wanEdit
    - wanRemove
"""
import time

from assertpy import soft_assertions, assert_that

from APIObject.baseClient import BaseClient
from Config import config as cfg
from base.APILib import API_lib

class WAN_TYPE():
    DHCP = "IPoE Dynamic"
    STATIC = "IPoE Static"
    PPPoE = "PPPoE"
    L2TP = "L2TP"
    PPTP = "PPTP"

class IP_VER():
    IPv4 = "IPv4"
    IPv6 = "IPv6"
    DUAL = "Dualstack"


class WanViewConfigClient(BaseClient):
    def __init__(self):
        super().__init__()
        self.url = cfg.url_Agent
        self.request = API_lib()

    def Create_WanViewConfig_Pload(self, action=None, reqID=None):
        pload = cfg.req_wanViewConfig
        payload = self.set_payload_with_action_reqID(pload=pload, action=action, reqID=reqID)
        return payload

    def wanViewConfig(self, cookies=None, pload=None):
        if pload is None:
            payload = self.Create_WanViewConfig_Pload()
        else:
            payload = pload

        response = self.request.post(url=self.url, headers=self.headersCurl, cookies=cookies, pload=payload)
        return response

    def assert_result_WAN1(self, resBody, wanType=None, vlanID=None, ipVer=None,
                           IPV4Addr=None, IPV4Net=None, IPV4GW=None,
                           IPV6Addr=None, IPV6GW=None, ipv6Type=None,
                           dftRoute=None,
                           userName=None, passW=None, server=None
                           ):
        result = self.get_result(resBody)[1]
        with soft_assertions():
            if wanType is not None:
                assert_that(result['wanType'], description="WAN TYPE").is_equal_to(wanType)

            if vlanID is not None:
                assert_that(result['vlanId'], description="VLAN ID").is_equal_to(vlanID)

            if ipVer is not None:
                assert_that(result['ipVersion'], description="IP Version").is_equal_to(ipVer)

            if IPV4Addr is not None:
                assert_that(result['ipv4Address'], description="IPv4 Address").is_equal_to(IPV4Addr)

            if IPV4Net is not None:
                assert_that(result['ipv4Netmask'], description="IPv4 Netmask").is_equal_to(IPV4Net)

            if IPV4GW is not None:
                assert_that(result['ipv4Gateway'], description="IPv4 Gateway").is_equal_to(IPV4GW)

            if IPV6Addr is not None:
                assert_that(result['ipv6Address'], description="IPV6 Addr").is_equal_to(IPV6Addr)

            if IPV6GW is not None:
                assert_that(result['ipv6Gateway'], description="IPV6 GW").is_equal_to(IPV6GW)

            if ipv6Type is not None:
                assert_that(result['ipv6Type'], description="ipv6 Type").is_equal_to(ipv6Type)

            if dftRoute is not None:
                assert_that(result['defaultRoute'], description="Default Route").is_equal_to(dftRoute)

            if userName is not None:
                assert_that(result['username'], description="User Name").is_equal_to(userName)

            if passW is not None:
                assert_that(result['password'], description="Pass word").is_equal_to(passW)

            if server is not None:
                assert_that(result['networkServer'], description="Network Server").is_equal_to(server)

    def convert_wantype_API_to_GUI(self, wantypeAPI):
        if wantypeAPI == WAN_TYPE.DHCP:
            wanType = "DHCP Client"

        elif wantypeAPI == WAN_TYPE.STATIC:
            wanType = "Static"

        else:
            wanType = wantypeAPI
        return wanType

    def conver_IPVer_API_To_GUI(self, ipVerAPI):
        if ipVerAPI == IP_VER.DUAL:
            ipVer = "Dual stack"
        else:
            ipVer = ipVerAPI
        return ipVer

    def assert_result_WAN0(self, resBody, wanType=None, vlanID=None, ipVer=None,
                      IPV4Addr=None, IPV4Net=None, IPV4GW=None,
                      IPV6Addr=None, IPV6GW=None, ipv6Type=None,
                      dftRoute=None,
                      userName=None, passW=None, server=None
                      ):
        result = self.get_result(resBody)[0]
        with soft_assertions():
            if wanType is not None:
                assert_that(result['wanType'], description="WAN TYPE").is_equal_to(wanType)

            if vlanID is not None:
                assert_that(result['vlanId'], description="VLAN ID").is_equal_to(vlanID)

            if ipVer is not None:
                assert_that(result['ipVersion'], description="IP Version").is_equal_to(ipVer)

            if IPV4Addr is not None:
                assert_that(result['ipv4Address'], description="IPv4 Address").is_equal_to(IPV4Addr)

            if IPV4Net is not None:
                assert_that(result['ipv4Netmask'], description="IPv4 Netmask").is_equal_to(IPV4Net)

            if IPV4GW is not None:
                assert_that(result['ipv4Gateway'], description="IPv4 Gateway").is_equal_to(IPV4GW)

            if IPV6Addr is not None:
                assert_that(result['ipv6Address'], description="IPV6 Addr").is_equal_to(IPV6Addr)

            if IPV6GW is not None:
                assert_that(result['ipv6Gateway'], description="IPV6 GW").is_equal_to(IPV6GW)

            if ipv6Type is not None:
                assert_that(result['ipv6Type'], description="ipv6 Type").is_equal_to(ipv6Type)

            if dftRoute is not None:
                assert_that(result['defaultRoute'], description="Default Route").is_equal_to(dftRoute)

            if userName is not None:
                assert_that(result['username'], description="User Name").is_equal_to(userName)

            if passW is not None:
                assert_that(result['password'], description="Pass word").is_equal_to(passW)

            if server is not None:
                assert_that(result['networkServer'], description="Network Server").is_equal_to(server)

    def assert_result_WAN2(self, resBody, wanType=None, vlanID=None, ipVer=None,
                      IPV4Addr=None, IPV4Net=None, IPV4GW=None,
                      IPV6Addr=None, IPV6GW=None, ipv6Type=None,
                      dftRoute=None,
                      userName=None, passW=None, server=None
                      ):
        result = self.get_result(resBody)[2]
        with soft_assertions():
            if wanType is not None:
                assert_that(result['wanType'], description="WAN TYPE").is_equal_to(wanType)

            if vlanID is not None:
                assert_that(result['vlanId'], description="VLAN ID").is_equal_to(vlanID)

            if ipVer is not None:
                assert_that(result['ipVersion'], description="IP Version").is_equal_to(ipVer)

            if IPV4Addr is not None:
                assert_that(result['ipv4Address'], description="IPv4 Address").is_equal_to(IPV4Addr)

            if IPV4Net is not None:
                assert_that(result['ipv4Netmask'], description="IPv4 Netmask").is_equal_to(IPV4Net)

            if IPV4GW is not None:
                assert_that(result['ipv4Gateway'], description="IPv4 Gateway").is_equal_to(IPV4GW)

            if IPV6Addr is not None:
                assert_that(result['ipv6Address'], description="IPV6 Addr").is_equal_to(IPV6Addr)

            if IPV6GW is not None:
                assert_that(result['ipv6Gateway'], description="IPV6 GW").is_equal_to(IPV6GW)

            if ipv6Type is not None:
                assert_that(result['ipv6Type'], description="ipv6 Type").is_equal_to(ipv6Type)

            if dftRoute is not None:
                assert_that(result['defaultRoute'], description="Default Route").is_equal_to(dftRoute)

            if userName is not None:
                assert_that(result['username'], description="User Name").is_equal_to(userName)

            if passW is not None:
                assert_that(result['password'], description="Pass word").is_equal_to(passW)

            if server is not None:
                assert_that(result['networkServer'], description="Network Server").is_equal_to(server)

    def assert_result_WAN3(self, resBody, wanType=None, vlanID=None, ipVer=None,
                      IPV4Addr=None, IPV4Net=None, IPV4GW=None,
                      IPV6Addr=None, IPV6GW=None, ipv6Type=None,
                      dftRoute=None,
                      userName=None, passW=None, server=None
                      ):
        result = self.get_result(resBody)[3]
        with soft_assertions():
            if wanType is not None:
                assert_that(result['wanType'], description="WAN TYPE").is_equal_to(wanType)

            if vlanID is not None:
                assert_that(result['vlanId'], description="VLAN ID").is_equal_to(vlanID)

            if ipVer is not None:
                assert_that(result['ipVersion'], description="IP Version").is_equal_to(ipVer)

            if IPV4Addr is not None:
                assert_that(result['ipv4Address'], description="IPv4 Address").is_equal_to(IPV4Addr)

            if IPV4Net is not None:
                assert_that(result['ipv4Netmask'], description="IPv4 Netmask").is_equal_to(IPV4Net)

            if IPV4GW is not None:
                assert_that(result['ipv4Gateway'], description="IPv4 Gateway").is_equal_to(IPV4GW)

            if IPV6Addr is not None:
                assert_that(result['ipv6Address'], description="IPV6 Addr").is_equal_to(IPV6Addr)

            if IPV6GW is not None:
                assert_that(result['ipv6Gateway'], description="IPV6 GW").is_equal_to(IPV6GW)

            if ipv6Type is not None:
                assert_that(result['ipv6Type'], description="ipv6 Type").is_equal_to(ipv6Type)

            if dftRoute is not None:
                assert_that(result['defaultRoute'], description="Default Route").is_equal_to(dftRoute)

            if userName is not None:
                assert_that(result['username'], description="User Name").is_equal_to(userName)

            if passW is not None:
                assert_that(result['password'], description="Pass word").is_equal_to(passW)

            if server is not None:
                assert_that(result['networkServer'], description="Network Server").is_equal_to(server)


    def assert_result_list(self, resBodyLst, wanType=None, vlanID=None, ipVer=None,
                      IPV4Addr=None, IPV4Net=None, IPV4GW=None,
                      IPV6Addr=None, IPV6GW=None, ipv6Type=None,
                      dftRoute=None,
                      userName=None, passW=None, server=None
                      ):
        with soft_assertions():
            for resBody in resBodyLst:
                self.assert_result_WAN1(resBody, wanType, vlanID, ipVer,
                                        IPV4Addr, IPV4Net, IPV4GW,
                                        IPV6Addr, IPV6GW, ipv6Type,
                                        dftRoute,
                                        userName, passW, server)

class WanCreateEditClient(BaseClient):
    def __init__(self):
        super().__init__()
        self.url = cfg.url_Agent
        self.request = API_lib()

    def Create_WanCreate_Common_Pload(self, action=None, reqID=None, wanIdx=None, wanType=None):
        pload = cfg.req_wanCreate
        payload = self.set_payload_with_action_reqID(pload=pload, action=action, reqID=reqID)
        if wanIdx is not None:
            payload['wanIndex'] = wanIdx
        else:
            payload['wanIndex'] = pload['wanIndex']

        if wanType is not None:
            payload['wanType'] = wanType
        else:
            payload['wanType'] = pload['wanType']

        return payload

    def Create_WanEdit_Common_Pload(self, action=None, reqID=None, wanIdx=None, wanType=None):
        pload = cfg.req_wanEdit
        payload = self.set_payload_with_action_reqID(pload=pload, action=action, reqID=reqID)
        if wanIdx is not None:
            payload['wanIndex'] = wanIdx
        else:
            payload['wanIndex'] = pload['wanIndex']

        if wanType is not None:
            payload['wanType'] = wanType
        else:
            payload['wanType'] = pload['wanType']
        return payload

    def Create_WanCreate_Edit_DHCP_pload(self, pload, vlanID=None, IPVer=None):
        if vlanID is not None:
            pload.update({'vlanId': vlanID})

        if IPVer is not None:
            pload.update({'ipVersion': IPVer})
        return pload

    def Create_WanCreate_Edit_WAN_IPV4_pload(self, pload, vlanID=None, IPVer=None,
                                             IPV4Addr=None, IPV4Net=None, IPV4GW=None):
        if vlanID is not None:
            pload.update({'vlanId': vlanID})

        if IPVer is not None:
            pload.update({'ipVersion': IPVer})

        if IPV4Addr is not None:
            pload.update({'ipv4Address': IPV4Addr})

        if IPV4Net is not None:
            pload.update({'ipv4Netmask': IPV4Net})

        if IPV4GW is not None:
            pload.update({'ipv4Gateway': IPV4GW})

        return pload

    def Create_WanCreate_Edit_WAN_IPV6_pload(self, pload, vlanID=None, IPVer=None,
                                             IPV6Addr=None, IPV6GW=None, ipv6Type=None,
                                             dftRoute=None):
        if vlanID is not None:
            pload.update({'vlanId': vlanID})

        if IPVer is not None:
            pload.update({'ipVersion': IPVer})

        if IPV6Addr is not None:
            pload.update({'ipv6Address': IPV6Addr})

        if IPV6GW is not None:
            pload.update({'ipv6Gateway': IPV6GW})

        if ipv6Type is not None:
            pload.update({'ipv6Type': ipv6Type})

        if dftRoute is not None:
            pload.update({'defaultRoute': dftRoute})

        return pload

    def Create_WanCreate_Edit_WAN_Dual_pload(self, pload, vlanID=None, IPVer=None,
                                             IPV4Addr=None, IPV4Net=None, IPV4GW=None,
                                             IPV6Addr=None, IPV6GW=None, ipv6Type=None,
                                             dftRoute=None):
        if vlanID is not None:
            pload.update({'vlanId': vlanID})

        if IPVer is not None:
            pload.update({'ipVersion': IPVer})

        if IPV4Addr is not None:
            pload.update({'ipv4Address': IPV4Addr})

        if IPV4Net is not None:
            pload.update({'ipv4Netmask': IPV4Net})

        if IPV4GW is not None:
            pload.update({'ipv4Gateway': IPV4GW})

        if vlanID is not None:
            pload.update({'vlanId': vlanID})

        if IPVer is not None:
            pload.update({'ipVersion': IPVer})

        if IPV6Addr is not None:
            pload.update({'ipv6Address': IPV6Addr})

        if IPV6GW is not None:
            pload.update({'ipv6Gateway': IPV6GW})

        if ipv6Type is not None:
            pload.update({'ipv6Type': ipv6Type})

        if dftRoute is not None:
            pload.update({'defaultRoute': dftRoute})

        return pload

    def Create_WanCreate_Edit_WAN_PPPoE(self, pload, vlanID=None, IPVer=None, userName=None, passW=None , dftRoute=None):
        if vlanID is not None:
            pload.update({'vlanId': vlanID})

        if IPVer is not None:
            pload.update({'ipVersion': IPVer})

        if userName is not None:
            pload.update({'username': userName})

        if passW is not None:
            pload.update({'password': passW})

        if dftRoute is not None:
            pload.update({'defaultRoute': dftRoute})

        return pload

    def Create_WanCreate_Edit_WAN_PPTP(self, pload, vlanID=None, server=None, userName=None, pword=None):
        if vlanID is not None:
            pload.update({'vlanId': vlanID})

        if server is not None:
            pload.update({'networkServer': server})

        if userName is not None:
            pload.update({'username': userName})

        if pword is not None:
            pload.update({'password': pword})
        return pload

    def Create_WanCreate_Edit_WAN_L2TP(self, pload, vlanID=None, server=None, userName=None, pword=None):
        if vlanID is not None:
            pload.update({'vlanId': vlanID})

        if server is not None:
            pload.update({'networkServer': server})

        if userName is not None:
            pload.update({'username': userName})

        if pword is not None:
            pload.update({'password': pword})
        return pload

    def wanCreateEdit(self, cookies=None, pload=None):
        response = self.request.post(url=self.url, headers=self.headersCurl, cookies=cookies, pload=pload)
        return response

    def Create_All_Wan(self, cookies=None):
        wanID_lst = []
        viewClt = WanViewConfigClient()
        viewResult = self.get_result(viewClt.wanViewConfig(cookies).body)
        for item in viewResult:
            wanID = item['wanIndex']
            if wanID != 0:
                wanID_lst.append(wanID)

        for idx in range(1, 4):
            if idx not in wanID_lst:
                ploadCom = self.Create_WanCreate_Common_Pload(
                    wanIdx=idx,
                    wanType=WAN_TYPE.DHCP
                )
                pload = self.Create_WanCreate_Edit_DHCP_pload(
                    pload=ploadCom,
                    vlanID=100 + idx,
                    IPVer=IP_VER.IPv4
                )
                response = self.request.post(url=self.url, headers=self.headersCurl, cookies=cookies, pload=pload)
                time.sleep(45)

        del viewClt

    def Create_DHCP_IPv4(self, cookies=None, index=None, vlanId=None):
        ploadCom = self.Create_WanCreate_Common_Pload(
            wanIdx=index,
            wanType=WAN_TYPE.DHCP
        )
        pload = self.Create_WanCreate_Edit_DHCP_pload(
            pload=ploadCom,
            vlanID=vlanId,
            IPVer=IP_VER.IPv4
        )
        response = self.request.post(url=self.url, headers=self.headersCurl, cookies=cookies, pload=pload)
        time.sleep(45)

    def Create_DHCP_IPv6(self, cookies=None, index=None, vlanId=None):
        ploadCom = self.Create_WanCreate_Common_Pload(
            wanIdx=index,
            wanType=WAN_TYPE.DHCP
        )
        pload = self.Create_WanCreate_Edit_DHCP_pload(
            pload=ploadCom,
            vlanID=vlanId,
            IPVer=IP_VER.IPv6
        )
        response = self.request.post(url=self.url, headers=self.headersCurl, cookies=cookies, pload=pload)
        time.sleep(45)

    def Create_DHCP_Dual(self, cookies=None, index=None, vlanId=None):
        ploadCom = self.Create_WanCreate_Common_Pload(
            wanIdx=index,
            wanType=WAN_TYPE.DHCP
        )
        pload = self.Create_WanCreate_Edit_DHCP_pload(
            pload=ploadCom,
            vlanID=vlanId,
            IPVer=IP_VER.DUAL
        )
        response = self.request.post(url=self.url, headers=self.headersCurl, cookies=cookies, pload=pload)
        time.sleep(45)
        return response


    def Create_STATIC_IPv4(self, cookies=None, index=None, vlanId=None, IPV4Addr=None, IPV4Net=None, IPV4GW=None):
        ploadCom = self.Create_WanCreate_Common_Pload(
            wanIdx=index,
            wanType=WAN_TYPE.STATIC
        )
        pload = self.Create_WanCreate_Edit_WAN_IPV4_pload(
            pload=ploadCom,
            vlanID=vlanId,
            IPVer=IP_VER.IPv4,
            IPV4Addr=IPV4Addr,
            IPV4Net=IPV4Net,
            IPV4GW=IPV4GW
        )
        response = self.request.post(url=self.url, headers=self.headersCurl, cookies=cookies, pload=pload)
        time.sleep(45)

    def Create_STATIC_IPv6(self, cookies=None, index=None, vlanId=None, IPV6Addr=None, IPV6GW=None, ipv6Type=None, dftRoute=None):
        ploadCom = self.Create_WanCreate_Common_Pload(
            wanIdx=index,
            wanType=WAN_TYPE.STATIC
        )
        pload = self.Create_WanCreate_Edit_WAN_IPV6_pload(
            pload=ploadCom,
            vlanID=vlanId,
            IPVer=IP_VER.IPv6,
            IPV6Addr=IPV6Addr,
            IPV6GW=IPV6GW,
            ipv6Type=ipv6Type,
            dftRoute=dftRoute
        )
        response = self.request.post(url=self.url, headers=self.headersCurl, cookies=cookies, pload=pload)
        time.sleep(45)

    def Create_STATIC_DUAL(self, cookies=None, index=None, vlanId=None,
                            IPV4Addr=None, IPV4Net=None, IPV4GW=None,
                            IPV6Addr=None, IPV6GW=None, ipv6Type=None, dftRoute=None):
        ploadCom = self.Create_WanCreate_Common_Pload(
            wanIdx=index,
            wanType=WAN_TYPE.STATIC
        )
        pload = self.Create_WanCreate_Edit_WAN_Dual_pload(
            pload=ploadCom,
            vlanID=vlanId,
            IPVer=IP_VER.DUAL,
            IPV4Addr=IPV4Addr,
            IPV4Net=IPV4Net,
            IPV4GW=IPV4GW,
            IPV6Addr=IPV6Addr,
            IPV6GW=IPV6GW,
            ipv6Type=ipv6Type,
            dftRoute=dftRoute
        )
        response = self.request.post(url=self.url, headers=self.headersCurl, cookies=cookies, pload=pload)
        time.sleep(45)

    def Create_PPPoE_IPV4(self, cookies=None, index=None, vlanID=None,
                           userName=None, passW=None):

        ploadCom = self.Create_WanCreate_Common_Pload(
            wanIdx=index,
            wanType=WAN_TYPE.PPPoE
        )
        pload = self.Create_WanCreate_Edit_WAN_PPPoE(
            pload=ploadCom,
            vlanID=vlanID,
            IPVer=IP_VER.IPv4,
            userName=userName,
            passW=passW
        )
        response = self.request.post(url=self.url, headers=self.headersCurl, cookies=cookies, pload=pload)
        time.sleep(45)

    def Create_PPPoE_IPV6(self, cookies=None, index=None, vlanID=None,
                          userName=None, passW=None):
        ploadCom = self.Create_WanCreate_Common_Pload(
            wanIdx=index,
            wanType=WAN_TYPE.PPPoE
        )
        pload = self.Create_WanCreate_Edit_WAN_PPPoE(
            pload=ploadCom,
            vlanID=vlanID,
            IPVer=IP_VER.IPv6,
            userName=userName,
            passW=passW
        )
        response = self.request.post(url=self.url, headers=self.headersCurl, cookies=cookies, pload=pload)
        time.sleep(45)

    def Create_PPPoE_DUAL(self, cookies=None, index=None, vlanID=None,
                          userName=None, passW=None, dftRoute=None):
        ploadCom = self.Create_WanCreate_Common_Pload(
            wanIdx=index,
            wanType=WAN_TYPE.PPPoE
        )
        pload = self.Create_WanCreate_Edit_WAN_PPPoE(
            pload=ploadCom,
            vlanID=vlanID,
            IPVer=IP_VER.DUAL,
            userName=userName,
            passW=passW,
            dftRoute=dftRoute
        )
        response = self.request.post(url=self.url, headers=self.headersCurl, cookies=cookies, pload=pload)
        time.sleep(45)

    def Create_L2TP(self, cookies=None, index=None,
                    server=None, userName=None, pword=None):

        ploadCom = self.Create_WanCreate_Common_Pload(
            wanIdx=index,
            wanType=WAN_TYPE.L2TP
        )

        pload = self.Create_WanCreate_Edit_WAN_L2TP(
            pload=ploadCom,
            server=server,
            userName=userName,
            pword=pword
        )
        response = self.request.post(url=self.url, headers=self.headersCurl, cookies=cookies, pload=pload)
        time.sleep(45)

    def Create_PPTP(self, cookies=None, index=None,
                    server=None, userName=None, pword=None):
        ploadCom = self.Create_WanCreate_Common_Pload(
            wanIdx=index,
            wanType=WAN_TYPE.PPTP
        )

        pload = self.Create_WanCreate_Edit_WAN_PPTP(
            pload=ploadCom,
            server=server,
            userName=userName,
            pword=pword
        )
        response = self.request.post(url=self.url, headers=self.headersCurl, cookies=cookies, pload=pload)
        time.sleep(45)

class WanRemoveClient(BaseClient):
    def __init__(self):
        super().__init__()
        self.url = cfg.url_Agent
        self.request = API_lib()

    def Create_WanRemove_Pload(self, action=None, wanIndex=None, reqID=None):
        pload = cfg.req_wanRemove
        payload = self.set_payload_with_action_reqID(pload=pload, action=action, reqID=reqID)

        if wanIndex is not None:
            payload['wanIndex'] = wanIndex
        else:
            payload['wanIndex'] = pload['wanIndex']

        return payload

    def wanRemove(self, cookies=None, pload=None):
        if pload is None:
            payload = self.Create_WanRemove_Pload()
        else:
            payload = pload

        response = self.request.post(url=self.url, headers=self.headersCurl, cookies=cookies, pload=payload)
        return response

    def Remove_All_WAN(self, cookies=None):
        wanID_lst = []
        viewClt = WanViewConfigClient()
        viewResult = self.get_result(viewClt.wanViewConfig(cookies).body)
        for item in viewResult:
            wanID = item['wanIndex']
            if wanID != 0:
                wanID_lst.append(wanID)

        numWan = len(wanID_lst)
        if numWan > 0:
            for idx in wanID_lst:
                payload = self.Create_WanRemove_Pload(wanIndex=idx)
                response = self.wanRemove(cookies=cookies, pload=payload)
                time.sleep(45)
        del viewClt

class WanViewStatusClient(BaseClient):
    def __init__(self):
        super().__init__()
        self.url = cfg.url_Agent
        self.request = API_lib()

    def Create_WanViewStatus_Pload(self, action=None, reqID=None):
        pload = cfg.req_wanViewStatus
        payload = self.set_payload_with_action_reqID(pload=pload, action=action, reqID=reqID)
        return payload

    def wanViewStatus(self, cookies=None, pload=None):
        if pload is None:
            payload = self.Create_WanViewStatus_Pload()
        else:
            payload = pload

        response = self.request.post(url=self.url, headers=self.headersCurl, cookies=cookies, pload=payload)
        return response
