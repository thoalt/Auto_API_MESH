import time

import paramiko
from paramiko.client import SSHClient


class SSH_Lib:
    def __init__(self, SSHSession=None, SSHShell=None):
        if SSHSession is not None:
            self.SSHSession: SSHClient = SSHSession

        if SSHShell is not None:
            self.SSHShell = SSHShell

    def run_SSH_command(self, command, outputDict=None):
        if outputDict is not None:
            outputDict['stdout'] = ''

        session = self.SSHSession.get_transport().open_session()

        # Create channel for input, output and error
        stdin = session.makefile('wb', -1)
        stdout = session.makefile('rb', -1)
        stderr = session.makefile_stderr('rb', -1)

        # Run the command
        session.exec_command(command)
        time.sleep(2)
        output = stdout.read().decode('utf8')
        if outputDict != None:
            outputDict['stdout'] = output

    def get_exactly_value_from_uci_show(self, outputStr):
        strVal = ''
        if outputStr is not None:
            strList = outputStr.split("=")
            strValLst = ''
            if len(strList) > 2:
                for idx in range(1, len(strList)):
                    strValLst = strValLst + "=" + strList[idx]
            else:
                strValLst = strList[1]

            if '\'' in strValLst:
                strSplit = strValLst.split('\'')
                lenLst = len(strSplit)
                # For case nomarl, value is 'value'
                # For NTP server, value is 'value1' 'value2' 'value3'
                if lenLst == 3:
                    strVal = strSplit[1]
                else:
                    for idx, ele in enumerate(strSplit):
                        if idx not in [0, lenLst]:
                            strVal += ele
            else:
                strVal = strValLst
        return strVal

    def get_uci_value_SSH_command(self, command):
        # Dictionary for output
        outputDict = {}
        uciVal = ''
        # Start the command
        self.run_SSH_command(command, outputDict)

        # Get output
        outputStr = outputDict['stdout']
        if outputStr != '':
            uciVal = self.get_exactly_value_from_uci_show(outputStr)
        return uciVal

    def start_mobile_agent(self):
        self.SSHShell.execute_command('/etc/init.d/vnptt_mad stop')
        time.sleep(1)
        self.SSHShell.execute_command('/etc/init.d/vnptt_mad start')
        time.sleep(1)
        return self.SSHShell
