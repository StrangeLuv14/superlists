#!/usr/bin/env python3

from django.test import TestCase
from django.core.urlresolvers import resolve
from django.http import HttpRequest

from selenium import webdriver

from lists.views import home_page

# Create your tests here.
class HomePageTest(TestCase):
    def setUp(self):
        print(webdriver.__file__)
        self.browser = webdriver.Firefox()
        #self.browser.implicitly(3)
        
    def tearDown(self):
        self.browser.quit()
    
    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)
        
    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        self.assertTrue(response.content.startswith(b'<html>'))
        self.assertIn(b'<title>To-Do lists</title', response.content)
        self.assertTrue(response.content.endswith(b'</html>'))
        
    def test_can_start_a_list_and_retrive_it_later(self):
        #Idis heard there is a super cool online TO-DO app
        #She goes to check the app's page
        self.browser.get('http://127.0.0.1:8000')

        #She noticed that both title and header of the page contain the word "TO-DO" 
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')

        #The app invite her to enter a to-do item

        #She enters "Buy peacock feathers" into the text area
        #Her habbit is to use make fly

        #After hitting ENTER, the page refreshed
        #The To-Do list shows "1: Buy peacock freathers"

        #The page shows another text area to enter other To-Do items
        #She enters "Use peacock feathers to make a fly" 

        #The page refreshed again,there are two items in her list

        #Idis wants to know wether this website could remember her list

        #She saw the website generate a unique URL for her
        #And there are some text to explain this feature

        #She checked that URL,found that her list is still there

        #She is satisfied,and gone to sleep