import unittest
from pyunitreport import HTMLTestRunner
from seleniumm import webdriver

class HelloWorld(unittest.TestCase):
    
    def setUp(self):
        return super().setUp()

    def test_hello_world(self):
        pass

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity = 2, testRunner = HTMLTestRunner(output = 'reportes', report_name = 'hello-world-report' ))

    