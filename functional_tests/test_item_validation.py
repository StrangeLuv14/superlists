#!/usr/bin/env python3
from .base import FunctionalTest
from selenium.webdriver.common.keys import Keys
import time
    
class ItemValidationTest(FunctionalTest):
    
    def test_cannot_add_empty_list_items(self):
        #Idith visit the home page,enter a empty item accidently
        #The input box does not have content, she pressed the ENTER
        self.browser.get(self.live_server_url)
        self.get_item_input_box().send_keys(Keys.ENTER)
        
        #Home page refreshed,a error message shows
        #Suggesting the item can not be empty
        self.wait_for(lambda: self.browser.find_element_by_css_selector(
        '#id_text:invalid'
        ))
        
        #She entered some text,then submit again,this time is ok
        self.get_item_input_box().send_keys('Buy milk')
        self.get_item_input_box().send_keys(Keys.ENTER)
        
        self.wait_for_row_in_list_table('1: Buy milk')
        
        #She's been naughty,submit a empty item again
        self.get_item_input_box().send_keys(Keys.ENTER)
        
        #At the item page she sees a similar error message
        self.wait_for_row_in_list_table('1: Buy milk')
        self.wait_for(lambda: self.browser.find_element_by_css_selector(
        '#id_text:invalid'
        ))
        
        #Enter some text,then alright
        self.get_item_input_box().send_keys('Make tea')
        self.get_item_input_box().send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy milk')
        self.wait_for_row_in_list_table('2: Make tea')
        
        
    def test_cannot_add_duplicate_items(self):
        #Idith visit home page and create a new list
        self.browser.get(self.live_server_url)
        self.get_item_input_box().send_keys('Buy wellies')
        self.get_item_input_box().send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy wellies')
        
        #She accdiently enter a duplicate item
        self.get_item_input_box().send_keys('Buy wellies')
        self.get_item_input_box().send_keys(Keys.ENTER)
        
        #She see a helpful error message
        self.wait_for(lambda: self.assertEqual(
            self.browser.find_element_by_css_selector('.has-error').text,
             "You've already got this in your list"
        ))
        
        
        