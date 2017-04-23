#!/usr/bin/env python3
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
import time
import os


class NewVisitorTest(StaticLiveServerTestCase):
    
    def setUp(self):
        self.browser = webdriver.Firefox()
        staging_server = os.environ.get('STAGING_SERVER')
        if staging_server:
            self.live_server_url = 'http://' + staging_server
        self.browser.implicitly_wait(3)
        
    def tearDown(self):
        self.browser.quit()
        
    def check_for_row_in_list_table(self, row_text):
        #wait page to refresh in case of getting stale element
        time.sleep(1)
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])
        
        
    def test_can_start_a_list_and_retrive_it_later(self):
        #Idith heard there is a super cool online TO-DO app
        #She goes to check the app's page
        self.browser.get(self.live_server_url)

        #She noticed that both title and header of the page contain the word "TO-DO" 
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        #The app invite her to enter a to-do item
        inputbox = self.browser.find_element_by_id('id_new_item')
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
        self.check_for_row_in_list_table('1: Buy peacock feathers')

        #The page shows another text area to enter other To-Do items
        #She enters "Use peacock feathers to make a fly" 
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Use peacock feathers to make a fly')
        inputbox.send_keys(Keys.ENTER)

        #The page refreshed again,there are two items in her list
        self.check_for_row_in_list_table('1: Buy peacock feathers')
        self.check_for_row_in_list_table('2: Use peacock feathers to make a fly')

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
        inputbox = self.browser.find_element_by_id('id_new_item')
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
        self.fail('Finish the test!')
        
    def test_layout_and_styling(self):
        #Idith visit the main page
        self.browser.get(self.live_server_url)
        self.browser.set_window_size(1024, 768)
        
        #She see that the input box is perfectly aligned to center
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertAlmostEqual(
            inputbox.location['x'] + inputbox.size['width'] / 2,
            512,
            delta = 5
        )
        
        #She enter a new list,see that the input box still aligned to center
        inputbox.send_keys('testing\n')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertAlmostEqual(
            inputbox.location['x'] + inputbox.size['width'] / 2,
            512,
            delta = 5
        )