'''PYTEST : Pytest is a unit testing framework which can test a small unit of any program

Advantages : We can group the testcases, can generate the reports, can use dependencies

Firstly we have to install the pytest
Go to cmd prompt --> pip install pytest
To check whether pytest is installed properly or not, check the version --> pytest --version'''

'''
🐍 Pytest (Python Testing Framework)

Pytest is a Python testing framework used for:
Unit testing
Functional testing
API testing
Automation framework integration (like Selenium + Pytest).

🔹 Why Pytest is Popular?
✔ Very simple syntax (no need to create classes mandatory)
✔ supports assertions
✔ Supports fixtures
✔ supports Parametrization
✔ Plugins support (pytest-html, pytest-xdist, etc.)
✔ Easy CI/CD integration (Jenkins, GitHub Actions)
'''


# def spam():
#     print('in spam')
#
# def display():
#     print('in display')
#
# spam()
# display()

''' When we define normal functions, we have to call the functions expliciltly,
To execute the functions without calling, we use pytest'''

# ---------------------
'''
Pre Conditions to create the files
1. filename should always start with test_ or end with _test

2. function names should always start with test_funcname()

3. Classnames should always start with TestClassname

This is because, pytest automatically recognizes the file/func/classes starting with test_ 
or ending with _test

-v --> verbocity . This gives the detailed explanation of the testcase
-s --> scripting. This will print all the print statements
'''

# -----------------------

# def test_spam():
#     print('in spam')
#
# def test_display():
#     print('in display')                 #pytest test_py.py -vs------enter in the terminal

# ## collected 2 items
#
# #---------------------------------------------------------------
# def test_spam():
#     print('in spam')
#
# def display():
#     print('in display')               #pytest test_py.py ------enter in the terminal

'''collected 1 item. Only test_spam() will be executed. display() will not execute because
# ## display func is not starting with test_ or ending with _test'''
#
#
# #-------------------------------------------------------------
# class Sample:
#
#     def test_spam(self):
#         print('in spam')
#
#     def test_display(self):
#         print('in display')

'''collected 0 items. Because classname not starting with Test'''
#
# #-------------------------------------------------
# class Test_Sample:
#
#     def test_spam(self):
#         print('in spam')
#
#     def test_display(self):
#         print('in display')
# #----------------------------------------------------
# import time
# from selenium import webdriver
# driver = webdriver.Chrome()
#
# driver.get('https://demowebshop.tricentis.com/')
# driver.maximize_window()
#
# def test_click_register():
#     driver.find_element('xpath', '//a[text()="Register"]').click()
#     time.sleep(3)
#
# def test_click_login():
#     driver.find_element('xpath', '//a[text()="Log in"]').click()
#     time.sleep(3)

# #-----------------------------------------------------------
# import time
# from selenium import webdriver
# driver = webdriver.Chrome()
#
# driver.get('https://demowebshop.tricentis.com/')
# driver.maximize_window()
#
# def test_click_register():
#     driver.find_element('xpath', '//a[text()="Register"]').click()
#     time.sleep(2)
#
# def click_login():
#     driver.find_element('xpath', '//a[text()="Log in"]').click()
#     time.sleep(3)
#
# def test_click_shopping_cart():
#     driver.find_element('xpath', '//span[text()="Shopping cart"]').click()

## If any of the function fails, it will not affect the execution of other functions

# #-----------------------------------------------------------
# class TestCalculator:
#
#     a = 10
#     b = 20
#
#     def test_add(self):
#         assert self.a + self.b==30         #'adddition not equal to 30'
#
#     def test_sub(self):
#         assert self.a - self.b==100        #'subtraction not equal to 100'
#
#     def test_mul(self):
#         assert self.a * self.b==200          #'mul not equal to 10'
#
#     def test_div(self):
#         assert self.a/self.b==0.5           #'div not equal to 0.5'

'''To validate we use assert keyword. If the condition fails, it will always give assertion error'''

#--------------------------------------------------------------
# '''fixtures'''
#
# import pytest
#
# @pytest.fixture()
# def greet():
#     print('***********hello**************')
#
# def test_spam(greet):
#     print('In spam executing')
#
# def test_display(greet):
#     print('In display executing')

'''If we want to perform any operation before the execution of each testcase, we make it as setup.
## To define a fixture, first import pytest and then decorate with @pytest.fixture()'''

# #----------------------------

# import pytest
#
# @pytest.fixture(autouse=True)
# def greet():
#     print('***********hello**************')
#
# def test_spam():
#     print('In spam executing')
#
# def test_display():
#     print('In display executing')

'''Instead of passing the fixture func as a parameter to each test func, we can give autouse=True
# while defining the fixture'''

#--------------------------------------------------------
# import pytest
#
# @pytest.fixture()
# def greet():
#     print('********hello*********')
#
# def test_spam(greet):
#     print('In spam executing')
#
# class TestSample:
#
#     def test_display(self, greet):
#         print('In display executing')
#
# #-------------------------------------------------
# import pytest
#
# @pytest.fixture(autouse=True)
# def display():
#     print('hello')
#
# class TestSample:
#     def test_example(self):
#         print('Example executing')
#
#     def test_sample(self):
#         print('sample executing')
#
# def test_data():
#     print('data executing')

# autouse=True, fixture will be applied to all the test functions and the class attributes

#---------------------------------------------
# import pytest
#
# @pytest.fixture(scope='class', autouse=True)
# def display():
#     print('hello')
#
# class TestSample:
#     def test_example(self):
#         print('Example executing')
#
#     def test_sample(self):
#         print('sample executing')
#
# def test_data():
#     print('data executing')

# scope='class'. Fixture will be applied only once for the entire class

# # ----------------------------------------------
# import pytest
#
# @pytest.fixture(scope='function', autouse=True)
# def greet():
#     print('***********hello**************')
#
# def test_spam():
#     print('In spam executing')
#
# def test_display():
#     print('In display executing')           # Applies for all the functions
#------------------------------------------------

# import pytest
#
# @pytest.fixture(scope='module',autouse=True)
# def greet():
#     print('***********hello**************')
#
# def test_spam():
#     print('In spam executing')                      # Apply for 1st function
#
# def test_display():
#     print('In display executing')
#
# class TestSample:
#     def test_example(self):
#         print('Example executing')

# scope='module'. Fixture will be applied only once for the entire module


#----------------------------------------
# import pytest
#
# @pytest.fixture(autouse=True)
# def greet():
#     print('***********hello**************')
#     yield
#     print('********** bye ************')
#
# def test_spam():
#     print('In spam executing')
#
# def test_display():
#     print('In display executing')

#-------------------------------------------
'''The operations before the yield will act as a setup and the operations after the yield will
act as teardown'''
#----------------------------------------------------------------
# #
# import pytest
# import time
# from selenium import webdriver
# driver = webdriver.Chrome()
#
# @pytest.fixture()
# def launch_browser():
#     driver.get('https://demowebshop.tricentis.com/')
#     driver.maximize_window()
#     time.sleep(3)
#
# def test_click_register(launch_browser):
#     driver.find_element('xpath', '//a[text()="Register"]').click()
#     time.sleep(3)
#
# def test_click_login(launch_browser):
#     driver.find_element('xpath', '//a[text()="Log in"]').click()
#     time.sleep(3)


#--------------------------------
# import pytest
# import time
# from selenium import webdriver
# @pytest.fixture(autouse=True)
# def launch_browser():
#     driver = webdriver.Chrome()
#     driver.get('https://demowebshop.tricentis.com/')
#     driver.maximize_window()
#     time.sleep(3)
#     yield driver

# import time
# def test_click_register(launch_browser):
#     launch_browser.find_element('xpath', '//a[text()="Register"]').click()
#     time.sleep(3)
#
# def test_click_login(launch_browser):
#     launch_browser.find_element('xpath', '//a[text()="Log in"]').click()
#     time.sleep(3)


#-------------------------------------------------------
'''
batch execution ---> pytest -vs
This will execute all the files in the directory. We call this as batch execution
'''

#------------------------------------------------
'''## Using Conftest : Whatever the common operations should be performed,
## we define them under a file. The file name should always be conftest.py
## Whenever we are executing any test files, conftest is the file
## which will get executed first.

## conftest will be shared among all the files in the particular package'''

# -------------------------------------------------------------------------------

'''DEPENDENCIES'''

'''## To make one testcase dependent on other, we use dependencies
## first we have to install dependency
# if the dependent test case is failed, then the test case will be skipped

## pip install pytest-dependency'''

# def test_spam():
#     print('spam executing')
#
# def test_display():
#     print('display executing')
#
# ## fail testcase not afftecting the other testcases
# #----------------------------------------------
#
# import pytest
#
# @pytest.mark.dependency()
# def test_spam():
#     print('spam executing')
#     assert 1+2 == 4
#
# @pytest.mark.dependency(depends=["test_spam"])
# def test_display():
#     print('display executing')

# test_spam --> error
# test_display --> skipped

'''## In the above case, since we have an error in the independent testcase,
the dependent testcase will be skipped'''

# #-------------------------------------------------------------

# import pytest
#
# class TestDepend:
#
#     @pytest.mark.dependency()
#     def test_spam(self):
#         print('spam executing')
#         assert 1+2 == 3
#
#     @pytest.mark.dependency(depends=["TestDepend::test_spam"])
#     def test_display(self):
#         print('display executing')

# ------------------------------------------------

# import pytest
#
# class TestDepend:
#     @pytest.mark.dependency()
#     def test_spam(self):
#         print('spam executing')
#         assert 1+2 == 3
#
#     @pytest.mark.dependency(depends=["TestDepend::test_spam"])
#     def test_display(self):
#         print('display executing')
#
#     @pytest.mark.dependency()
#     def test_kgf(self):
#         print('display executing')
#
# class TestSample:
#
#     @pytest.mark.dependency(depends=["TestDepend::test_kgf"])
#     def test_qsp(self):
#         print('basavanagudi')


# -----------------------------------------------

# import time
# import pytest
# from selenium import webdriver
# driver = webdriver.Chrome()
#
# driver.get('https://demo.actitime.com/login.do')
# driver.maximize_window()
# time.sleep(4)
#
# @pytest.mark.dependency()       ## independent testcase
# def test_login():
#     driver.find_element('xpath', '//input[@name="username"]').send_keys('admin')
#     driver.find_element('xpath', '//input[@name="pwd"]').send_keys('managerrr')
#     driver.find_element('xpath', '//div[text()="Login "]').click()
#     time.sleep(3)
#
#
# @pytest.mark.dependency(depends=["test_login"])     ## dependent testcase.
# def test_logout():
#     driver.find_element('xpath', '//a[@id="logoutLink"]').click()
#
#
# #-------------------------------------------------------
# #
# import time
#
# import pytest
# from selenium import webdriver
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions
#
# driver = webdriver.Chrome()
#
# driver.get('https://demo.actitime.com/login.do')
# driver.maximize_window()
# time.sleep(4)
#
# wait_ = WebDriverWait(driver, 30)
#
# @pytest.mark.dependency()       ## independent testcase
# def test_login():
#     driver.find_element('xpath', '//input[@name="username"]').send_keys('admin')
#     driver.find_element('xpath', '//input[@name="pwd"]').send_keys('managerrr')
#     driver.find_element('xpath', '//div[text()="Login "]').click()
#     time.sleep(3)
#     if wait_.until(expected_conditions.presence_of_element_located('(//span[@class="errormsg"])[1]')):
#         raise Exception
#     else:
#         time.sleep(2)
#
# @pytest.mark.dependency(depends=["test_login"])     ## dependent testcase.
# def test_logout():
#     driver.find_element('xpath', '//a[@id="logoutLink"]').click()

# -------------------------------------------------------------------------------

''' 
MARKERS

1. skip
2. skipif
3. xfail
4. parameterize
'''

## skip : If we want to skip the execution of the testcase. This is unconditional skip
## Here we dont pass any condition to skip the testcase
## Syntax : @pytest.mark.skip('reason')

# import pytest
#
# def test_login():
#     print('login page executing')
#
# @pytest.mark.skip
# def test_reg():
#     print('registration page executing')
#
# def test_signup():
#     print('signup page executing')
#
# def test_logout():
#     print('logout page executing')

#----------------------------------------

# import pytest
#
# def test_login():
#     print('login page executing')
#
# @pytest.mark.skip('Not valid testcase')
# def test_reg():
#     print('registration page executing')
#
# def test_signup():
#     print('signup page executing')
#
# def test_logout():
#     print('logout page executing')

#-------------------------------------
# import pytest
# def test_login():
#     print('login page executing')
#
# @pytest.mark.skip('Not valid testcase')
# def test_reg():
#     print('registration page executing')
#
# @pytest.mark.smoke
# def test_signup():
#     print('signup page executing')
#
# @pytest.mark.smoke
# def test_logout():
#     print('logout page executing')              # pytest -m "smoke" test_practice.py -vs


## In the above case, only test_signup and test_logout will execute

#-----------------------------------------------------------
# import pytest
# def test_login():
#     print('login page executing')
#
# @pytest.mark.smoke
# @pytest.mark.skip('Not valid testcase')
# def test_reg():
#     print('registration page executing')
#
# @pytest.mark.smoke
# def test_signup():
#     print('signup page executing')
#
# @pytest.mark.smoke
# def test_logout():
#     print('logout page executing')

#------------------------------------------------------
## Skipping entire class

# import pytest
# @pytest.mark.skip
# class TestGmail:
#
#     def test_login(self):
#         print('login page executing')
#
#     def test_reg(self):
#         print('registration page executing')
#
#     def test_signup(self):
#         print('signup page executing')
#
#     def test_logout(self):
#         print('logout page executing')

#--------------------------------------------------
# import pytest
# class TestGmail:
#
#     @pytest.mark.skip
#     def test_login(self):
#         print('login page executing')
#
#     def test_reg(self):
#         print('registration page executing')
#
#     def test_signup(self):
#         print('signup page executing')
#
#     @pytest.mark.skip
#     def test_logout(self):
#         print('logout page executing')

#-----------------------------------------------------------------
####################################################################
## skipif : Conditional skip. Testcase will be skipped based on the conditions
## skipif takes two parameters, condition and reason. Both are mandatory parameters

# import pytest
# a = 10
#
# @pytest.mark.skipif(a==20, reason='numbers not matching')
# def test_login():
#     print('login page executing')
#
# def test_reg():
#     print('registration page executing')
#
# @pytest.mark.skipif(a==10, reason='numbers matching')
# def test_signup():
#     print('signup page executing')
#
# def test_logout():
#     print('logout page executing')

#-------------------------------------------------------------------
# import pytest
# from selenium import webdriver
# driver = webdriver.Chrome()
#
# url = 'amazon'
#
# @pytest.mark.skipif(url in 'https://amazon.com/', reason='Not valid')
# def test_login():
#     driver.get('https://amazon.com/')
#
#
# @pytest.mark.skipif(url in 'https://flipkart.com/', reason='Not valid')
# def test_login():
#     driver.get('https://flipkart.com/')

#------------------------------------------------------------------
## xfail

'''
mark test functions as expected to fail
You can use the xfail marker to indicate that you expect a test to fail:
Syntax: @pytest.mark.xfail([parameters])

1. condition parameter : If a test is only expected to fail under a certain condition, you can pass
that condition as the first parameter:
Eg:
@pytest.mark.xfail(sys.platform == "win32", reason="bug in a 3rd party library")
def test_function():

2. reason parameter: You can specify the motive of an expected failure with the reason parameter
Eg:
@pytest.mark.xfail(reason="known parser issue")
def test_function():

3. raises parameter: If you want to be more specific as to why the test is failing, you can specify
a single exception, or a tuple of exceptions, in the raises argument.
Eg:
@pytest.mark.xfail(raises=RuntimeError)
def test_function():'''

# import pytest
# @pytest.mark.xfail
# def test_login():
#     print('login page executing')
#
# def test_reg():
#     print('registration page executing')
#
# @pytest.mark.xfail(raises=RuntimeError)
# def test_signup():
#     print('signup page executing')
#
# @pytest.mark.xfail(reason='not required')
# def test_logout():
#     print('logout page executing')


#----------------------------------------------------------
## parameterize

# To run same TC for multiple times using different parameters

# import pytest
#
# a = 'adminn'
# @pytest.mark.parametrize("un", ["demologin", "actitime", "automation", a])
# def test_login(un):
#     print(un)                                   # pytest test_practice.py -vs


#-------------------------------
# import pytest
# @pytest.mark.parametrize(["un", "pwd"], [["admin", "manager"]])
# def test_login(un, pwd):
#     print(un)
#     print(pwd)

#------------------------------------------
# import pytest
# @pytest.mark.parametrize(["un", "pwd"], [["admin", "manager"], ['adminn', "managerrr"]])
# def test_login(un, pwd):
#     print(un)
#     print(pwd)

#--------------------------------------
# import pytest
# @pytest.mark.parametrize(["un1", "pwd"], [["admin", "manager"], ['adminn', "managerrr"]])
# def test_login(un, pwd):
#     print(un)
#     print(pwd)

## Error. Because un and un1 are different

#-----------------------------------
# import pytest
# @pytest.mark.parametrize(["un", "pwd"], [["admin", "manager", 'hai'], ['adminn', "managerrr"]])
# def test_login(un, pwd):
#     print(un)
#     print(pwd)

## Error. Signatures mismatching


#-----------------------------------
# import pytest
# @pytest.mark.parametrize(["un", "pwd"], (["admin", "manager"], ['adminn', "managerrr"]))
# def test_login(un, pwd):
#     print(un)
#     print(pwd)

# -------------------------------------
# import pytest
# @pytest.mark.parametrize(["un", "pwd"], [("admin", "manager"), ('adminn', "managerrr")])
# def test_login(un, pwd):
#     print(un)
#     print(pwd)


'''ORDERING'''


# import pytest
#
# @pytest.mark.run(order=3)
# def test_login1():
#     print('un1')
#
# @pytest.mark.run(order=4)
# def test_login2():
#     print('un2')
#
#
# @pytest.mark.run(order=1)
# def test_login3():
#     print('un3')
#
# @pytest.mark.run(order=2)
# def test_login4():
#     print('un4')


# --------------------------------------------------