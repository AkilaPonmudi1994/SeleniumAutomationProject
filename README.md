
This is a simple test automation project I created while learning Selenium with Python. It tests the admin panel of the OrangeHRM demo website.

## What This Project Does 

This script tests two main features of the OrangeHRM admin panel:
1. Searching for employees by their name
2. Searching for users by their username

## Prerequisites 

Before running this project, you need to have:
- Python installed on your computer
- Chrome browser installed
- Selenium package installed (you can install it using pip install selenium)

## How to Run the Tests

1. Open your terminal/command prompt
2. Navigate to the project folder
3. Run the script:
   
   python crm_test.py
   

## What the Script Does 

1. Opens Chrome browser
2. Goes to OrangeHRM demo website
3. Logs in as admin
4. Tests employee search
5. Tests username search
6. Closes the browser when done

## Test Results 

The script will print:
- What it's searching for
- When it finds something
- Whether the tests passed or failed
