import os
import sys

from appium import webdriver
from behave import given, when, then, step
from time import sleep

PAGE_NAVIGATION_TIMER    = 3
IDLE_TIMER               = 2

@given('the app is launched')
def step_impl(context):
    try:
        context.reddit_home_page.skip_on_board_page()
        return
    except Exception as e:
        raise e
    finally:
        sleep(PAGE_NAVIGATION_TIMER)

@when(u'"{searchedterm}" is entered')
def step_impl(context, searchedterm):
    context.reddit_home_page.input_searched_term(searchedterm)
    sleep(IDLE_TIMER)
    context.reddit_home_page.send_enter_key()
    sleep(PAGE_NAVIGATION_TIMER)

@then(u'should be able to see the "{searchedterm}" results')
def step_impl(context, searchedterm):
    assert context.reddit_home_page.check_searched_result_is_displayed(searchedterm) is True
    sleep(IDLE_TIMER)

@when(u'tap on the "{searchedterm}" in the searched result list')
def step_impl(context, searchedterm):
    context.reddit_home_page.tap_on_the_searched_result(searchedterm)
    sleep(PAGE_NAVIGATION_TIMER)

@then(u'check "{checkterm}" in the recent posted title')
def step_impl(context, checkterm):
    assert context.reddit_home_page.check_specific_term_in_top_posted_title(checkterm) is True
