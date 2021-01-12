from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()
    
    def tearDown(self):
        self.browser.quit()
    
    def test_can_start_a_list_and_retrieve_it_later(self):
        self.browser.get('http://localhost:8000')

        # test the page title and header 
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # Invited to enter a to-do item right away
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(inputbox.get_attribute('placeholder'),'Enter a to-do item')

        #Types in "Buy peacock feathers" in to a text box
        inputbox.send_keys('Buy peacock feathers')
        
        #When she hits enter the page updates and the item is added to the list
        # "1. Buy peacock feathers" as an item in the list
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1: Buy peacock feathers' for row in rows)
        )        
        
        # Enters "Use peacock feathers to make a fly"

        # The page updates again, and now shows both items on her list

        #Unique URL generated for the list

        # Vist unique url
        
        self.fail('Finish the test!')
if __name__ == '__main__':
    unittest.main()