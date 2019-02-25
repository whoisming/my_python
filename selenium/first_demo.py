import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("http://www.tengyue360.com")
        self.assertIn("腾跃校长在线，K12教培机构一站式办学服务运营商【官网】", driver.title)
        #elem = driver.find_element_by_xpath('/html/body/div[1]/div[1]/section/div[5]') 绝对路径模式
        elem = driver.find_element_by_xpath('//section/div[@class=app-load nav]')
        elem.click()
        #elem.send_keys(Keys.RETURN)
        self.assertIn("腾跃校长在线APP下载，15万校长的坚定选择", driver.title)


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()