import pytest
from selene import browser
from appium.options.android import UiAutomator2Options
from appium import webdriver
from config import config
from qa_guru_lesson_19_2.utils import attach


@pytest.fixture(scope='function', autouse=True)
def mobile_android_management():
    options = UiAutomator2Options().load_capabilities({
        "platformName": "android",
        "platformVersion": "9.0",
        "deviceName": "Google Pixel 3",

        "app": config.APP_URL,

        'bstack:options': {
            "projectName": "First Python project",
            "buildName": "browserstack-build-1",
            "sessionName": "BStack first_test",

            "userName": config.BS_USER,
            "accessKey": config.BS_ACCESS_KEY
        }
    })

    browser.config.driver = webdriver.Remote(config.BS_URL, options=options)
    browser.config.timeout = config.TIMEOUT

    yield

    session_id = browser.driver.session_id

    attach.add_screenshot()
    attach.add_xml()

    browser.quit()

    attach.add_video(session_id)
