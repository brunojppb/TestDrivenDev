from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    #setUp and tearDown are special methods 
    #which get run before and after each test.
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        #Edith has heard about a cool new online to-do app.
        #She goes to check out its homepage
        self.browser.get('http://localhost:8000')

        #She notices the page title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')

        #She is invited to enter a to-do item straight away


        #When she types "Buy peacock feathers" into a text box (Edith's hobby)
        #is tying fly-fishing lures)

        #When she hits enter, the page updates, and now the page list
        #"1: Buy peacock feathers" as an item in a to-do list

        #There is still a text box inviting her to add another item.
        #She enters "Use peacock feathers to make a fly" (Edith is very methodical)

        #The page updates again, and now shows both items on her list

        #Edith wonders whether the site will remember her list. Then she sees
        #that the site has generated a unique URL for her -- There is some
        #explanatory text to that effect

        #She visits that URL - Her to-do list still there

        #Satisfied, she goes back to sleep


if __name__ == '__main__':
    #We call unittest.main(), which launches the unittest test runner, 
    #which will automatically find test classes and methods in the file and run them.
    unittest.main(warnings='ignore')

