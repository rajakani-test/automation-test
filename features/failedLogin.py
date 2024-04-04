from behave import *
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService


@given('I am on the demo login page')
def demoLog(context):
    context.browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    context.browser.implicitly_wait(5)
    context.driver.get("https://www.saucedemo.com/")

@when('I fill the account information for account LockedOutUser into the username field and the password field')
def  userPas(context):
    username_input = context.driver.find_element_by_id("user_name")
    password_input = context.driver.find_element_by_id("password")
    username_input.send_keys("locked_out_user")
    password_input.send_keys("secret_sauce")

@when('I click the login button')
def loginButton(context):
    login_button = context.driver.find_element_by_id("login-button")
    login_button.click()

@then('I verify the error message contains the text "Sorry, this user has been banned"')
def errorMsg(context):
    error_message = context.driver.find_element_by.Class("error")
    assert "Sorry, this user has been banned" in error_message.text, "Epic sadface: Username and password do not match any user in this service"

@then('I close the browser')

def  closeBrowser(context):
    context.driver.quit()
