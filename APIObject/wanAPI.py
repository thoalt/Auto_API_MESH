"""
This moudle is for following API:
    - wanViewConfig
    - wanViewStatus
    - wanCreate
    - wanEdit
    - wanRemove
"""
from APIObject.baseClient import BaseClient
from Config import config as cfg
from base.APILib import API_lib


class WanViewConfigClient(BaseClient):
    def __init__(self):
        super().__init__()
        self.url = cfg.url_Agent
        self.request = API_lib()

    def Create_WanView_Pload(self, action=None, reqID=None):
        pload = cfg.req_wanViewConfig
        payload = self.set_payload_with_action_reqID(pload=pload, action=action, reqID=reqID)
        return payload

    def wanViewConfig(self, cookies=None, pload=None):
        if pload is None:
            payload = self.Create_WanView_Pload()
        else:
            payload = pload

        response = self.request.post(url=self.url, headers=self.headersCurl, cookies=cookies, pload=payload)
        return response

class WanCreateEditClient(BaseClient):
    def __init__(self):
        super().__init__()
        self.url = cfg.url_Agent
        self.request = API_lib

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
            pload.update({'defaultRoute': ipv6Type})

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
            pload.update({'defaultRoute': ipv6Type})

        return pload

    def Create_WanCreate_Edit_WAN_PPPoE(self, pload, vlanID=None, IPVer=None, userName=None, passW=None):
        if vlanID is not None:
            pload.update({'vlanId': vlanID})

        if IPVer is not None:
            pload.update({'ipVersion': IPVer})

        if userName is not None:
            pload.update({'username': userName})

        if passW is not None:
            pload.update({'password': passW})

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

class WanRemoveClient(BaseClient):
    def __init__(self):
        super().__init__()
        self.url = cfg.url_Agent
        self.request = API_lib()

    def Create_WanRemove_Pload(self, action=None, wanIndex=None, reqID=None):
        pload = cfg.req_wanViewConfig
        payload = self.set_payload_with_action_reqID(pload=pload, action=action, reqID=reqID)

        if wanIndex is not None:
            payload['wanIndex'] = wanIndex
        else:
            payload['wanIndex'] = pload['wanIndex']

        return payload

    def wanViewConfig(self, cookies=None, pload=None):
        if pload is None:
            payload = self.Create_WanRemove_Pload()
        else:
            payload = pload

        response = self.request.post(url=self.url, headers=self.headersCurl, cookies=cookies, pload=payload)
        return response

class WanViewStatusClient(BaseClient):
    def __init__(self):
        super().__init__()
        self.url = cfg.url_Agent
        self.request = API_lib()

    def Create_WanView_Pload(self, action=None, reqID=None):
        pload = cfg.req_wanViewConfig
        payload = self.set_payload_with_action_reqID(pload=pload, action=action, reqID=reqID)
        return payload

    def wanViewConfig(self, cookies=None, pload=None):
        if pload is None:
            payload = self.Create_WanView_Pload()
        else:
            payload = pload

        response = self.request.post(url=self.url, headers=self.headersCurl, cookies=cookies, pload=payload)
        return response