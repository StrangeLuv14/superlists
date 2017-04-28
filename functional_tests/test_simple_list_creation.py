#!/usr/bin/env python3
from .base import FunctionalTest
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time
        
        
class NewVisitorTest(FunctionalTest):
    
    def test_can_start_a_list_and_retrieve_it_later(self):
        #Idith heard there is a super cool online TO-DO app
        #She goes to check the app's page
        self.browser.get(self.live_server_url)

        #She noticed that both title and header of the page contain the word "TO-DO" 
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        #The app invite her to enter a to-do item
        inputbox = self.get_item_input_box()
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        #She enters "Buy peacock feathers" into the text area
        #Her habbit is to use make fly
        inputbox.send_keys('Buy peacock feathers')

        #After hitting ENTER, she is brought to a new URL
        #The To-Do list in this page shows "1: Buy peacock feathers"
        inputbox.send_keys(Keys.ENTER)
        #wait page to redirect
        time.sleep(1)
        edith_list_url = self.browser.current_url
        self.assertRegex(edith_list_url, '/lists/.+')
        self.wait_for_row_in_list_table('1: Buy peacock feathers')

        #The page shows another text area to enter other To-Do items
        #She enters "Use peacock feathers to make a fly" 
        inputbox = self.get_item_input_box()
        inputbox.send_keys('Use peacock feathers to make a fly')
        inputbox.send_keys(Keys.ENTER)

        #The page refreshed again,there are two items in her list
        self.wait_for_row_in_list_table('1: Buy peacock feathers')
        self.wait_for_row_in_list_table('2: Use peacock feathers to make a fly')

        #Idith wants to know wether this website could remember her list
        #She saw the website generate a unique URL for her
        #And there are some text to explain this feature
    
        #Now a new user called Francis visit the website
        
        ##We use a new browser dialog
        ##Make sure Idith's info won't leak from cookie
        self.browser.quit()
        self.browser = webdriver.Firefox()
        
        #Francis visits home page
        #The home page won't show Idith's To-Do list
        self.browser.get(self.live_server_url)
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers', page_text)
        self.assertNotIn('make a fly', page_text)
        
        #Francis enter a new item, make a new To-Do list
        inputbox = self.get_item_input_box()
        inputbox.send_keys('Buy milk')
        inputbox.send_keys(Keys.ENTER)
        #wait page to redirect
        time.sleep(1)
        
        #Francis get a unique URL of his own
        francis_list_url = self.browser.current_url
        self.assertRegex(francis_list_url, '/lists/.+')
        self.assertNotEqual(francis_list_url, edith_list_url)
        
        #This page still do not have edith's list
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers', page_text)
        self.assertIn('Buy milk', page_text)
        
        #Both of them are satisfied, and gone to sleep
    