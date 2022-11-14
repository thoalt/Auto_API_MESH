import time

from base.WEBLib import Web_Lib

class MeshPage(Web_Lib):
    lnkMeshTab_xpath = "//a[@title='Mesh']"
    btnCreateMesh_xpath = "//input[@id='createmesh']"
    drpMeshMode_xpath = "//select[@id='Input_Enable_Bridge']"
    txtMeshSSID_xpath = "//input[@id='Input_SSID']"
    lbMeshSSID_xpath = "//td[@id='meshnetwork']"
    txtWPAPass_xpath = "//input[@id='Input_WPA_passphrase']"
    lbWPAPass_xpath = "//td[contains(text(),'WPA Passphrase')]"
    btnApply_xpath = "//input[@id='applynew']"

    btnJoinMesh_xpath = "//input[@onclick='JoinMesh()']"
    btnSearchMesh_xpath = "//input[@onclick='ScanNeighborSSID()']"
    btnJoinManual_xpath = "//input[@onclick='Manual()']"
    txtManuMeshSSID_xpath = "//input[@id='Input_SSID']"
    lbManuMeshSSID_xpath = "//td[@id='meshnetwork']"
    txtManuWPAPass_xpath = "//input[@id='Input_WPA_passphrase']"
    lbManuWPAPass_xpath = "//td[contains(text(),'WPA Passphrase')]"
    btnApplyJoinManu_xpath = "//input[@onclick='ApplyRepeater2G()']"

    lbScannedSSID_xpath = "//td[contains(text(),'Scanned SSID Table')]"
    btnJoinSSID_xpath = "//tbody/tr[3]/td[2]/input[1]"

    lbMeshName_xpath = "//label[@id='SSID']"
    btnDisableONTMesh_xpath = "//img[@id='disable_syncONT']"
    btnEnableONTMesh_xpath = "//img[@id='enable_syncONT']"

    # Init method
    def __init__(self, driver):
        super().__init__(driver)

    def click_mesh_tab(self):
        self.wait_and_click_element(self.lnkMeshTab_xpath)

    def click_create_mesh(self):
        self.wait_and_click_element(self.btnCreateMesh_xpath)

    def set_mesh_SSID(self, meshSSID):
        self.wait_and_set_text_element_with_delete(self.txtMeshSSID_xpath, meshSSID)

    def get_mesh_SSID(self):
        return self.wait_and_get_attribute_element(self.txtMeshSSID_xpath, 'value')

    def get_mesh_name(self):
        return self.wait_and_get_text_element(self.lbMeshName_xpath)

    def set_WPA_pass(self, wpaPass):
        self.wait_and_set_text_element_with_delete(self.txtWPAPass_xpath, wpaPass)

    def get_WPA_pass(self):
        return self.wait_and_get_attribute_element(self.txtWPAPass_xpath, 'value')

    def select_mesh_mode(self, meshMode):
        self.wait_and_select_item(self.drpMeshMode_xpath, meshMode)

    def click_apply(self):
        self.wait_and_click_element(self.btnApply_xpath)

    def click_join_mesh(self):
        self.wait_and_click_element(self.btnJoinMesh_xpath)

    def click_search_mesh(self):
        self.wait_and_click_element(self.btnSearchMesh_xpath)

    def click_join_SSID(self):
        self.wait_and_click_element(self.btnJoinSSID_xpath)

    def click_join_manual_mesh(self):
        self.wait_and_click_element(self.btnJoinManual_xpath)

    def set_manual_mesh_SSID(self, meshSSID):
        self.wait_and_set_text_element_with_delete(self.txtManuMeshSSID_xpath, meshSSID)

    def set_manual_WPA_Pass(self, wpaPass):
        self.wait_and_set_text_element_with_delete(self.txtManuWPAPass_xpath, wpaPass)

    def click_apply_join_manual(self):
        self.wait_and_click_element(self.btnApplyJoinManu_xpath)

    def click_enable_sync_ONT(self):
        self.wait_and_click_element(self.btnEnableONTMesh_xpath)

    def click_disable_sync_ONT(self):
        self.wait_and_click_element(self.btnDisableONTMesh_xpath)

    def get_enable_sync_ONT_status(self):
        status = False
        style = self.wait_and_get_attribute_element(self.btnEnableONTMesh_xpath, attribute_name='style')
        if style == "display: none;":
            status = False
        elif style == "display: block;":
            status = True
        return status

    def get_disable_sync_ONT_status(self):
        status = False
        style = self.wait_and_get_attribute_element(self.btnDisableONTMesh_xpath, attribute_name='style')
        if style == "display: none;":
            status = True
        elif style == "display: block;":
            status = False
        return status

    def navigate_to_mesh_tab(self):
        self.click_mesh_tab()
        time.sleep(1)

    def navigate_to_create_mesh_network(self):
        self.click_mesh_tab()
        time.sleep(1)
        self.click_create_mesh()
        time.sleep(2)

    def navigate_to_join_mesh_network(self):
        self.click_mesh_tab()
        time.sleep(1)
        self.click_join_mesh()
        time.sleep(1)
        self.click_join_manual_mesh()
        time.sleep(2)

    def set_create_mesh(self, stateSync=None, meshMode=None, SSID=None, password=None, clickAction=True):

        if meshMode is not None:
            self.select_mesh_mode(meshMode)

        if SSID is not None:
            self.set_mesh_SSID(SSID)

        if password is not None:
            self.set_WPA_pass(password)

        if clickAction:
            self.click_apply()
            time.sleep(0.5)
            self.accept_alert()

    def set_join_manual(self, SSID=None, password=None, clickAction=True):
        if SSID is not None:
            self.set_mesh_SSID(SSID)

        if password is not None:
            self.set_WPA_pass(password)

        if clickAction:
            self.click_apply_join_manual()

    def set_sync_ONT(self, stateSync=None):
        if stateSync == True:
            self.click_enable_sync_ONT()
            self.accept_alert()

        else:
            self.click_disable_sync_ONT()
            self.accept_alert()

    def get_alert_info(self):
        alert_text = self.get_alert_text()
        return (alert_text)