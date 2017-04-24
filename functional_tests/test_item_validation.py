#!/usr/bin/env python3
from .base import FunctionalTest
    
class ItemValidationTest(FunctionalTest):
    
    def test_cannot_add_empty_list_items(self):
        #Idith visit the home page,enter a empty item accidently
        #The input box does not have content, she pressed the ENTER
        self.browser.get(self.live_server_url)
        self.browser.find_element_by_id('id_new_item').send_keys('\n')
        
        #Home page refreshed,a error message shows
        #Suggesting the item can not be empty
        error = self.browser.find_element_by_css_selector('.has-error')
        self.assertEqual(error.text, "You can't have an empty list item")
        
        #She entered some text,then submit again,this time is ok
        self.browser.find_element_by_id('id_new_item').send_keys('Buy milk\n')
        self.check_for_row_in_list_table('1: Buy milk')
        
        #She's been naughty,submit a empty item again
        self.browser.find_element_by_id('id_new_item').send_keys('\n')
        
        #At the item page she sees a similar error message
        self.check_for_row_in_list_table('1: Buy milk')
        error = self.browser.find_element_by_css_selector('.has-error')
        self.assertEqual(error.text, "You can't have an empty list item")
        
        #Enter some text,then alright
        self.browser.find_element_by_id('id_new_item').send_keys('Make tea\n')
        self.check_for_row_in_list_table('1: Buy milk')
        self.check_for_row_in_list_table('2: Make tea')