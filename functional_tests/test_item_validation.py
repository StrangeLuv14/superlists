#!/usr/bin/env python3
from .base import FunctionalTest
from unittest import skip
    
class ItemValidationTest(FunctionalTest):
    
    def test_cannot_add_empty_list_items(self):
        #Idith visit the home page,enter a empty item accidently
        #The input box does not have content, she pressed the ENTER
        
        #Home page refreshed,a error message shows
        #Suggesting the item can not be empty
        
        #She entered some text,then submit again,this time is ok
        
        #She's been nappy,submit a empty item again
        
        #At the item page she sees a similar error message
        
        #Enter some text,then alright
        self.fail('write me!')