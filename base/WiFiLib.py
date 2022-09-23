import io
import os
import subprocess
import sys
import tempfile
from typing import List
from Utilities import global_dir

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

    def connect_wifi(self, ssid: str = '', auth: str = '', encrypt: str = '', passwd: str = '',
                     remember: bool = True, bssid: str = '', GUID=None):

        profile = self.gen_profile(ssid=ssid, auth=auth, encrypt=encrypt, passwd=passwd, remember=remember)
        self.add_profile(profile)

        self.connect(ssid=ssid, bssid=bssid, profileName=ssid, GUID=GUID)

    def check_ping(self, serverAddr, srcAddr=None, count=None) -> bool:
        if count is None:
            count = 10

        if srcAddr is not None:
            cmdPing = "ping {} -S {} -n {}".format(serverAddr, srcAddr, count)
        else:
            cmdPing = "ping {} -n {}".format(serverAddr, count)

        print(cmdPing)
        output: str = self.run_command(cmd=cmdPing, timeout=count+3).stdout
        print(output)
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




