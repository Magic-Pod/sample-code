import os
import sys
import unittest

from time import sleep
from appium import webdriver

# get userName, password from Environment variable
RTK_USERNAME = os.environ.get('RTK_USERNAME')
RTK_PASSWORD = os.environ.get('RTK_PASSWORD')
if not RTK_USERNAME or not RTK_PASSWORD:
    print("Environment variable error")
    sys.exit()


class FindWebContextTest(unittest.TestCase):
    def setUp(self):
        caps = {
            'userName': RTK_USERNAME,
            'password': RTK_PASSWORD,
            'logLevel': 'info',
            'platformName': 'iOS',
            'deviceName': 'iPad Pro 11',
            'platformVersion': '13.1',
            'app': 'https://github.com/Magic-Pod/AppiumRegressionCheck/blob/master/test_app/iOSWebView.ipa?raw=true',
            'bundleId': 'com.trident-qa.iOSWebView'
        }
        self.driver = webdriver.Remote('https://gwjp.appkitbox.com/wd/hub', caps)

    def tearDown(self):
        self.driver.quit()

    def test_find_web_context(self):
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
