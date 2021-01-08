from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()
    
    def tearDown(self):
        self.browser.quit()
    
    def test_can_start_a_list_and_retrieve_it_later(self):
        self.browser.get('http://localhost:8000')

        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')


# Invited to enter a to-do item right away

#Types in "Buy peacock feathers" in to a text box

#When she hits enter the page updates and the item is added to the list
# "1. Buy peacock feathers" as an item in the list

# Enters "Use peacock feathers to make a fly"

# The page updates again, and now shows both items on her list

#Unique URL generated for the list

# Vist unique url

if __name__ == '__main__':
    unittest.main()