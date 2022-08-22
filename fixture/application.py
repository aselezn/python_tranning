from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.contact import ContactHelper

class Application:

    def __init__(self):
        self.wd = webdriver.Chrome()
        self.wd.implicitly_wait(60)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)


    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/index.php")


    def is_element_present(self, how, what):
        try:self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True


    def destroy(self):
        self.wd.quit()
        #метод разрушающий фикстуру (заркрывает браузер)
