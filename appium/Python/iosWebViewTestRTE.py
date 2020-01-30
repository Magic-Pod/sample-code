import os
import sys
import unittest

from time import sleep
from appium import webdriver

# get userName, password from Environment variable
RTE_USERNAME = os.environ.get('RTE_USERNAME')
RTE_PASSWORD = os.environ.get('RTE_PASSWORD')
RTE_URL = os.environ.get('RTE_URL')
if not RTE_USERNAME or not RTE_PASSWORD:
    print("Environment variable error")
    sys.exit()


class FindWebContextTest(unittest.TestCase):
    def setUp(self):
        caps = {
            'userName': RTE_USERNAME,
            'password': RTE_PASSWORD,
            'logLevel': 'info',
            'platformName': 'iOS',
            'deviceName': 'iPhone',
            'platformVersion': '12',
            'app': 'https://github.com/Magic-Pod/AppiumRegressionCheck/blob/master/test_app/iOSWebView.ipa?raw=true',
            'bundleId': 'com.trident-qa.iOSWebView',
        }
        self.driver = webdriver.Remote(RTE_URL, caps)

    def tearDown(self):
        self.driver.quit()

    def test_find_web_context(self):
        print(self.driver.capabilities['snapshotUrl'])
        driver = self.driver
        single_webview = driver.find_element_by_xpath("//XCUIElementTypeStaticText[@name='SingleWebView']")
        single_webview.click()

        sleep(3)
        # Needs to get contest twice https://github.com/appium/appium/issues/13770
        print(f'available contexts: {driver.contexts}')

        sleep(3)
        print(f'available contexts: {driver.contexts}')
        driver.switch_to.context(driver.contexts[1])

        tag = driver.find_element_by_xpath("//a[text()='Tags']")
        print(f'tag.text: {tag.text}')


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(FindWebContextTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
