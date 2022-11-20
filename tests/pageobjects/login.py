from playwright.sync_api import expect

class Login:
    BASE_URL = "https://parabank.parasoft.com"
    LOGIN_URL = BASE_URL+"/parabank/index.htm"
    USERNAME = "input[name=\"username\"]"
    PASSWORD = "input[name=\"password\"]"
    LOGIN = "text=Log In"
    ERROR_TITLE = "ParaBank | Error"

    def __init__(self, page):
        self.page = page

    def fill_username(self, usrname):
        self.page.locator(self.USERNAME).click()
        self.page.locator(self.USERNAME).fill(usrname)

    def fill_password(self, pwd):
        self.page.locator(self.PASSWORD).click()
        self.page.locator(self.PASSWORD).fill(pwd)

    def submit(self):
        self.page.locator(self.LOGIN).click()
