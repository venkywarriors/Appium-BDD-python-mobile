import os
import six
import sys
import time
import unittest

from appium import webdriver
from behave.tag_matcher import ActiveTagMatcher, setup_active_tag_values
#from appium import Saucelabs
#from appium import SauceTestCase
#from appium import on_platforms
#from sauceclient import SauceClient

CWD = os.getcwd()
SCREEN_SHOTS_PATH = CWD + "/reports/screenshots/"

__driver_configs = {}

def driver_setup(host, port, appium_version, platform_name, platform_version,
                 device_name, browser_name, device_orientation, test_name, app_uri, saucelabs_user,
                 saucelabs_key, saucelabs_on):
    __driver_configs['host'] = host
    __driver_configs['port'] = port
    __driver_configs['appium_version'] = appium_version
    __driver_configs['platform_name'] = platform_name
    __driver_configs['platform_version'] = platform_version
    __driver_configs['device_name'] = device_name
    __driver_configs['browser_name'] = browser_name
    __driver_configs['device_orientation'] = device_orientation
    __driver_configs['test_name'] = test_name
    __driver_configs['app_uri'] = app_uri
    __driver_configs['saucelabs_user'] = saucelabs_user
    __driver_configs['saucelabs_key'] = saucelabs_key
    __driver_configs['saucelabs_on'] = saucelabs_on

def start_driver(context):
    try:
        context.driver = webdriver.Remote(
        command_executor='http://%s:%s/wd/hub' % (__driver_configs.get('host'),__driver_configs.get('port')),
        desired_capabilities={
            'platformName': __driver_configs.get('platform_name'),
            'platformVersion': __driver_configs.get('platform_version'),
            'deviceName': __driver_configs.get('device_name'),
            'app': (CWD + __driver_configs.get('app_uri'))
        })

        context.platform = __driver_configs.get('platform_name')
        if  context.platform == 'Android':
            from pages.android.reddit_home_page import RedditHomePage
        elif context.platform == 'iOS':
            from pages.iOS.reddit_home_page import RedditHomePage
        else:
            raise RuntimeError('Unrecognized platform: {}'.format(platform))
        context.reddit_home_page = RedditHomePage(context.driver)
    except Exception,e:
        raise e

def take_screenshot(context, filename):
    # ts = time.time()
    # st = time.ctime(ts)
    # screenshot_file =  SCREEN_SHOTS_PATH + filename + st + ".PNG"
    
    context.driver.save_screenshot(filename)

def cleanup_driver(context):
    context.driver.quit()

def teardown_driver(context):
    context.driver.quit()
