import os
import sys
import unittest

from time import sleep
from appium import webdriver

# get xcodeOrgId from Environment variable
XCODE_ORG_ID = os.environ.get('XCODE_ORG_ID')
if not XCODE_ORG_ID:
    print("Environment variable error")
    sys.exit()


class FindWebContextTest(unittest.TestCase):
    def setUp(self):
        caps = {
            'automationName': 'XCUITest',
            'logLevel': 'info',
            'platformName': 'iOS',
            'deviceName': 'iPad Pro 11',
            'platformVersion': '13.1',
            'app': '<path/to/iOSWebView.ipa>',  # TODO: update this
            'xcodeOrgId': XCODE_ORG_ID,
            'xcodeSigningId': 'iPhone Developer',
            'udid': 'auto',
            'newCommandTimeout': '60',
        }
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', caps)

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
