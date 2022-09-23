schema_common = {
    'status': {'type': 'integer'},
    'message': {'type': 'string'},
    'requestId': {'type': 'integer'},
    'data': {
        'type': 'dict',
        'schema': {
            'action': {'type': 'string'},
            'results': {'type': 'list'}
        }
    }
}

schema_topo_common = {
    'status': {'type': 'integer'},
    'message': {'type': 'string'},
    'requestId': {'type': 'integer'},
    'data': {
        'type': 'dict',
        'schema': {
            'action': {'type': 'string'},
            'nodeNum': {'type': 'integer'},
            'clientNum': {'type': 'integer'},
            'results': {'type': 'list'}
        }
    }
}

schema_lanView_common = {
    "status": {'type': 'int'},
    "message": {'type': 'string'},
    "requestId": {'type': 'string'},
    "data": {
        'type': 'dict',
        'schema': {
            'action': {'type': 'string'},
            'lanList': {'type': 'list'}
        }
    }
}

schema_lanView_result = {
    "ipAddr": {'type': 'string'},
    "subnetMask": {'type': 'string'}
}


schema_wanViewConfig_result = {
    "wanIndex": {'type': 'string'},
    "wanType": {'type': 'string'},
    "vlanId": {'type': 'string'},
    "ipVersion": {'type': 'string'},
    "username": {'type': 'string'},
    "password": {'type': 'string'},
    "defaultRoute": {'type': 'string'},
}

schema_radio24GView_result = {
    "enable": {'type': 'boolean'},
    "channel": {'type': 'string'},
    "bandwidth": {'type': 'string'}
}

schema_radio5GView_result = {
    "enable": {'type': 'boolean'},
    "channel": {'type': 'string'},
    "bandwidth": {'type': 'string'}
}

schema_ssidView_result = {
    "ssidName": {'type': 'string'},
    "authenMode": {'type': 'string'},
    "password": {'type': 'string'}
}

schema_guest24GView_result = {
    "enable": {'type': 'string'},
    "ssidName": {'type': 'string'},
    "authenMode": {'type': 'string'},
    "password": {'type': 'string'}
}

schema_guest5GView_result = {
    "enable": {'type': 'string'},
    "ssidName": {'type': 'string'},
    "authenMode": {'type': 'string'},
    "password": {'type': 'string'}
}

schema_repeater24GView_result = {
    "enable": {'type': 'string'},
    "ssidName": {'type': 'string'},
    "bssid": {'type': 'string'},
    "authenMode": {'type': 'string'},
    "password": {'type': 'string'}
}

schema_repeater5GView_result = {
    "enable": {'type': 'string'},
    "ssidName": {'type': 'string'},
    "bssid": {'type': 'string'},
    "authenMode": {'type': 'string'},
    "password": {'type': 'string'}
}

schema_portforwardView_result = {
    "wanName": {'type': 'string'},
    "ruleIndex": {'type': 'string'},
    "protocol": {'type': 'string'},
    "startRemotePort": {'type': 'string'},
    "endRemotePort": {'type': 'string'},
    "ipAddr": {'type': 'string'},
    "startLocalPort": {'type': 'string'}
}

schema_ddnsView_result = {
    "index": {'type': 'string'},
    "serviceProvider": {'type': 'string'},
    "hostname": {'type': 'string'},
    "username": {'type': 'string'},
    "password": {'type': 'string'}
}

schema_deviceInfoView_result = {
    "firmwareVersion": {'type': 'string'},
    "buildTimestamp": {'type': 'string'},
    "deviceMac": {'type': 'string'},
    "serial": {'type': 'string'},
    "deviceUptime": {'type': 'string'},
    "deviceName": {'type': 'string'},
    "deviceLocation": {'type': 'string'},
    "linkState": {'type': 'string'},
    "modelName": {'type': 'string'},
    "hardwareVersion": {'type': 'string'}
}


schema_wanViewStatus_result = {
    "wanIndex": {'type': 'string'},
    "wanStatus": {'type': 'string'},
    "wanipv4Addr": {'type': 'string'},
    "wanipv6Addr": {'type': 'string'}
}

schema_networkinfoView_result = {
    "statusV4": {'type': 'string'},
    "ipAddrV4": {'type': 'string'},
    "defaultGatewayV4": {'type': 'string'},
    "statusV6": {'type': 'string'},
    "ipAddrV6": {'type': 'string'},
    "defaultGateway6": {'type': 'string'}
}

schema_topology_result = {
    "nodeName": {'type': 'string'},
    "modelName": {'type': 'string'},
    "firmwareVersion": {'type': 'string'},
    "nodeMac": {'type': 'string'},
    "serialNumber": {'type': 'string'},
    "nodeIp": {'type': 'string'},
    "deviceType": {'type': 'integer'},
    "connectType": {'type': 'integer'},
    "nodeRssi": {'type': 'integer'},
    "hardwareVersion": {'type': 'string'},
    "location": {'type': 'string'},
    "upstream": {'type': 'string'},
    "nodeTxrate": {'type': 'string'},
    "nodeRxrate": {'type': 'string'},
    "clientInfo": {'type': 'list'}
}

schema_topology_clientInfo = {
    "hostName": {'type': 'string'},
    "interfaceType": {'type': 'integer'},
    "clientIp": {'type': 'string'},
    "clientMac": {'type': 'string'},
    "clientRssi": {'type': 'integer'},
    "status": {'type': 'boolean'},
    "clientTxrate": {'type': 'string'},
    "clientRxrate": {'type': 'string'}
}

schema_ping_result = {
    "pingCode": {'type': 'string'},
    "host": {'type': 'string'},
    "hostAddress": {'type': 'string'},
    "successCount": {'type': 'string'},
    "failureCount": {'type': 'string'},
    "averageResponseTime": {'type': 'string'},
    "minimumResponseTime": {'type': 'string'},
    "maximumResponseTime": {'type': 'string'},
    "jitter": {'type': 'string'}
}

schema_speedtest_result = {
    "speedtestCode": {'type': 'string'},
    "downloadSpeed": {'type': 'string'},
    "uploadSpeed": {'type': 'string'},
    "latency": {'type': 'string'}
}


schema_lanEdit = {
    "status": {'type': 'int'},
    "message": {'type': 'string'},
    "requestId": {'type': 'string'},
    "data": {'type': 'dict'}
}

schema_wanCreate = {
    "status": {'type': 'int'},
    "message": {'type': 'string'},
    "requestId": {'type': 'string'},
    "data": {'type': 'dict'}
}

schema_wanEdit = {
    "status": {'type': 'int'},
    "message": {'type': 'string'},
    "requestId": {'type': 'string'},
    "data": {'type': 'dict'}
}

schema_wanRemove = {
    "status": {'type': 'int'},
    "message": {'type': 'string'},
    "requestId": {'type': 'string'},
    "data": {'type': 'dict'}
}

schema_radio24GEdit = {
    "status": {'type': 'int'},
    "message": {'type': 'string'},
    "requestId": {'type': 'string'},
    "data": {'type': 'dict'}
}

schema_radio5GEdit = {
    "status": {'type': 'int'},
    "message": {'type': 'string'},
    "requestId": {'type': 'string'},
    "data": {'type': 'dict'}
}

schema_ssidEdit = {
    "status": {'type': 'int'},
    "message": {'type': 'string'},
    "requestId": {'type': 'string'},
    "data": {'type': 'dict'}
}

schema_guest24GEdit = {
    "status": {'type': 'int'},
    "message": {'type': 'string'},
    "requestId": {'type': 'string'},
    "data": {'type': 'dict'}
}

schema_guest5GEdit = {
    "status": {'type': 'int'},
    "message": {'type': 'string'},
    "requestId": {'type': 'string'},
    "data": {'type': 'dict'}
}

schema_repeater24GEdit = {
    "status": {'type': 'int'},
    "message": {'type': 'string'},
    "requestId": {'type': 'string'},
    "data": {'type': 'dict'}
}

schema_repeater5GEdit = {
    "status": {'type': 'int'},
    "message": {'type': 'string'},
    "requestId": {'type': 'string'},
    "data": {'type': 'dict'}
}

schema_portforwardCreate = {
    "status": {'type': 'int'},
    "message": {'type': 'string'},
    "requestId": {'type': 'string'},
    "data": {'type': 'dict'}
}

schema_portforwardRemove = {
    "status": {'type': 'int'},
    "message": {'type': 'string'},
    "requestId": {'type': 'string'},
    "data": {'type': 'dict'}
}

schema_ddnsCreate = {
    "status": {'type': 'int'},
    "message": {'type': 'string'},
    "requestId": {'type': 'string'},
    "data": {'type': 'dict'}
}

schema_ddnsEdit = {
    "status": {'type': 'int'},
    "message": {'type': 'string'},
    "requestId": {'type': 'string'},
    "data": {'type': 'dict'}
}

schema_ddnsRemove = {
    "status": {'type': 'int'},
    "message": {'type': 'string'},
    "requestId": {'type': 'string'},
    "data": {'type': 'dict'}
}

schema_passwordEdit = {
    "status": {'type': 'int'},
    "message": {'type': 'string'},
    "requestId": {'type': 'string'},
    "data": {'type': 'dict'}
}