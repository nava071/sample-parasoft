import random, string
from playwright.sync_api import expect

class Registration:

    BASE_URL = "https://parabank.parasoft.com"
    REGISTER_LINK = "text=Register"
    REGISTER_SUBMIT = "input:has-text(\"Register\")"
    FIRSTNAME = "input[name=\"customer\\.firstName\"]"
    LASTNAME = "input[name=\"customer\\.lastName\"]"
    STREET = "input[name=\"customer\\.address\\.street\"]"
    CITY = "input[name=\"customer\\.address\\.city\"]"
    STATE = "input[name=\"customer\\.address\\.state\"]"
    USERNAME = "input[name=\"customer\\.username\"]"
    ZIPCODE = "input[name=\"customer\\.address\\.zipCode\"]"
    PHONENO = "input[name=\"customer\\.phoneNumber\"]"
    SSN = "input[name=\"customer\\.ssn\"]"
    PASSWORD = "input[name=\"customer\\.password\"]"
    REPEAT_PASSWORD = "input[name=\"repeatedPassword\"]"
    LOGOUT = "text=Log Out"

    ACCOUNT_SERVICES_TXT = "text=Account Services"
    REGISTRATION_TITLE = "ParaBank | Register for Free Online Account Access"
    POST_REGISTRATION_TITLE = "ParaBank | Customer Created"
    INDEX_TITLE = "ParaBank | Welcome | Online Banking"


    def __init__(self):
        pass

    def generate_random_form_values(self):
        self.firstname_val = self._random_text(10)
        self.lastname_val = self._random_text(10)
        self.address_val = self._random_text(10)
        self.city_val = self._random_text(10)
        self.state_val = self._random_text(10)
        self.username_val = self._random_text(10)
        self.password_val = self._random_text(10)
        self.zip_val = self._random_digits(6)
        self.phoneno_val = self._random_digits(10)
        self.ssn_val = self._random_digits(9)

    def navigate_to_registration_page(self, page):
        self.page = page
        self.page.goto(self.BASE_URL)
        expect(self.page).to_have_url(self.BASE_URL+"/parabank/index.htm")

        self.page.locator(self.REGISTER_LINK).click()
        expect(self.page).to_have_title(self.REGISTRATION_TITLE)

    def fill_values(self):
        self.page.locator(self.FIRSTNAME).click()
        self.page.locator(self.FIRSTNAME).fill(self.firstname_val)
        self.page.locator(self.LASTNAME).click()
        self.page.locator(self.LASTNAME).fill(self.lastname_val)
        self.page.locator(self.STREET).click()
        self.page.locator(self.STREET).fill(self.address_val)
        self.page.locator(self.CITY).click()
        self.page.locator(self.CITY).fill(self.city_val)
        self.page.locator(self.STATE).click()
        self.page.locator(self.STATE).fill(self.state_val)
        self.page.locator(self.ZIPCODE).click()
        self.page.locator(self.ZIPCODE).fill(self.zip_val)
        self.page.locator(self.PHONENO).click()
        self.page.locator(self.PHONENO).fill(self.phoneno_val)
        self.page.locator(self.SSN).click()
        self.page.locator(self.SSN).fill(self.ssn_val)
        self.page.locator(self.USERNAME).click()
        self.page.locator(self.USERNAME).fill(self.username_val)
        self.page.locator(self.PASSWORD).click()
        self.page.locator(self.PASSWORD).fill(self.password_val)
        self.page.locator(self.REPEAT_PASSWORD).click()
        self.page.locator(self.REPEAT_PASSWORD).fill(self.password_val)

    def submit_registration(self):
        self.page.locator(self.REGISTER_SUBMIT).click()
    
    def _random_text(self, k):
        return ''.join(random.choices(string.ascii_lowercase+string.ascii_uppercase, k=k))

    def _random_digits(self, k):
        return ''.join(random.choices(string.digits, k=k))


