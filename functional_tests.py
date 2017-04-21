#!/usr/bin/env python3


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)
        
    def tearDown(self):
        self.browser.quit()
        
    def test_can_start_a_list_and_retrive_it_later(self):
        #Idis heard there is a super cool online TO-DO app
        #She goes to check the app's page
        self.browser.get('http://127.0.0.1:8000')

        #She noticed that both title and header of the page contain the word "TO-DO" 
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-DO', header_text)

        #The app invite her to enter a to-do item
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get-attribute('placeholder'),
            'Enter a to-do item'
        )

        #She enters "Buy peacock feathers" into the text area
        #Her habbit is to use make fly
        inputbox.send_keys('Buy peacock feathers')

        #After hitting ENTER, the page refreshed
        #The To-Do list shows "1: Buy peacock freathers"
        inputbox.send_keys(keys.ENTER)
        
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1: Buy peacock feathers' for row in rows)
        )

        #The page shows another text area to enter other To-Do items
        #She enters "Use peacock feathers to make a fly" 
        self.fail('Finish the test!')

        #The page refreshed again,there are two items in her list

        #Idis wants to know wether this website could remember her list

        #She saw the website generate a unique URL for her
        #And there are some text to explain this feature

        #She checked that URL,found that her list is still there

        #She is satisfied,and gone to sleep

if __name__ == '__main__':
    unittest.main(warnings='ignore')