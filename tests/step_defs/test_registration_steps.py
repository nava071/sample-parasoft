from pytest_bdd import scenarios, scenario, given, when, then, step
from playwright.sync_api import Page, expect
import pytest, requests

from pageobjects.registration import Registration
from pageobjects.login import Login


scenarios("../features/registration.feature")

@pytest.fixture()
def registerpage():

    registration_page = Registration()
    registration_page.generate_random_form_values()
    return registration_page

@given("I provide my details in the registration form", target_fixture="register")
@step("I provide the same details again in the registration form")
def input_details_in_registration_form(registerpage, page:Page):
    registerpage.navigate_to_registration_page(page)
    registerpage.fill_values()
    return registerpage


@step("I click register button")
def register_(register):
    register.submit_registration()

@then("the registration should be successful")
@step("the registration is successful")
def post_register(page:Page, register):
    expect(page).to_have_title(register.POST_REGISTRATION_TITLE)
    expect(page.locator(register.ACCOUNT_SERVICES_TXT)).to_be_visible()
    assert page.locator(f'text="Welcome {register.username_val}"').text_content() == f"Welcome {register.username_val}"
    assert page.locator("text=Your account was created successfully. You are now logged in.").text_content() == "Your account was created successfully. You are now logged in."
    page.locator(register.LOGOUT).click()
    expect(page).to_have_url("https://parabank.parasoft.com/parabank/index.htm?ConnType=JDBC")
    expect(page).to_have_title(register.INDEX_TITLE)
    
@then("I should be able to login with the registered creds")
def login_with_registered_creds(register, page:Page):
    login = Login(page)
    page.goto(login.LOGIN_URL)
    login.fill_username(register.username_val)
    login.fill_password(register.password_val)
    login.submit()
    expect(page).not_to_have_title(register.INDEX_TITLE)
    expect(page).not_to_have_title(login.ERROR_TITLE)

@then("the registration should not be successful")
def register_twice_should_fail(page:Page, register):
    expect(page).not_to_have_title(register.POST_REGISTRATION_TITLE)
    expect(page.locator(f'text="Welcome {register.username_val}"')).not_to_be_visible()
    expect(page.locator("text=Your account was created successfully. You are now logged in.")).not_to_be_visible()


@given("I send my details to registration api", target_fixture="register_api")
def register_api(registerpage):
    url = "https://parabank.parasoft.com/parabank/register.htm"
    response = requests.request("GET", url)
    assert response.status_code == 200
    # print(response.headers['set-cookie'].split(';')[0])
    assert "JSESSIONID" in response.headers['set-cookie'].split(';')[0]

    payload= {"customer.firstName": registerpage.firstname_val,
        "customer.lastName": registerpage.lastname_val,
        "customer.address.street": registerpage.address_val,
        "customer.address.city": registerpage.city_val,
        "customer.address.state": registerpage.state_val,
        "customer.address.zipCode": registerpage.zip_val,
        "customer.phoneNumber": registerpage.phoneno_val,
        "customer.ssn": registerpage.ssn_val,
        "customer.username": registerpage.username_val,
        "customer.password": registerpage.password_val,
        "repeatedPassword": registerpage.password_val
        }
    headers = {
  'Content-Type': 'application/x-www-form-urlencoded',
  'Cookie': response.headers["set-cookie"].split(';')[0]
        }
    response1 = requests.request("POST", url, headers=headers, data=payload)

    response1.old_session_id = response.headers['set-cookie'].split(';')[0]
    return response1 


@step("the response code is 200")
def registration_response_validation(register_api):
    assert register_api.status_code == 200


@step("I logout")
def logout(register_api):
    # print(register_api.request.headers["cookie"])
    url = "https://parabank.parasoft.com/parabank/logout.htm"
    headers = {
  'Content-Type': 'application/x-www-form-urlencoded',
  'Cookie': register_api.request.headers["cookie"]
        }
    response = requests.request("GET", url, headers = headers)
    assert response.status_code == 200


@step("I should be able to login via the login api")
def login_after_register(registerpage, register_api):
    
    url = "https://parabank.parasoft.com/parabank/index.htm"
    response = requests.request("GET", url)
    assert response.status_code == 200

    url2 = "https://parabank.parasoft.com/parabank/login.htm"
    payload= {"username": registerpage.username_val, "password": registerpage.password_val}
    headers = {
  'Content-Type': 'application/x-www-form-urlencoded',
  'Cookie': register_api.request.headers["cookie"]
        }
    response2 = requests.request("POST", url2, headers=headers, data=payload)
    # print(response2.request.headers)
    # print(response2.headers)
    assert response2.status_code == 200

