import subprocess
import time
import paramiko
import pytest
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import IEDriverManager, EdgeChromiumDriverManager

from APIObject.login import LoginClient
from APIObject.openssesion import openssesionClient
from Config import config as cfg
from sshaolin.client import SSHClient, SSHShell
from base.SSHLib import SSH_Lib
from pages.LoginPage import LoginPage


@pytest.fixture(autouse=False, scope="class")
def create_ssh_session(request):
    MAX_RETRY_CONNECT = 3
    SSH_CONNECTION_TIMEOUT = 240
    SSHSession = paramiko.SSHClient()
    SSHSession.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    for i in range(MAX_RETRY_CONNECT):
        try:
            SSHSession.connect(hostname=cfg.IP_ADDR_CAP, username=cfg.USER_SSH, password=cfg.PASS_SSH, port=cfg.PORT_NUM,
                               timeout=SSH_CONNECTION_TIMEOUT)
            request.cls.SSHSession = SSHSession
            break
        except:
            pass
        time.sleep(5)
    else:
        SSHSession.close()
        raise Exception("Exception during connecting to " + cfg.IP_ADDR_CAP + "!\n")

    yield
    SSHSession.close()


@pytest.fixture(autouse=False, scope="class")
def create_shell(request):
    try:
        client = SSHClient(hostname=cfg.IP_ADDR_CAP, username=cfg.USER_SSH, password=cfg.PASS_SSH)
        SSHShell = client.create_shell()
        request.cls.SSHShell = SSHShell
    except:
        raise Exception("Exception during connecting to " + cfg.IP_ADDR_CAP + "!\n")

    yield
    SSHShell.close()

@pytest.fixture(autouse=False, scope="class")
def start_agent():
    try:
        client = SSHClient(hostname=cfg.IP_ADDR_CAP, username=cfg.USER_SSH, password=cfg.PASS_SSH)
        SSHShell = client.create_shell()
        SSHSes = SSH_Lib(SSHShell=SSHShell)
        SSHSes.start_mobile_agent()
    except:
        raise Exception("Exception during connecting to " + cfg.IP_ADDR_CAP + "!\n")

@pytest.fixture(autouse=False, scope="class")
@pytest.mark.usefixtures("start_agent")
def login(request):
    ClientSes = openssesionClient()
    cookie = ClientSes.Open_Sesion_And_Get_Cookie()

    LoginClt = LoginClient()
    LoginClt.login(cookie)
    request.cls.cookie = cookie


@pytest.fixture(autouse=False, scope="class")
def driver_setup(browser):
    try:
        # Kill all process of chromedriver before create new
        subprocess.call("TASKKILL /f  /IM  CHROMEDRIVER.EXE")
    except:
        pass

    if browser == "Chrome":
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    elif browser == "Firefox":
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    elif browser == "IE":
        driver = webdriver.Ie(executable_path=IEDriverManager().install())
    elif browser == "Edge":
        driver = webdriver.Edge(executable_path=EdgeChromiumDriverManager().install())
    else:
        #driver = webdriver.Chrome(executable_path="E:\Auto_WorkingTesting\Auto_Project_WF6\Drivers\chromedriver.exe")
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    driver.implicitly_wait(10)
    return driver

@pytest.fixture(autouse=False, scope="class")
def login_CAP_GUI(request, driver_setup):
    base_url = cfg.CAP_URL
    username = cfg.USER_GUI
    password = cfg.PASS_GUI
    driver: WebDriver = driver_setup
    try:
        lp = LoginPage(driver)
        lp.open_url(base_url)
        lp.log_in_to_webgui(username, password)
        request.cls.driver = lp.driver
        yield
        driver.close()
    except Exception as exc:
        driver.quit()
        raise Exception("Login WebGui CAP Fail !!!! \n" + str(exc))


def get_report_name(request):
    """
    This function return the report name
    """
    return request.config.getoption("--html-report")

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture(scope="class", autouse=False)
def browser(request):
    """
    This function return the Browser value to setup method
    """
    return request.config.getoption("--browser")