from appium import webdriver
from appium.options.android import UiAutomator2Options


class MobileWrapper:
    def __init__(self):
        self.driver = None
        print('test start')

    def get_driver(self):
        capabilities = dict(
            platformName="Android",
            deviceName="emulator-5554",
            platformVersion="14.0",
            automationName="UiAutomator2",
            appPackage="com.claudivan.taskagenda",
            appActivity=".Activities.MainActivity"
        )

        appium_server_url = 'http://localhost:4723'
        capabilities_options = UiAutomator2Options().load_capabilities(capabilities)
        self.driver = webdriver.Remote(
            command_executor=appium_server_url,
            options=capabilities_options
        )
        return self.driver
