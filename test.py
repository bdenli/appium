import unittest
from appium import webdriver
#from selenium import webdriver

# Set the desired capapbilities, be sure to change the values accordingly
desired_caps = {}
desired_caps['platformName'] = 'iOS'
#desired_caps['platformVersion'] = '16.4'
desired_caps['deviceName'] = 'My-Amazing-Simulator' # "xcrun simctl list" will return list of all simulators
#desired_caps['udid'] = '71C90C81-231C-4F59-A90C-339B4110DDE8' --> Unique device identifier of the connected physical device
#desired_caps['bundleId'] = 'com.apple.news'
#desired_caps['app'] = '/path/to/my.app'
desired_caps['automationName'] = 'XCUITest'
desired_caps['usePrebuiltWDA'] = True
desired_caps['browserName'] = 'Safari'

'''
DeprecationWarning: desired_capabilities argument is deprecated and will be removed in future versions. Use options instead.
{
    "platformName": "iOS",
    "appium:options": {
        "automationName": "XCUITest",
        "platformVersion": "16.0",
        "app": "/path/to/your.app",
        "deviceName": "iPhone 12",
        "noReset": true
    }
}
'''

#appium_server_url = 'http://localhost:4723/wd/hub' --> this is depricated for Appium 2.x
appium_server_url = 'http://localhost:4723'

class TestAppium(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Remote(appium_server_url, desired_caps)

    def tearDown(self) -> None:
        if self.driver:
            self.driver.quit()

    def test_open_browser(self) -> None:
        self.driver.get(r'https://applitools.com/helloworld')


if __name__ == '__main__':
    unittest.main()