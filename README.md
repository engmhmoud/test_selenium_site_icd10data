# test_selenium_site_icd10data
# icd10data site test
# Task
Title: 
Python application for finding medical codes.

Task:
The application, on the page https://www.icd10data.com, should search for the disease by medical code.

Steps to reproduce:
  1. Go to the page https://www.icd10data.com using Selenium Webdriver.

  2. On the page, perform the following actions:

       a. Check the presence of the website logo and its name on the logo on the page.
            

       b. Check that there is a Codes button in the menu bar of the page.
     
       c. Check that when you click on the Codes button, a drop-down menu opens.
            

       d. Check that the disease search field by code is located at the top of the page.
           

       e. Enter the Coronavirus code in the search field and click the search button.
          

       f. Check that the search result we need is on the page that opens.
         

          

# solution on code  at test_all.py file named and ordered
to run you should have python ,pytest , selenium ,and pipenv
run > pytest . 
