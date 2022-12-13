from dataclasses import dataclass
import io
import os
import subprocess
import sys
import tempfile
import time
from typing import List
from Utilities import global_dir
from Config import config as cfg

@dataclass
class WifiInfo:
    SSID : str
    BSSID: str
    standard: str
    channel: str
    receiveRate: str
    transmissRate: str

class Wifi_lib:
    def get_profile_template(self):
        """
        Description: Get Profile Wifi Template which save in folder Roodt_dir_project/config/Profile_Wifi_Template.xml
        Output: string profile
        """
        with open(global_dir.PROFILE_TEMPLATE_PATH, 'r') as file:
            profile_tmp = file.read()
        return profile_tmp

    def netsh(self, args: List[str], timeout: int = 3, check: bool = True) -> subprocess.CompletedProcess:
        """
        Description: Run command 'netsh ...' in window using subprocess module
        :param args: List string follow command netsh
        :param timeout: Timeout to run command
        :param check:
        """
        return subprocess.run(['netsh'] + args, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                              timeout=timeout, check=check, encoding=sys.stdout.encoding)

    def run_command(self, cmd: str, timeout: int = 3, check: bool = True) -> subprocess.CompletedProcess:
        """
        Description: Run window command using subprocess module
        :param cmd: Command
        :param timeout: Timeout to run command
        :param check:
        """
        return subprocess.run(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                              timeout=timeout, check=check,  shell=True, encoding=sys.stdout.encoding)

    def gen_profile(self, ssid: str = '', auth: str = '', encrypt: str = '', passwd: str = '',
                    remember: bool = True) -> str:
        """
        Description:
        :param ssid:
        :param auth:
        :param encrypt:
        :param passwd:
        :param remember:
        """
        profile = self.get_profile_template()

        profile = profile.replace('{SSID}', ssid)
        profile = profile.replace('{connmode}', 'auto' if remember else 'manual')
        if not passwd:
            profile = profile[:profile.index('<sharedKey>')] + \
                      profile[profile.index('</sharedKey>') + len('</sharedKey>'):]
            profile = profile.replace('{auth}', 'open')
            profile = profile.replace('{encrypt}', 'none')
        else:
            profile = profile.replace('{auth}', auth)
            profile = profile.replace('{encrypt}', encrypt)
            profile = profile.replace('{passwd}', passwd)
        return profile

    def add_profile(self, profile: str):
        fd: io.RawIOBase
        path: str
        fd, path = tempfile.mkstemp()
        os.write(fd, profile.encode())
        self.netsh(['wlan', 'add', 'profile', 'filename="{}"'.format(path)])

        os.close(fd)
        os.remove(path)

    def connect(self, ssid: str = '', bssid: str = '', profileName: str = '', GUID=None):
        if not bssid:
            cmdConnect = 'cd {} && WifiInfoView.exe /ConnectAP "{}"'.format(global_dir.DRIVER_FOLDER, ssid)
        else:
            if GUID is not None:
                cmdConnect = 'cd {} && WifiInfoView.exe /ConnectAP "{}" "{}" {}  {}'.format(global_dir.DRIVER_FOLDER, ssid, bssid, profileName, GUID)
            else:
                cmdConnect = 'cd {} && WifiInfoView.exe /ConnectAP "{}" "{}" {}'.format(global_dir.DRIVER_FOLDER, ssid, bssid, profileName)
        print(cmdConnect)
        self.run_command(cmdConnect)

    def forget_wifi(self, ssid: str = '', interface: str = ''):
        if not ssid:
            #self.netsh(['wlan', 'delete', 'profile', 'name=*', 'interface="{}"'.format(interface)])
            self.netsh(['wlan', 'delete', 'profile', 'name=*'])
        else:
            #self.netsh(['wlan', 'delete', 'profile', 'name="{}"'.format(ssid), 'interface="{}"'.format(interface)])
            self.netsh(['wlan', 'delete', 'profile', 'name="{}"'.format(ssid)])

    def disconnect(self):
        self.netsh(['wlan', 'disconnect'])

    def connect_wifi(self, ssid: str = None, auth: str = None, encrypt: str = None, passwd: str = None,
                     remember: bool = True, bssid: str = '', GUID=None, wifiName=None):

        if ssid is None:
            ssid = cfg.SSID

        if auth is None:
            auth = cfg.auth

        if encrypt is None:
            encrypt = cfg.encrypt

        if passwd is None:
            passwd = cfg.PASSWORD

        if GUID is None:
            GUID = cfg.GUID

        if wifiName is None:
            wifiName = cfg.CARD_WIFI_NAME

        try:
            profile = self.gen_profile(ssid=ssid, auth=auth, encrypt=encrypt, passwd=passwd, remember=remember)
            self.add_profile(profile)

            for i in range(0, 5):
                self.connect(ssid=ssid, bssid=bssid, profileName=ssid, GUID=GUID)
                time.sleep(5)
                if not self.check_connect_success(wifiName=wifiName):
                    time.sleep(10)
                else:
                    break
            else:
                raise Exception(f"Cannot connect {ssid} via {bssid}")
        except:
            raise Exception(f"Cannot connect {ssid} via {bssid}")

    def check_connect_success(self, wifiName):
        status = False
        state = ''
        preStr = "Name                   : " + wifiName
        output: str = self.netsh(['wlan', 'show', 'interface']).stdout
        lines = output.split('\n')

        for idx, line in enumerate(lines):
            if preStr in line:
                stateLine = lines[idx + 4]
                state = stateLine.split(":")[1].replace(' ', '')
                break
        if state == "connected":
            status = True
        else:
            status = False
        return status

    def Get_Wifi_Info_Show_Interface(self, wifiName):
        ssid, bssid, standard, channel, recRate, transRate = '', '', '', '', '', ''
        preStr = "Name                   : " + wifiName
        output: str = self.netsh(['wlan', 'show', 'interface']).stdout
        lines = output.split('\n')

        for idx, line in enumerate(lines):
            if preStr in line:
                ssid = lines[idx + 5].split(" : ")[1].upper()
                bssid = lines[idx + 6].split(" : ")[1].upper()
                standard = lines[idx + 8].split(" : ")[1]
                channel = lines[idx + 12].split(" : ")[1]
                recRate = lines[idx + 13].split(" : ")[1]
                transRate = lines[idx + 14].split(" : ")[1]

        return WifiInfo(ssid, bssid, standard, channel, recRate, transRate)

    def get_BSSID_connected(self, wifiName):
        status = False
        bssid = ''
        preStr = "Name                   : " + wifiName
        output: str = self.netsh(['wlan', 'show', 'interface']).stdout
        lines = output.split('\n')

        for idx, line in enumerate(lines):
            if preStr in line:
                bssidLine = lines[idx + 6]
                bssid = bssidLine.split(" : ")[1].replace(' ', '')
                break
        return bssid.upper()

    def Convert_Bitrate_To_Bandwith(self, standard, bitrate):
        bandW = ''
        if standard == "11g" and bitrate == "54":
            bandW = 0 #"20MHz"

        elif standard == "11ng" and bitrate == "144":
            bandW = 0 #"20MHz"

        elif standard == "11ng" and bitrate == "300":
            bandW = 2 #"20/40MHz"

        elif standard == "11a" and bitrate == "54":
            bandW = 0 #"20MHz"

        elif standard == "11na" and bitrate == "144":
            bandW = 0 #"20MHz"

        elif standard == "11na" and bitrate == "300":
            bandW = 1 #"40MHz"

        elif standard == "11ac" and bitrate == "360":
            bandW = 0 #"20MHz"

        elif standard == "11ac" and bitrate == "400":
            bandW = 1 #"40MHz"

        elif standard == "11ac" and bitrate == "867":
            bandW = 3 #"80MHz"

        elif standard == "11ac" and bitrate == "1730":
            bandW = 4 #"160MHz"

        print("***********BIT RATE **********")
        print(bitrate)

        print("****************** BAND WIDTH ***********")
        print(bandW)

        return bandW

    def Convert_BandW_To_Bitrate(self, standard, bandW):
        bitRate = ''
        if standard == "11g" and bandW == "20MHz":
            bitRate = "54"

        elif standard == "11ng" and bandW == "20MHz":
            bitRate = "144"

        elif standard == "11ng" and bandW == "40MHz":
            bitRate = "300"

        elif standard == "11a" and bandW == "20MHz":
            bitRate = "54"

        elif standard == "11na" and bandW == "20MHz":
            bitRate = "144"

        elif standard == "11na" and bandW == "40MHz":
            bitRate = "300"

        elif standard == "11ac" and bandW == "20MHz":
            bitRate = "360"

        elif standard == "11ac" and bandW == "40MHz":
            bitRate = "400"

        elif standard == "11ac" and bandW == "80MHz":
            bitRate = "867"

        elif standard == "11ac" and bandW == "160MHz":
            bitRate = "1730"

        return bitRate

    # def get_Radio_Type(self, wifiName):
    #     standard = ''
    #     preStr = "Name                   : " + wifiName
    #     output: str = self.netsh(['wlan', 'show', 'interface']).stdout
    #     lines = output.split('\n')
    #
    #     for idx, line in enumerate(lines):
    #         if preStr in line:
    #             standard = lines[idx + 8].split(" : ")[1].replace(' ', '')
    #             break
    #     return standard
    #
    # def get_Channel(self, wifiName):
    #     channel = ''
    #     preStr = "Name                   : " + wifiName
    #     output: str = self.netsh(['wlan', 'show', 'interface']).stdout
    #     lines = output.split('\n')
    #
    #     for idx, line in enumerate(lines):
    #         if preStr in line:
    #             channel = lines[idx + 12].split(" : ")[1].replace(' ', '')
    #             break
    #     return channel
    #
    # def get_Receive_Rate(self, wifiName):
    #     channel = ''
    #     preStr = "Name                   : " + wifiName
    #     output: str = self.netsh(['wlan', 'show', 'interface']).stdout
    #     lines = output.split('\n')
    #
    #     for idx, line in enumerate(lines):
    #         if preStr in line:
    #             channel = lines[idx + 12].split(" : ")[1].replace(' ', '')
    #             break
    #     return channel

    def check_ping(self, serverAddr, srcAddr=None, count=None) -> bool:
        if count is None:
            count = 10

        if srcAddr is not None:
            cmdPing = "ping {} -S {} -n {}".format(serverAddr, srcAddr, count)
        else:
            cmdPing = "ping {} -n {}".format(serverAddr, count)

        print(cmdPing)
        output: str = self.run_command(cmd=cmdPing, timeout=count+3).stdout
        # print(output)
        lines = output.split("\n")

        totalSent = lines[-4].split(',')[0].split('=')[1]
        recevied = lines[-4].split(',')[1].split('=')[1]
        lost = lines[-4].split(',')[2].split('=')[1]

        # If Recevied is more than 50%, ping done
        perRecevied = int(recevied)/int(totalSent) *100
        if perRecevied > 50:
            return True
        else:
            return False




