import os
import HTMLTestRunner
import unittest
from newsGoogle import selectOptionTest

#load test
Test1 = unittest.TestLoader().loadTestsFromTestCase(selectOptionTest)

# Create Test Suite
TestSuite1=unittest.TestSuite([Test1])


# dir 
dir=os.getcwd()
print "dir", dir
file1=dir + "/report.html"
print 'file1',file1
fileHandle=open(file1,"w+")
fileHandle.write("welcome")
i=fileHandle.closed
print i


#HTMLRunner 
runner=HTMLTestRunner.HTMLTestRunner(stream=fileHandle,title='Test Report',description='Smoke Tests')
runner.run(TestSuite1)
