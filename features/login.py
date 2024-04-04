import time

from behave import *
from selenium.common import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService


def before_scenario(context):
    context.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    context.driver.maximize_window()

def after_scenario(context):
    context.driver.quit()


@given('I am on the Demo login page')
def logiPage(context):

    context.driver.get("https://www.saucedemo.com/")


@when('I fill the account information for account standarduser into the username field and the password field')
def namePass(context):
    username_input = context.driver.find_element_by_id("user_name")
    password_input = context.driver.find_element_by_id("password")
    username_input.send_keys("standard_user")
    password_input.send_keys("secret_sauce")


@when('I click the login button')
def loginButton(context):
    login_button = context.driver.find_element_by_id("login-button")
    login_button.click()

@then ('I am redirected to the demo main page')

def mainPage(context):

        expected_url = "https://www.saucedemo.com/inventory.html"
        current_url = context.browser.current_url

        assert current_url == expected_url, f"Expected URL: {expected_url}. Actual URL: {current_url}"


@then('I verify the App Logo exists')
def loGo(context):
    try:

        app_logo = context.browser.find_element_by_id('app-logo')

        assert app_logo.is_displayed(), "App Logo exists"

    except NoSuchElementException:

        assert False, "App Logo does not exist"
