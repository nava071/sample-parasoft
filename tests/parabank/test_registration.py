import pytest, random, string
from playwright.sync_api import Page, expect
from pageobjects.registration import Registration


@pytest.fixture()
def register_page(page: Page):

    rp = Registration()
    rp.generate_random_form_values()
    # page.goto(rp.BASE_URL)
    # expect(page).to_have_url(rp.BASE_URL+"/parabank/index.htm")
    return rp
   
@pytest.mark.xfail()
@pytest.mark.parametrize(
    "updated_value",
    [pytest.param(None,id="empty"),
    pytest.param('',id="no character"),
    pytest.param(str(random.randint(1000, 10000)),id="one number"),
    pytest.param(''.join(random.choices(string.ascii_letters)),id="length=1"),
    pytest.param(''.join(random.choices(string.ascii_letters, k=2)),id="length=2"),
    pytest.param(''.join(random.choices(string.ascii_letters, k=8)),id="length=8"),
    pytest.param(''.join(random.choices(string.ascii_letters, k=32)),id="length=32"),
    pytest.param(''.join(random.choices(string.ascii_letters, k=64)),id="length=64"),
    pytest.param(''.join(random.choices(string.ascii_letters, k=128)),id="length=128"),
    ]
)
def test_registration_with_different_values_on_firstname(page: Page, register_page, updated_value):
    register_page.navigate_to_registration_page(page)
    register_page.fill_values()

    page.locator(register_page.FIRSTNAME).clear()
    if updated_value:
        page.locator(register_page.FIRSTNAME).fill(updated_value)

    register_page.submit_registration()
    
    expect(page).to_have_title(register_page.POST_REGISTRATION_TITLE)
    expect(page.locator(register_page.ACCOUNT_SERVICES_TXT)).to_be_visible()
    assert page.locator(f'text="Welcome {register_page.username_val}"').text_content() == f"Welcome {register_page.username_val}"
    assert page.locator("text=Your account was created successfully. You are now logged in.").text_content() == "Your account was created successfully. You are now logged in."

    page.locator(register_page.LOGOUT).click()
    expect(page).to_have_url("https://parabank.parasoft.com/parabank/index.htm?ConnType=JDBC")
    expect(page).to_have_title(register_page.INDEX_TITLE)

@pytest.mark.xfail()
@pytest.mark.parametrize(
    "updated_value",
    [pytest.param(None,id="empty"),
    pytest.param('',id="no character"),
    pytest.param(str(random.randint(1000, 10000)),id="one number"),
    pytest.param(''.join(random.choices(string.ascii_letters)),id="length=1"),
    pytest.param(''.join(random.choices(string.ascii_letters, k=2)),id="length=2"),
    pytest.param(''.join(random.choices(string.ascii_letters, k=8)),id="length=8"),
    pytest.param(''.join(random.choices(string.ascii_letters, k=32)),id="length=32"),
    pytest.param(''.join(random.choices(string.ascii_letters, k=64)),id="length=64"),
    pytest.param(''.join(random.choices(string.ascii_letters, k=128)),id="length=128"),
    ]
)
def test_registration_with_different_values_on_lastname(page: Page, register_page, updated_value):
    register_page.navigate_to_registration_page(page)
    register_page.fill_values()

    page.locator(register_page.LASTNAME).clear()
    if updated_value:
        page.locator(register_page.LASTNAME).fill(updated_value)

    register_page.submit_registration()
    
    expect(page).to_have_title(register_page.POST_REGISTRATION_TITLE)
    expect(page.locator(register_page.ACCOUNT_SERVICES_TXT)).to_be_visible()
    assert page.locator(f'text="Welcome {register_page.username_val}"').text_content() == f"Welcome {register_page.username_val}"
    assert page.locator("text=Your account was created successfully. You are now logged in.").text_content() == "Your account was created successfully. You are now logged in."

    page.locator(register_page.LOGOUT).click()
    expect(page).to_have_url("https://parabank.parasoft.com/parabank/index.htm?ConnType=JDBC")
    expect(page).to_have_title(register_page.INDEX_TITLE)

@pytest.mark.xfail()
@pytest.mark.parametrize(
    "updated_value",
    [pytest.param(None,id="empty"),
    pytest.param('',id="no character"),
    pytest.param(str(random.randint(1000, 10000)),id="one number"),
    pytest.param(''.join(random.choices(string.ascii_letters)),id="length=1"),
    pytest.param(''.join(random.choices(string.ascii_letters, k=2)),id="length=2"),
    pytest.param(''.join(random.choices(string.ascii_letters, k=8)),id="length=8"),
    pytest.param(''.join(random.choices(string.ascii_letters, k=32)),id="length=32"),
    pytest.param(''.join(random.choices(string.ascii_letters, k=64)),id="length=64"),
    pytest.param(''.join(random.choices(string.ascii_letters, k=128)),id="length=128"),
    ]
)
def test_registration_with_different_values_on_username(page: Page, register_page, updated_value):
    register_page.navigate_to_registration_page(page)
    register_page.fill_values()

    page.locator(register_page.USERNAME).clear()
    if updated_value:
        page.locator(register_page.USERNAME).fill(updated_value)

    register_page.submit_registration()
    
    expect(page).to_have_title(register_page.POST_REGISTRATION_TITLE)
    expect(page.locator(register_page.ACCOUNT_SERVICES_TXT)).to_be_visible()
    assert page.locator(f'text="Welcome {register_page.username_val}"').text_content() == f"Welcome {register_page.username_val}"
    assert page.locator("text=Your account was created successfully. You are now logged in.").text_content() == "Your account was created successfully. You are now logged in."

    page.locator(register_page.LOGOUT).click()
    expect(page).to_have_url("https://parabank.parasoft.com/parabank/index.htm?ConnType=JDBC")
    expect(page).to_have_title(register_page.INDEX_TITLE)

@pytest.mark.xfail()
@pytest.mark.parametrize(
    "updated_value",
    [pytest.param(None,id="empty"),
    pytest.param('',id="no character"),
    pytest.param(str(random.randint(1000, 10000)),id="number"),
    pytest.param(''.join(random.choices(string.ascii_letters)),id="length=1"),
    pytest.param(''.join(random.choices(string.ascii_letters, k=2)),id="length=2"),
    pytest.param(''.join(random.choices(string.ascii_letters, k=8)),id="length=8"),
    pytest.param(''.join(random.choices(string.ascii_letters, k=32)),id="length=32"),
    pytest.param(''.join(random.choices(string.ascii_letters, k=64)),id="length=64"),
    pytest.param(''.join(random.choices(string.ascii_letters, k=128)),id="length=128"),
    ]
)
def test_registration_with_different_values_on_ssn(page: Page, register_page, updated_value):
    register_page.navigate_to_registration_page(page)
    register_page.fill_values()

    page.locator(register_page.SSN).clear()
    if updated_value:
        page.locator(register_page.SSN).fill(updated_value)

    register_page.submit_registration()
    
    expect(page).to_have_title(register_page.POST_REGISTRATION_TITLE)
    expect(page.locator(register_page.ACCOUNT_SERVICES_TXT)).to_be_visible()
    assert page.locator(f'text="Welcome {register_page.username_val}"').text_content() == f"Welcome {register_page.username_val}"
    assert page.locator("text=Your account was created successfully. You are now logged in.").text_content() == "Your account was created successfully. You are now logged in."

    page.locator(register_page.LOGOUT).click()
    expect(page).to_have_url("https://parabank.parasoft.com/parabank/index.htm?ConnType=JDBC")
    expect(page).to_have_title(register_page.INDEX_TITLE)