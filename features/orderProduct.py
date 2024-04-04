from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By

@given('I am on the inventory page')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://www.saucedemo.com/inventory.html")

@when('user sorts products from low price to high price')
def step_impl(context):
    sort_select = context.driver.find_element(By.CLASS_NAME, "product_sort_container")
    sort_select.click()
    sort_option = context.driver.find_element(By.XPATH, "//option[text()='Price (low to high)']")
    sort_option.click()

@when('user adds the lowest priced product')
def step_impl(context):
    add_to_cart_buttons = context.driver.find_elements(By.XPATH, "//button[text()='ADD TO CART']")
    add_to_cart_buttons[0].click()

@when('user clicks on cart')
def step_impl(context):
    cart_button = context.driver.find_element(By.CLASS_NAME, "shopping_cart_link")
    cart_button.click()

@when('user clicks on checkout')
def step_impl(context):
    checkout_button = context.driver.find_element(By.XPATH, "//a[text()='CHECKOUT']")
    checkout_button.click()

@when('user enters first name "{first_name}"')
def step_impl(context, first_name):
    first_name_input = context.driver.find_element_by_id("lfirst_name_input")
    first_name_input.send_keys("Jhon")

@when('user enters last name "{last_name}"')
def step_impl(context, last_name):
    last_name_input = context.driver.find_element_by_id("last-name")
    last_name_input.send_keys("Deo")

@when('user enters zip code "{123}"')
def step_impl(context, zip_code):
    zip_code_input = context.driver.find_element(By.ID, "zip-code")
    zip_code_input.send_keys(123)

@when('user clicks continue button')
def step_impl(context):
    continue_button = context.driver.find_element(By.XPATH, "//input[@value='CONTINUE']")
    continue_button.click()

@then('I verify in the checkout overview page if the total amount for the added item is ${expected_total}')
def step_impl(context, expected_total):
    actual_total = context.driver.find_element(By.CLASS_NAME, "summary_total_label").text
    assert actual_total == expected_total, f"Expected total: {expected_total}. Actual total: {actual_total}"

@when('user clicks finish button')
def step_impl(context):
    finish_button = context.driver.find_element(By.XPATH, "//a[text()='FINISH']")
    finish_button.click()

@then('"{header_text}" header is shown in the checkout complete page')
def step_impl(context, header_text):
    header = context.driver.find_element(By.CLASS_NAME, "complete-header").text
    assert header == header_text, f"Expected header: {header_text}. Actual header: {header}"

@then('I close the browser')
def step_impl(context):
    context.driver.quit()
