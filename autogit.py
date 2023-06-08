import unittest
from selenium import webdriver 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class GitLogin:
    def __init__(self, driver):
        self.driver = driver
        self.username_input = (By.ID, "login_field")
        self.password_input = (By.ID, "password")
        self.sign_in = (By.CSS_SELECTOR, "input[value='Sign in']")

    def set_username(self, username):
        self.driver.find_element(*self.username_input).send_keys(username)

    def set_password(self, password):
        self.driver.find_element(*self.password_input).send_keys(password)

    def click_enter(self):
        self.driver.find_element(*self.sign_in).click()

class MakeRepo:
    def __init__ (self, driver):
        self.driver = driver
        self.namerepo = (By.ID,"react-aria-2")
        self.description = (By.ID,"react-aria-3")
        #public
        self.public = (By.ID, "react-aria-5")
        #private
        self.private = (By.ID, "react-aria-6")
        self.readme = (By.ID, "react-aria-8")
        self.button = (By.XPATH,"//button[@class='types__StyledButton-sc-ws60qy-0 fAcoGo']") 

    
    def name(self,name):
        self.driver.find_element(*self.namerepo).send_keys(name)

    def descrip(self,description):
        self.driver.find_element(*self.description).send_keys(description)
    
    def setpriv(self):
        self.driver.find_element(*self.private).click()

    def setpub(self):
        self.driver.find_element(*self.public).click()

    def makereadme(self):
        self.driver.find_element(*self.readme).click()
    
    def clickbutton(self):
        self.driver.find_element(*self.button).click()

class DeleteRepo:
    def __init__(self,driver):
        self.driver = driver
        self.settings = (By.ID,"settings-tab")
        #self.delbutton = (By.CLASS_NAME, "js-repo-delete-button Button--danger Button--medium Button")
        self.delbutton = (By.XPATH,"//*[contains(text(), 'Delete this repository')]")
        self.confirmation = (By.ID, "repo-delete-proceed-button")#click two times cause two confirmations
        self.typerepo = (By.ID, "verification_field")
        self.finaldelete = (By.ID,"repo-delete-proceed-button")

    def setting(self):
        self.driver.find_element(*self.settings).click()

    def deletebutton(self):
        self.driver.find_element(*self.delbutton).click()

    def confirm(self):
        for i in range(2):
            self.driver.find_element(*self.confirmation).click()

    def inputkeys(self,u):
        self.driver.find_element(*self.typerepo).send_keys(u)

    def finaldel(self):
        self.driver.find_element(*self.finaldelete).click()

class TestGit(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.get("https://github.com/login")
        test = GitLogin(self.driver)
        GitLogin.set_username(test,"username")
        GitLogin.set_password(test,"password")
        GitLogin.click_enter(test)
        WebDriverWait(self.driver, 10).until(EC.title_contains("GitHub"))

    def stop(self):
        self.driver.quit()

    def test_makerepo(self):
        test = MakeRepo(self.driver)
        self.driver.execute_script("window.open('about:blank', 'new_window')")
        self.driver.switch_to.window("new_window")
        self.driver.get("https://github.com/new")
        MakeRepo.name(test,"testu")
        MakeRepo.descrip(test,"a little testu")
        MakeRepo.setpriv(test)
        MakeRepo.makereadme(test)
        MakeRepo.clickbutton(test)

    def test_deleterepo(self):
        repo_to_delete = "testu"
        test = DeleteRepo(self.driver)
        self.driver.execute_script("window.open('about:blank', 'new_window')")
        self.driver.switch_to.window("new_window")
        self.driver.get(f"https://github.com/username/{repo_to_delete}")
        DeleteRepo.setting(test)
        self.driver.get("https://www.youtube.com/")#if I don't include this line SCROLLING DOES NOT WORK 
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        DeleteRepo.deletebutton(test)
        DeleteRepo.confirm(test)
        DeleteRepo.inputkeys(test,f"username/{repo_to_delete}")
        DeleteRepo.finaldel(test)


if __name__ == "__main__":
    start = TestGit()
    start.setUp()
    #driver.title btn btn-sm btn-primary= GitHub

