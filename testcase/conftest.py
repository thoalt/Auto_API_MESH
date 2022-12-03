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
from APIObject.meshAPI import meshCreateClient
from APIObject.openssesion import openssesionClient
from Config import config as cfg
from sshaolin.client import SSHClient, SSHShell
from base.SSHLib import SSH_Lib
from pages.LoginPage import LoginPage
from pages.MeshPage import MeshPage
from base.SerialLib import Serial_Lib
from Utilities import Utility as utl
import Utilities.global_dir as gld

@pytest.fixture(autouse=False, scope="class")
def create_ssh_session(request):
    MAX_RETRY_CONNECT = 3
    SSH_CONNECTION_TIMEOUT = 240
    SSHSession = paramiko.SSHClient()
    SSHSession.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    for i in range(MAX_RETRY_CONNECT):
        try:
            SSHSession.connect(hostname=cfg.IP_ADDR_CAP, username=cfg.USER_SSH, password=cfg.PASS_SSH,
                               port=cfg.PORT_NUM,
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
        client = SSHClient(hostname=cfg.IP_ADDR_CAP, username=cfg.USER_SSH, password=cfg.PASS_SSH, timeout=300)
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
    except Exception as exc:
        raise Exception("Exception during connecting to " + cfg.IP_ADDR_CAP + "!\n" + str(exc))


@pytest.fixture(autouse=False, scope="class")
def login(request):
    """
    Description: Login to MESH AP via API
    - If mode Mesh is FACTORY --> Login and Create New Mesh Default --> Return Cookie
    - If Mode Mesh is CAP, and SSIDName is not Default SSID --> First Reset Factory, Then Login and Create new mesh default --> return Cookie
    - If Mode Mesh is CAP, and SSIDName is Default SSID --> Only Login  --> Return Cookie
    """
    # ClientSes = openssesionClient()
    # cookie = ClientSes.Open_Sesion_And_Get_Cookie()
    #
    # LoginClt = LoginClient()
    # LoginClt.login(cookie)
    #
    # request.cls.cookie = cookie

    # print("START LOGIN")
    serialClt = Serial_Lib()
    meshCreateClt = meshCreateClient()
    ClientSes = openssesionClient()
    LoginClt = LoginClient()
    cookie = ""

    passGuiDefault = utl.md5_encrypt(cfg.STR_ENCRYPT, cfg.SALT_DEFAULT)
    modeMesh = serialClt.Get_Mode_Mesh()
    print("************** MODE MESSH *************")
    print(modeMesh)
    SSIDName = serialClt.Get_SSID_Name(cfg.WIFI_INT_5G)
    print("************** SSID Name *************")
    print(SSIDName)
    passGUI = serialClt.Get_Pass_GUI()
    ipAddr = serialClt.Get_IP_Address()
    print("************** IP ADDRESS *************")
    print(ipAddr)

    if modeMesh == "FACTORY":
        cookie = ClientSes.Open_Sesion_And_Get_Cookie()
        LoginClt.login(cookie)
        meshCreateClt.Create_Mesh_Network_Default(cookie)

    # elif (modeMesh != "FACTORY") \
    #         and ((SSIDName == cfg.SSID) and (passGUI == passGuiDefault) and (ipAddr == cfg.IP_ADDR_CAP)):
    elif (modeMesh != "FACTORY") \
         and ((SSIDName == cfg.SSID) and (ipAddr == cfg.IP_ADDR_CAP)):
        cookie = ClientSes.Open_Sesion_And_Get_Cookie()
        LoginClt.login(cookie)

    else:
        serialClt.Reset_Factory()
        cookie = ClientSes.Open_Sesion_And_Get_Cookie()
        LoginClt.login(cookie)
        meshCreateClt.Create_Mesh_Network_Default(cookie)
    serialClt.Close_Serial_Connect()
    del serialClt
    request.cls.cookie = cookie


@pytest.fixture(autouse=False, scope="class")
def login_without_create_mesh(request):
    serialClt = Serial_Lib()
    modeMesh = serialClt.Get_Mode_Mesh()
    if modeMesh != "FACTORY":
        serialClt.Reset_Factory()
    serialClt.Close_Serial_Connect()
    del serialClt

    ClientSes = openssesionClient()
    cookie = ClientSes.Open_Sesion_And_Get_Cookie()

    LoginClt = LoginClient()
    LoginClt.login(cookie)

    request.cls.cookie = cookie


# def login(request, start_agent):
#     ClientSes = openssesionClient()
#     cookie = ClientSes.Open_Sesion_And_Get_Cookie()
#
#     LoginClt = LoginClient()
#     LoginClt.login(cookie)
#     request.cls.cookie = cookie


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
        # driver = webdriver.Chrome(executable_path="E:\Auto_WorkingTesting\Auto_Project_WF6\Drivers\chromedriver.exe")
        driver = webdriver.Chrome(executable_path=gld.DRIVER_FOLDER + "chromedriver.exe")
        # driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
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

@pytest.fixture(autouse=False, scope="class")
def login_CAP_GUI_with_reset_factory(request, driver_setup):
    # print("START LOGIN")
    serialClt = Serial_Lib()
    meshCreateClt = meshCreateClient()
    ClientSes = openssesionClient()
    LoginClt = LoginClient()
    cookie = ""

    passGuiDefault = utl.md5_encrypt(cfg.STR_ENCRYPT, "00000006")
    # print(" modeMesh START LOGIN")
    modeMesh = serialClt.Get_Mode_Mesh()
    # print("SSIDName START LOGIN")
    SSIDName = serialClt.Get_SSID_Name(cfg.WIFI_INT_5G)
    # print("passGUI START LOGIN")
    passGUI = serialClt.Get_Pass_GUI()

    base_url = cfg.CAP_URL
    username = cfg.USER_GUI
    password = cfg.PASS_GUI
    driver: WebDriver = driver_setup
    try:
        if modeMesh == "FACTORY":
            # print("LOGIN1")
            lp = LoginPage(driver)
            lp.open_url(base_url)
            lp.log_in_to_webgui(username, password)

            mp = MeshPage(driver)
            mp.navigate_to_create_mesh_network()
            mp.set_create_mesh(SSID=cfg.SSID, password=cfg.PASSWORD, clickAction=True)
            time.sleep(30)

            request.cls.driver = mp.driver
            yield
            driver.close()

        elif (modeMesh != "FACTORY") and ((SSIDName == cfg.SSID) and (passGUI == passGuiDefault)):
            # print("LOGIN2")
            lp = LoginPage(driver)
            lp.open_url(base_url)
            lp.log_in_to_webgui(username, password)

            request.cls.driver = lp.driver
            yield
            driver.close()

        else:
            # print("LOGIN3")
            serialClt.Reset_Factory()

            lp = LoginPage(driver)
            lp.open_url(base_url)
            lp.log_in_to_webgui(username, password)

            mp = MeshPage(driver)
            mp.navigate_to_create_mesh_network()
            mp.set_create_mesh(SSID=cfg.SSID, password=cfg.PASSWORD, clickAction=True)
            time.sleep(30)
            request.cls.driver = mp.driver
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
