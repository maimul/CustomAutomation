# serunaiAutomation.py
# Created by: Maimul Hoque
# Created on: 2023-04-19

import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import Select
import random
import datetime
from seleniumbase import BaseCase

class vhsmart(): # Class for VH Smart automation
    '''
    Class for VH Smart automation
    All the function for VH Smart automation will be here

    Common parameters:
        - message: This is the message that will be printed when the function is done running.
        - wait: This is the time to wait before all the actions are performed in that function. 
                Some are set to default to 1 second or 0.5 and at most 1.5 seconds.
                This is to ensure that the page is loaded before the actions are performed.
        - css_selector: This is the css_selector of the element that the function will be performed on.
                This is to ensure that the correct element is selected.
        - text: This is the text that will be input into the text field or selected from the dropdown menu.
                This is to ensure that the correct text is inputted or selected.
        - type: This is the type of the element that the function will be performed on.
                This is to ensure that the correct element is selected.
                The type can be:
                    - text
                    - select-one
                    - tel
                    - checkbox
                    - radio
                    - button
                    - submit
                    - reset
                    - file
                    - hidden
                    - image
                    - password
                    - email
                    - Etc. (https://www.w3schools.com/tags/att_input_type.asp)
        - url: This is the url of the website.
                This is to ensure that the correct website is used.
        - delete: If this is set to True, the function will return true if the item is deleted. Only used in check_title function.
        - xpath: If this is set to True, the function will use xpath instead of css_selector.
        - title: This is the title of the page. Only used in check_title function.


    Common functions:
        - login: This function will login into VH Smart.
        - goto_url: This function will go to a specific url within VH Smart.
        - click_btn: This function will click a button.
        - input_txt: This function will input text into a text field.
        - select_dropdown: This function will select an option from a dropdown menu.
        - input_txt: This function will input text into a text field.
        - checkall_dropdown: This function will select all the options from a dropdown menu.
        - select_dropdown_RandIter: This function will select a random option from a dropdown menu.
        - check_title: This function will check the title of the page to ensure that the correct page is loaded.
                       This function can be also used to check if an item is deleted or not.
        - check_element: This function will check if an element is present.
        - check_type: This function will check the type of an element.
        - is_enabled: This function will check if an element is enabled.
        - is_disabled: This function will check if an element is disabled.
        - accept_alert: This function will accept an alert.
        - scroll_end: This function will scroll to the element and bring it to view.
    '''

    def __init__(self, driver): # Constructor  # driver_loc by default is /Driver/chromedriver
        '''
        Constructor
        This function will always be called when an object is created.
        - The drivers are set up here.

        '''
        self.driver = driver

        # Create alert object for handling alerts
        global alert 
        alert = Alert(self.driver)  # Create alert object for handling alerts
        
        # generate a random string for naming purpose
        # Example create an email with random string
        self.datenow_str = datetime.datetime.now().strftime("%Y%m%d") # Look into datetime library for more info on strftime




    def login(self, message = 'login'): 
        '''
        Function to login into VH Smart
        - The login credentials are set here.
        - The website is set to default to https://vhsmarttest.azurewebsites.net/
        - The login credentials are set to default to
                    "admin@qsrbrands.com.my" 
                    "p@ssw0rd1234"
        - The login credentials can be changed by changing the username and password variables.
        - The website can be changed by changing the url variable.         
        - The message is set to default to 'login'
        '''
        url = 'https://vhsmarttest.azurewebsites.net/'
        self.driver.get(url) # Go to VH Smart website login
        try:
            # Login credentials
            username = "admin@qsrbrands.com.my" 
            password = "p@ssw0rd1234"

            # 1. Login into VH SMART
            self.driver.find_element('xpath', '//*[@id="Input_Email"]').send_keys(username) 
            self.driver.find_element('xpath', '//*[@id="Input_Password"]').send_keys(password) 
            self.driver.find_element('xpath', '//*[@id="buttonLogin"]').click()
            print('TEST PASSED! ✅',message) 
        
        except Exception as e: 
            assert False, print('TEST FAILED! ❌',message,e)
    

    def goto_url(self, url='https://vhsmarttest.azurewebsites.net/', message = 'go to url'): # Function to go to url
        '''
        Function to go to specific url within VH Smart
        - The url is set to default to https://vhsmarttest.azurewebsites.net/
        - The url can be changed by changing the url variable.
        - The message is set to default to 'go to url'
        '''
        
        try:
            self.driver.get(url)
            print('TEST PASSED! ✅',message) 

        except Exception as e:
            assert False, print('TEST FAILED! ❌',message,e)

    def click_btn(self, css_selector, message = 'click button', wait = 1, xpath=False): # Function to click button

        element = "css selector" # Default element is css selector
        
        if xpath == True: # If xpath is set to True, change element to xpath
            element = 'xpath'

        try:
            time.sleep(wait)
            self.driver.find_element(element, css_selector).click() # Click button
            print('TEST PASSED! ✅',message) 

        except Exception as e:
            assert False, ('TEST FAILED! ❌',message,e)

    def input_txt(self, css_selector, text, message = 'input textfield', wait = 0.5, xpath=False): # Function to input text into text field

        element = "css selector" # Default element is css selector
        
        if xpath == True: # If xpath is set to True, change element to xpath
            element = 'xpath'

        try:
            time.sleep(wait)
            textField = self.driver.find_element(element, css_selector) # Get the input field
            textField.clear() # Clear the input field
            textField.send_keys(text) # Enter text into input field
            print('TEST PASSED! ✅',message)

        except Exception as e:
            assert False, print('TEST FAILED! ❌',message,e)


############################################## Dropdown Menu Functions ##############################################
    def select_dropdown(self, css_selector, text, message = 'select dropdown menu', wait = 0.5, xpath=False): # Function to select an option from dropdown
        
        element = "css selector" # Default element is css selector
        
        if xpath == True: # If xpath is set to True, change element to xpath
            element = 'xpath'        
        
        try:
            time.sleep(wait)
            select = Select(self.driver.find_element(element, css_selector))
            select.select_by_visible_text(text)
            print('TEST PASSED! ✅',message)

        except Exception as e:
            assert False, print('TEST FAILED! ❌',message,e)

    def checkall_dropdown(self, css_selector, message = 'Go through all option in dropdown', wait = 0.5, xpath=False): # Function to go through all option in dropdown and select them
        
        element = "css selector" # Default element is css selector
        
        if xpath == True: # If xpath is set to True, change element to xpath
            element = 'xpath' 

        try:
            time.sleep(wait)
            options = self.driver.find_elements(element, css_selector+'/option') # Get the number of options in the dropdown
            options = range(len(options)-1) # Subtract 1 as the 1st option is --PLEASE SELECT--
            for i in options: # Go through all the options
                option = self.driver.find_element(element, css_selector+' > option:nth-child('+str(i+2)+')').get_attribute('textContent') # Get all the options
                # print(option) # Uncomment to see all the options printed
                self.driver.find_element(element, css_selector+' > option:nth-child('+str(i+2)+')').click() # Choose option one by one
            print('TEST PASSED! ✅',message)

        
        except Exception as e:
            assert False, print('TEST FAILED! ❌',message,e)

    def select_dropdown_RandIter(self, css_selector, message = 'select dropdown menu', wait = 0.5, xpath=False): # Function to select a random option from dropdown
        
        element = "css selector" # Default element is css selector
        
        if xpath == True: # If xpath is set to True, change element to xpath
            element = 'xpath' 
        
        try:
            time.sleep(wait)
            select = Select(self.driver.find_element(element, css_selector))
            select.select_by_index(random.randint(1, len(select.options)-1))
            print('TEST PASSED! ✅',message)

        except Exception as e:
            assert False, print('TEST FAILED! ❌',message,e)
############################################## End Dropdown Menu Functions ##############################################


    def check_title(self, css_selector, title, message = 'verify title', wait = 1, delete = False, type = 'title', xpath = False): # Function to verify title
        
        element = "css selector" # Default element is css selector
        
        if xpath == True: # If xpath is set to True, change element to xpath
            element = 'xpath' 

        try:
            time.sleep(wait)
            # print(self.driver.find_element(element, css_selector).text)

            if xpath == False:
                actual_title = self.driver.find_element(element, css_selector) # Store the css_selector of the title
            else:
                actual_title = self.driver.find_element(element, css_selector) # Store the xpath of the title


            if type == 'text field':
                actual_title = self.driver.execute_script('return arguments[0].value', actual_title) # Get the value of the text field
            else:
                actual_title = actual_title.text # Get the text of the title

            if delete == True:
                assert actual_title != title # Check if title is not the same
            else:
                assert actual_title == title # Check if title is the same
            print('TEST PASSED! ✅',message, '| Expected:',title,'| Actual:',actual_title)

        except Exception as e:
            assert False, print('TEST FAILED! ❌',message,e,'| Expected:',title,'| Actual:',actual_title)

    def check_element(self, css_selector, message = 'verify element', wait = 0, xpath=False): # Function to verify element
        
        element = "css selector" # Default element is css selector
        
        if xpath == True: # If xpath is set to True, change element to xpath
            element = 'xpath' 
        
        try:
            time.sleep(wait)
            assert self.driver.find_element(element, css_selector).is_displayed() == True
            print('TEST PASSED! ✅',message)
        except Exception as e:
            assert False, print('TEST FAILED! ❌',message,e)

    def check_type(self, css_selector, type, message = '(verify type)', wait=0, xpath=False): # Function to verify type
        
        element = "css selector" # Default element is css selector
        
        if xpath == True: # If xpath is set to True, change element to xpath
            element = 'xpath' 
        
        try:
            time.sleep(wait)
            # print(self.driver.find_element(element, css_selector).get_attribute('type'))
            actual_type = self.driver.find_element(element, css_selector).get_attribute('type')
            assert actual_type == type
            
            print('TEST PASSED! ✅','| Expected:',type,"| Actual:",actual_type,'|| for', message)

        except Exception as e:
            assert False, print('TEST FAILED! ❌',e,'| Expected:',type,"| Actual:",actual_type,'|| for', message)

    def is_enabled(self, css_selector, message = 'input is enabled', wait = 0.5, xpath=False): # Function to check if input is enabled
        
        element = "css selector" # Default element is css selector
        
        if xpath == True: # If xpath is set to True, change element to xpath
            element = 'xpath' 
        
        try:
            time.sleep(wait)
            assert self.driver.find_element(element, css_selector).is_enabled() == True    
            print('TEST PASSED! ✅',message)
        except Exception as e:
            assert False, print('TEST FAILED! ❌',message,e)

    def is_disabled(self, css_selector, message = 'input is disabled', wait = 0.5, xpath=False): # Function to check if input is disabled
        
        element = "css selector" # Default element is css selector
        
        if xpath == True: # If xpath is set to True, change element to xpath
            element = 'xpath' 
        
        try:
            time.sleep(wait)
            assert self.driver.find_element(element, css_selector).is_enabled() == False    
            print('TEST PASSED! ✅',message)
        except Exception as e:
            assert False, print('TEST FAILED! ❌',message,e)


    def accept_alert(self, message = 'accept alert', wait = 0.5): # Function to accept alert
        try:
            time.sleep(wait)
            alert.accept()
            print('TEST PASSED! ✅',message)
        except Exception as e:
            assert False, print('TEST FAILED! ❌',message,e)

    def scroll_end(self, css_selector, message = 'scroll to end', wait = 0.5, xpath=False): # Function to scroll to end of page
        
        element = "css selector" # Default element is css selector
        
        if xpath == True: # If xpath is set to True, change element to xpath
            element = 'xpath' 

        try:
            time.sleep(wait)
            element = self.driver.find_element(element, css_selector)
            self.driver.execute_script("arguments[0].scrollIntoView();", element)
            print('TEST PASSED! ✅',message)
        except Exception as e:
            assert False, print('TEST FAILED! ❌',message,e)
    
    # def get_option(self, css_selector, message = 'get option'):
    #     try:
    #         self.driver.find_elements(element, css_selector+'/option')
    #         print('TEST PASSED! ✅',message)
    #     except Exception as e:
    #         assert False, print('TEST FAILED! ❌',message,e)
    #         //*[@id="CompanyDataTable_wrapper"]/div[2]/div
    #         //*[@id="CompanyDataTable"]/tbody/tr[1]/td[1]
    #         //*[@id="CompanyDataTable"]/tbody/tr[2]/td[1]

    #         //*[@id="CompanyDataTable"]/tbody/tr[1]/td[3]
