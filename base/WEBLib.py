import os
import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webdriver import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from Config import config as cfg
from typing import List
from Utilities import global_dir

class Web_Lib:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.timeout = int(cfg.AVG_TIMEOUT)
        self.minTimeout = int(cfg.MIN_TIMEOUT)
        self.driver.implicitly_wait(self.timeout)
        self.driverWait: WebDriverWait = WebDriverWait(self.driver, self.timeout)

    ####### Selenium Webdriver ##############
    def open_url(self, url_value):
        """
        Description: Load a web page in the current browser
        :param url_value: url link
        :return:
        """
        self.driver.get(url_value)
        self.driver.maximize_window()

    def open_new_windown(self, url_value):
        """
        Description: Open new windown then switch to
        """
        self.driver.execute_script("window.open('');")
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.open_url(url_value)

    def get_page_title(self):
        """
        Description: Get title of page
        :return: title of page
        """
        return self.driver.title

    def get_page_source(self):
        """
        Description: Get page source
        :return:
        """
        return self.driver.page_source

    def get_current_url(self):
        """
        Description: Get current url
        :return: current url
        """
        return self.driver.current_url

    def back(self):
        """
        Description : Back to previous page
        :return:
        """
        self.driver.back()

    def refresh(self):
        """
        Description: Refresh page
        :return:
        """
        self.driver.refresh()

    def forward(self):
        """
        Description: Forward to next page
        :return:
        """
        self.driver.forward()

    def accept_alert(self):
        """
        Description: Accept Alert
        """
        try:
            WebDriverWait(self.driver, self.timeout).until(EC.alert_is_present())
            alert = self.driver.switch_to.alert
            alert.accept()
        except Exception as exc:
            raise Exception("Alert didn't appear!" + "\n" + str(exc))

    def cancel_alert(self):
        """
        Description: Cancel Alert
        :param time_out:
        :return:
        """
        try:
            WebDriverWait(self.driver, self.timeout).until(EC.alert_is_present())
            alert = self.driver.switch_to.alert
            alert.dismiss()
        except Exception as exc:
            raise Exception("Alert didn't appear!" + "\n" + str(exc))

    def get_alert_text(self):
        """
        Description: get alert text
        :param time_out:
        :return:
        """
        try:
            WebDriverWait(self.driver, self.minTimeout).until(EC.alert_is_present())
            alert = self.driver.switch_to.alert
            al_txt = alert.text
            time.sleep(1)
            alert.accept()
        except TimeoutException:
            al_txt = ''
        return al_txt

    def set_alert_text(self, value: str = ''):
        """
        Description: send key to alert
        :param value:
        :param time_out:
        :return:
        """
        try:
            WebDriverWait(self.driver, self.timeout).until(EC.alert_is_present())
            alert = self.driver.switch_to.alert
            alert.send_keys(value)
        except Exception as exc:
            raise Exception("Alert didn't appear!" + "\n" + str(exc))

    def get_current_window_ID(self):
        """
        Description: Get current window ID
        :return:
        """
        return self.driver.current_window_handle

    def switch_window_by_ID(self, window_id):
        """
        Description : Switch to window by windown ID
        :return:
        """
        all_windows_id = self.driver.window_handles

        for wdID in all_windows_id:
            if wdID == window_id:
                self.driver.switch_to.window(window_id)
                break

    def switch_window_by_title(self, title_window: str = ''):
        """
        Description : Switch to windown by title
        :param title:
        :return:
        """
        all_windows_id = self.driver.window_handles

        for wdID in all_windows_id:
            self.driver.switch_to.window(wdID)
            curTitle = self.driver.title
            if curTitle == title_window:
                break

    def close_all_window_without_parent(self, parent_id: str = ''):
        """
        Description: Close all window without parent window
        :param parent_id:
        :return:
        """
        all_windows_id = self.driver.window_handles

        for wdID in all_windows_id:
            if wdID != parent_id:
                self.driver.switch_to.window(wdID)
                self.driver.close()

        self.driver.switch_to.window(parent_id)

        if len(self.driver.window_handles) == 1:
            return True
        else:
            return False

    def quit(self):
        self.driver.quit()

    #### Selenium Web Element
    def wait_and_click_element(self, xpath: str):
        """
        Description: Wait until element can click able, then click element
        :param driver: Web Driver
        :param xpath: xpath for this element
        :param time_out: time for implicitly wait
        :return:
        """
        try:
            element: WebElement = WebDriverWait(self.driver, self.timeout). \
                until(EC.element_to_be_clickable((By.XPATH, xpath)))
            element.click()
        except Exception as exc:
            raise Exception("Element cannot clickable!" + "\n" + str(exc))

    def wait_and_set_text_with_clear(self, xpath: str, text_value: str):
        """
        Description: Wait element is visibility then send key
        :param xpath:
        :param text_value:
        :param time_out:
        :return:
        """
        try:
            element: WebElement = WebDriverWait(self.driver, self.timeout). \
                until(EC.visibility_of_element_located((By.XPATH, xpath)))
            element.clear()
            element.send_keys(text_value)
        except Exception as exc:
            raise Exception("Element cannot located!" + "\n" + str(exc))

    def set_text_element(self, xpath, textVal):
        ele = self.driver.find_element(By.XPATH, xpath)
        #ele.clear()
        ele.send_keys(textVal)

    def wait_and_set_text_element_with_delete(self, xpath: str, text_value: str):
        """
        Description: Wait element is visibility then send key
        :param xpath:
        :param text_value:
        :param time_out:
        :return:
        """
        try:
            element: WebElement = WebDriverWait(self.driver, self.timeout). \
                until(EC.visibility_of_element_located((By.XPATH, xpath)))
            element.send_keys(Keys.CONTROL + "a")
            element.send_keys(Keys.DELETE)
            element.send_keys(text_value)
            element.send_keys(Keys.ENTER)
        except Exception as exc:
            raise Exception("Element cannot located!" + "\n" + str(exc))

    def wait_and_set_text_element_without_enter(self, xpath: str, text_value: str):
        """
        Description: Wait element is visibility then send key
        :param xpath:
        :param text_value:
        :param time_out:
        :return:
        """
        try:
            element: WebElement = WebDriverWait(self.driver, self.timeout). \
                until(EC.visibility_of_element_located((By.XPATH, xpath)))
            element.send_keys(Keys.CONTROL + "a")
            element.send_keys(Keys.DELETE)
            element.send_keys(text_value)
        except Exception as exc:
            raise Exception("Element cannot located!" + "\n" + str(exc))

    def wait_and_get_text_element(self, xpath: str):
        """
        Description: Wait element util visibility then get text
        :param xpath:
        :param time_out:
        :return:
        """
        try:
            element: WebElement = WebDriverWait(self.driver, self.timeout). \
                until(EC.presence_of_element_located((By.XPATH, xpath)))
            # print ("Element Text: \'%s\'" %element.text )
            return element.text
        except Exception as exc:
            raise Exception("Element cannot located!" + "\n" + str(exc))

    def wait_and_get_attribute_element(self, xpath: str, attribute_name: str):
        """
        Description: Wait element util visibility then get text
        :param attribute_name:
        :param xpath:
        :param time_out:
        :return:
        """
        try:
            element: WebElement = WebDriverWait(self.driver, self.timeout). \
                until(EC.visibility_of_element_located((By.XPATH, xpath)))
            return element.get_attribute(attribute_name)

        except Exception as exc:
            raise Exception("Element cannot located!" + "\n" + str(exc))

    def wait_and_get_selected_text(self, xpath: str):
        """
        Description: Wait dropdown element element until it is presence in DOM

        """
        try:
            element: WebElement = WebDriverWait(self.driver, self.timeout) \
                .until(EC.presence_of_element_located((By.XPATH, xpath)))
            drp: Select = Select(element)
            cntSelected = 0

            for opt in drp.options:
                if opt.is_selected():
                    cntSelected += 1

            if cntSelected == 0:
                textVal = None
            else:
                selectedOp = drp.first_selected_option
                textVal = selectedOp.text

            return textVal
        except Exception as exc:
            raise Exception("Element cannot select!" + "\n" + str(exc))

    def wait_and_select_item(self, xpath: str, text_item: str):
        """
        Description: Wait dropdown element element until it is visibility then select one by text item
        :param xpath:
        :param text_item:
        :param time_out:
        :return:
        """
        try:
            element: WebElement = WebDriverWait(self.driver, self.timeout) \
                .until(EC.visibility_of_element_located((By.XPATH, xpath)))
            drp: Select = Select(element)
            drp.select_by_visible_text(text_item)
        except Exception as exc:
            raise Exception("Element cannot select!" + "\n" + str(exc))

    def wait_and_select_item_by_value(self, xpath: str, value: str):
        """
        Description: Wait dropdown element element until it is visibility then select one by text item
        :param xpath:
        :param text_item:
        :param time_out:
        :return:
        """
        try:
            element: WebElement = WebDriverWait(self.driver, self.timeout) \
                .until(EC.visibility_of_element_located((By.XPATH, xpath)))
            drp: Select = Select(element)
            drp.select_by_value(value)
        except Exception as exc:
            raise Exception("Element cannot select!" + "\n" + str(exc))

    def wait_and_select_multi_item(self, xpath: str, list_text_item: list):
        """
        Description: Wait dropdown element until it is visibility then select multi item by text
        :param xpath:
        :param list_text_item:
        :param time_out:
        :return:
        """
        try:
            element: WebElement = WebDriverWait(self.driver, self.timeout) \
                .until(EC.visibility_of_element_located((By.XPATH, xpath)))
            drp: Select = Select(element)
            if drp.is_multiple:
                for item in list_text_item:
                    drp.select_by_visible_text(item)
            else:
                raise Exception("Element doesn't support multi selected!")
        except Exception as exc:
            raise Exception("Element cannot select!" + "\n" + str(exc))

    def wait_and_get_selected_item(self, xpath: str):
        """
        Description: Wait dropdown element until it is visibility then get selected item
        :param xpath:
        :param time_out:
        :return:
        """
        try:
            element: WebElement = WebDriverWait(self.driver, self.timeout) \
                .until(EC.visibility_of_element_located((By.XPATH, xpath)))
            drp: Select = Select(element)
            return drp.first_selected_option
        except Exception as exc:
            raise Exception("Element cannot located!" + "\n" + str(exc))

    def wait_and_get_multi_selected_item(self, xpath: str) -> List[str]:
        """
        Description: Wait dropdown element until it is visibility then get multi selected item
        :param xpath:
        :param time_out:
        :return:
        """
        items_text: List[str] = []
        try:
            element: WebElement = WebDriverWait(self.driver, self.timeout) \
                .until(EC.visibility_of_element_located((By.XPATH, xpath)))
            drp: Select = Select(element)
            for item in drp.all_selected_options:
                items_text.append(item.text)
        except Exception as exc:
            raise Exception("Element cannot located!" + "\n" + str(exc))

    def wait_and_get_checkbox_selected(self, xpath: str):
        """
        Description: Wait checkbox element until it visible, then get status
        :param xpath:
        :param time_out:
        :return:
        """
        try:
            element: WebElement = WebDriverWait(self.driver, self.timeout) \
                .until(EC.element_to_be_clickable((By.XPATH, xpath)))
            if element.is_selected():
                return True
            else:
                return False
        except Exception as exc:
            raise Exception("Element cannot located!" + "\n" + str(exc))

    def wait_and_check_checkbox(self, xpath: str):
        """
        Description: Wait checkbox element until it visible, then check the checkbox
        :param xpath:
        :param time_out:
        :return:
        """
        try:
            element: WebElement = WebDriverWait(self.driver, self.timeout) \
                .until(EC.element_to_be_clickable((By.XPATH, xpath)))
            if not element.is_selected():
                element.click()
        except Exception as exc:
            raise Exception("Element cannot check!" + "\n" + str(exc))

    def wait_and_uncheck_checkbox(self, xpath: str):
        """
        Description: Wait checkbox element until it visible, then uncheck the checkbox
        :param xpath:
        :param time_out:
        :return:
        """
        try:
            element: WebElement = WebDriverWait(self.driver, self.timeout) \
                .until(EC.element_to_be_clickable((By.XPATH, xpath)))
            if element.is_selected():
                element.click()

        except Exception as exc:
            raise Exception("Element cannot check!" + "\n" + str(exc))

    def wait_and_count_element_number(self, xpath: str) -> int:
        """
        Description:
        :param xpath:
        :param time_out:
        :return:
        """
        try:
            elements: List = WebDriverWait(self.driver, self.timeout) \
                .until(EC.visibility_of_element_located((By.XPATH, xpath)))
            return len(elements)
        except Exception as exc:
            raise Exception("Cannot find element!")

    def is_element_displayed(self, xpath: str) -> bool:
        """
        Description: get status of element is display or not
        """
        return self.driver.find_element(By.XPATH, xpath).is_displayed()

    def is_element_selected(self, xpath: str) -> bool:
        """
        Description: get status of element is selected or not
        """
        return self.driver.find_element(By.XPATH, xpath).is_selected()

    def is_element_enabled(self, xpath: str) -> bool:
        """
        Description: get status of element is enabled or not
        """
        return self.driver.find_element(By.XPATH, xpath).is_enabled()

    def wait_and_switch_to_frame_or_iframe(self, frameID):
        """
        Description: wait until frame element is appeared then switch to frame by ID
        """
        try:
            element: WebElement = WebDriverWait(self.driver, self.timeout) \
                .until(EC.frame_to_be_available_and_switch_to_it(frameID))
            #self.driver.switch_to.frame(element)

        except Exception as exc:
            raise Exception("Element cannot check!" + "\n" + str(exc))

    def switch_to_frame_by_ID(self, frameID):
        self.driver.switch_to.frame(frameID)

    def switch_to_default_content(self):
        """
        Description: Switch from frame/iframe to default content frame
        """
        self.driver.switch_to.default_content()

    def wait_and_hover_mouse_to_element(self, xpath: str):
        """
        Description: hover mouse to element
        """
        try:
            element: WebElement = WebDriverWait(self.driver, self.timeout) \
                .until(EC.visibility_of_element_located((By.XPATH, xpath)))
            ActionChains(self.driver).move_to_element(element).perform()
        except Exception as exc:
            raise Exception("Element cannot find!" + "\n" + str(exc))

    def wait_and_double_click(self, xpath: str):
        """
        Description: double click
        """
        try:
            element: WebElement = WebDriverWait(self.driver, self.timeout) \
                .until(EC.element_to_be_clickable((By.XPATH, xpath)))
            ActionChains(self.driver).double_click(element).perform()
        except Exception as exc:
            raise Exception("Element cannot find!" + "\n" + str(exc))

    def wait_and_right_click(self, xpath: str):
        """
        Description: double click
        """
        try:
            element: WebElement = WebDriverWait(self.driver, self.timeout) \
                .until(EC.element_to_be_clickable((By.XPATH, xpath)))
            ActionChains(self.driver).context_click(element).perform()
        except Exception as exc:
            raise Exception("Element cannot find!" + "\n" + str(exc))

    def wait_and_drag_drop(self, xpathSrc: str, xpathDst: str):
        """
         Description: drag then drop element in HTML4
        """
        try:
            element_src: WebElement = WebDriverWait(self.driver, self.timeout) \
                .until(EC.visibility_of_element_located((By.XPATH, xpathSrc)))
            element_dst: WebElement = WebDriverWait(self.driver, self.timeout) \
                .until(EC.visibility_of_element_located((By.XPATH, xpathDst)))

            ActionChains(self.driver).drag_and_drop(element_src, element_dst).perform()

        except Exception as exc:
            raise Exception("Element cannot find!" + "\n" + str(exc))

    def execute_for_browser(self, javascript):
        """
        Description: execute java script for browser
        """
        return self.driver.execute_script(javascript)

    def scroll_to_bottom_page(self):
        """
        Description: Scroll to the bottom of page
        """
        self.driver.execute_script("window.scrollBy(0, document.body.scrollHeight)")

    def scroll_to_element(self, xpath: str):
        """
        Description: Scroll to the element
        """
        element: WebElement = self.driver.find_element(By.XPATH, xpath)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    def is_image_loaded(self, xpath: str):
        """
        Description: check image loaded successfully
        """
        element: WebElement = self.driver.find_element(By.XPATH, xpath)
        jsscript = "return arguments[0].complete && typeof arguments[0].naturalWith != 'undefined'" \
                   " && arguments[0].naturalWith > 0"
        status = self.driver.execute_script(jsscript, element)

        if status:
            return True
        else:
            return False


    def take_screenshot(self, file_name):
        """
        Description: Capture Screenshot then save to folder "Report/Screenshots"
        """
        dirFile = os.path.join(global_dir.SCREENSHOT_FILES_PATH, file_name)
        self.driver.save_screenshot(dirFile)