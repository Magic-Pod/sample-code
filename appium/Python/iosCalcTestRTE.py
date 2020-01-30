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


class OpenUrlTest(unittest.TestCase):
    def setUp(self):
        caps = {
            'userName': RTE_USERNAME,
            'password': RTE_PASSWORD,
            'logLevel': 'info',
            'platformName': 'iOS',
            'deviceName': 'iPhone',
            'platformVersion': '12',
            'bundleId': 'com.apple.calculator'
        }
        self.driver = webdriver.Remote(RTE_URL, caps)
        print(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test_calculator(self):
        print(self.driver.capabilities['snapshotUrl'])
        driver = self.driver
        self.driver.save_screenshot('capture_01.png')
        el1 = driver.find_element_by_accessibility_id("1")
        el1.click()
        self.driver.save_screenshot('capture_02.png')


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(OpenUrlTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
