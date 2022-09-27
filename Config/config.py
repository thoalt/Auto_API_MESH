IP_ADDR_CAP = "192.168.88.1"
CLIENT_MAC = "00:0E:C6:59:A1:A6"
SALT = "D2...40."
STR_ENCRYPT = "VNPT"
SERIAL = "1292922130B4454"

SERVER_BROADCAST = "255.255.255.255"
PORT_BROADCAST = 9000

SSID = "API_TEST_ThoaLT"
PASSWORD = "1234567890"
auth = "WPA2PSK"
encrypt = "AES"
GUID = "{829d9c08-9781-498b-8677-4cecbddc1c1d}"

CAP_MAC = "A4:F4:C2:0B:44:54"
MRE1_MAC = "A4:F4:C2:0B:44:68"
MRE2_MAC = ""

BSSIDList_MeshOnly = [
    "A4:F4:C2:0B:44:55",
    "A4:F4:C2:0B:44:56",
    "A4:F4:C2:0B:44:69",
    "A4:F4:C2:0B:44:6A"
]

BSSIDList_MeshONT = [
    "A4:F4:C2:0B:44:55",
    "A4:F4:C2:0B:44:56",
    "A4:F4:C2:0B:44:69",
    "A4:F4:C2:0B:44:6A"
]

MIN_TIMEOUT = 2
MAX_TIMEOUT = 30
AVG_TIMEOUT = 10

USER_SSH = "root"
PASS_SSH = "VNPT@88Tech"
PORT_NUM = "22"

url_Login = f"https://{IP_ADDR_CAP}:9000/onelinklogin"
url_Agent = f"https://{IP_ADDR_CAP}:9000/onelinkagent"
url_Broadcast = f"https://255.255.255.255:9000"

# GUI INFORMATION
CAP_URL = f"http://{IP_ADDR_CAP}/"
USER_GUI = "root"
PASS_GUI = "VNPT"

req_discovery = {
    "action": "discovery",
    "clientMac": "<clientMac>",
    "authenString": "<authenString>",
    "requestId": "<requestId>"
}

req_openSession = {
    "action": "openSession",
    "clientMac": "<clientMac>",
    "authenString": "<authenString>",
    "requestId": "<requestId>"
}

req_logout = {
    "action": "logout",
    "requestId": "<requestId>"
}

req_reboot = {
    "action": "reboot",
    "macList": "<macList>",
    "requestId": "<requestId>"
}

req_reset = {
    "action": "reset",
    "macList": "<macList>",
    "requestId": "<requestId>"
}

req_lanview = {
    "action": "lanView",
    "requestId": "<requestId>"
}

req_radio2GView = {
    "action": "radio2.4GView",
    "requestId": "<requestId>"
}

req_radio2GEdit = {
    "action": "radio2.4GEdit",
    "requestId": "<requestId>",
    "channel": "<2.4GChannel>",
    "bandwidth": "<2.4GBandwidth>"
}

req_radio5GView = {
    "action": "radio5GView",
    "requestId": "<requestId>"
}

req_radio5GEdit = {
    "action": "radio5GEdit",
    "requestId": "<requestId>",
    "channel": "<5GChannel>",
    "bandwidth": "<5GBandwidth>"
}

req_deviceInfoView = {
    "action": "deviceInfoView",
    "requestId": "<requestId>"
}

req_networkinfoView = {
    "action": "networkinfoView",
    "requestId": "<requestId>"
}

req_passwordEdit = {
    "action": "passwordEdit",
    "username": "<username>",
    "password": "<password>",
    "requestId": "<requestId>"
}

req_speedtest = {
    "action": "speedtest",
    "requestId": "<requestId>"
}

req_ping = {
    "action": "ping",
    "pingCode": 1,
    "host": "<host domain name or IP address>",
    "requestId": "<requestId>"
}

req_traceroute = {
    "action": "traceroute",
    "tracerouteCode": 1,
    "host": "<host domain name or IP address>",
    "requestId": "<requestId>"
}

req_topology = {
    "action": "topology",
    "requestId": "<requestId>"
}

req_addNewNode = {
    "action": "addNewNode",
    "requestId": "<requestId>"
}

req_syncONTConfig = {
    "action": "syncONTConfig",
    "requestId": "<requestId>",
    "enableSync": False
}

req_lanEdit = {
    "action": "lanEdit",
    "ipAddr": "<ipAddr>",
    "subnetMask": "<subnetMask>",
    "requestId": "<requestId>"
}

req_wanViewConfig = {
    "action": "wanViewConfig",
    "requestId": "<requestId>"
}

req_wanViewStatus = {
    "action": "wanViewStatus",
    "requestId": "<requestId>"
}

req_wanCreate = {
    "action": "wanCreate",
    "wanIndex": "<wanIndex>",
    "wanType": "<wanType>",
    "requestId": "<requestId>"
}

req_wanEdit = {
    "action": "wanEdit",
    "wanIndex": "<wanIndex>",
    "wanType": "<wanType>",
    "requestId": "<requestId>"
}

req_wanRemove = {
    "action": "wanRemove",
    "wanIndex": "<wanIndex>",
    "requestId": "<requestId>"
}

req_ssid2GView = {
    "action": "ssid2.4GView",
    "requestId": "<requestId>"
}

req_ssid5GView = {
    "action": "ssid5GView",
    "requestId": "<requestId>"
}

req_ssid2GEdit = {
    "action": "ssid2.4GEdit",
    "ssidIndex": "<ssidIndex>",
    "enable": "<enable>",
    "ssid": "<ssid>",
    "authenMode": "<authenMode>",
    "password": "<password>",
    "requestId": "<requestId>"
}

req_ssid5GEdit = {
    "action": "ssid5GEdit",
    "ssidIndex": "<ssidIndex>",
    "enable": "<enable>",
    "ssid": "<ssid>",
    "authenMode": "<authenMode>",
    "password": "<password>",
    "requestId": "<requestId>"
}

req_portforwardView = {
    "action": "portforwardView",
    "requestId": "<requestId>"
}

req_portforwardCreate = {
    "action": "portforwardCreate",
    "ruleIndex": "<ruleIndex>",
    "wanName": "<wanName>",
    "protocol": "<protocol>",
    "startRemotePort": "<startRemotePort>",
    "ipAddr": "<ipAddr>",
    "startLocalPort": "<startLocalPort>",
    "requestId": "<requestId>"
}

req_portforwardEdit = {
    "action": "portforwardEdit",
    "ruleIndex": "<ruleIndex>",
    "wanName": "<wanName>",
    "protocol": "<protocol>",
    "startRemotePort": "<startRemotePort>",
    "ipAddr": "<ipAddr>",
    "startLocalPort": "<startLocalPort>",
    "requestId": "<requestId>"
}

req_ddnsView = {
    "action": "ddnsView",
    "requestId": "<requestId>"
}

req_ddnsCreate = {
    "action": "ddnsCreate",
    "index": "<index>",
    "serviceProvider": "<serviceProvider>",
    "hostname": "<hostname>",
    "username": "<username>",
    "password": "<password>",
    "requestId": "<requestId>"
}

req_ddnsEdit = {
    "action": "ddnsEdit",
    "index": "<index>",
    "serviceProvider": "<serviceProvider>",
    "hostname": "<hostname>",
    "username": "<username>",
    "password": "<password>",
    "requestId": "<requestId>"
}

req_ddnsRemove = {
    "action": "ddnsRemove",
    "index": "<index>",
    "requestId": "<requestId>"
}

req_meshView = {
    "action": "meshView",
    "requestId": "<requestId>"
}

req_meshCreate = {
    "action": "meshCreate",
    "requestId": "<requestId>",
    "meshMode": 0,
    "addNode": True
}

req_meshChange = {
    "action": "meshChange",
    "requestId": "<requestId>",
    "meshMode": 0
}

req_restoreConfig = {
    "action": "restoreConfig",
    "fileName": "<config’s file name>",
    "md5sum": "<Md5sum>",
    "requestId": "<requestId>"
}

req_backupConfig = {
    "action": "backupConfig",
    "requestId": "<requestId>"
}

req_upgradeFirmware = {
    "action": "upgradeFirmware",
    "macList": "<macList>",
    "fileName": "<firmware’s file name>",
    "md5sum": "<Md5sum>",
    "requestId": "<requestId>"
}

req_updateDatabase = {
    "action": "updateDatabase",
    "status": "Requested",
    "fileName": "<database’s file name>",
    "md5sum": "<Md5sum>",
    "requestId": "<requestId>"
}