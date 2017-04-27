#!/usr/bin/env python3
from .base import FunctionalTest
from selenium.webdriver.common.keys import Keys
import time

    
class LayoutAndStylingTest(FunctionalTest):
    
    def test_layout_and_styling(self):
        #Idith visit the main page
        self.browser.get(self.live_server_url)
        self.browser.set_window_size(1024, 768)
        time.sleep(1)
        
        #She see that the input box is perfectly aligned to center
        inputbox = self.get_item_input_box()
        self.assertAlmostEqual(
            inputbox.location['x'] + inputbox.size['width'] / 2,
            512,
            delta = 5
        )
        
        #She enter a new list,see that the input box still aligned to center
        inputbox.send_keys('testing\n')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)
        inputbox = self.get_item_input_box()
        self.assertAlmostEqual(
            inputbox.location['x'] + inputbox.size['width'] / 2,
            512,
            delta = 5
        )
    