import unittest
from   xmlrunner   import xmlrunner
from   newsGoogle  import selectOptionTest

#get all tests from SearchProductTest and HomePageTest class
Test1=unittest.TestLoader().loadTestsFromTestCase(selectOptionTest)

#create a test suite combining search_test and home_page_test
Test2=unittest.TestSuite([Test1])

#run the suite
xmlrunner.XMLTestRunner(verbosity=2,output='test-reports').run(Test2)
