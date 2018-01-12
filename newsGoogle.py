# !usr/bin/python 
from   selenium                                     import webdriver
from   selenium.webdriver.support.wait              import WebDriverWait
from   selenium.webdriver.support.select            import Select
from   selenium.webdriver.support.ui                import Select
from   selenium.webdriver.common.by                 import By
from   selenium.webdriver.common.action_chains      import ActionChains
from   selenium.webdriver.support                   import expected_conditions as EC 
import unittest
import time
 

class selectOptionTest(unittest.TestCase):
    '''
    selectOptionTest class will check all the news stories frame have images; if in case the news stories have no images than the test will inform 
    the non-availaibility of images in the frame of news stories.
    '''
    
    @classmethod
    def setUpClass(cls):
        global driver
        cls.driver  = webdriver.Firefox()
        driver      = cls.driver
        page        = 'https://news.google.com/news/headlines?hl=en-GB&ned=uk' 
        driver.get(page)
        driver.maximize_window()
        

    def test_1selectOptions(self):
        self.assertEqual(driver.title,u'Google News') 
        print "i am in "
        frameList1      = driver.find_elements_by_xpath("//c-wiz[@class='lPV2Xe k3Pzib'][@jsmodel='hc6Ubd']")
        imageList2      = driver.find_elements_by_xpath("//img[@class='lmFAjc']") 
        countframeList1 = len(frameList1)
        countimageList2 = len(imageList2)
        try:
            self.assertEqual(countframeList1,countimageList2)
        except:
            print "There exist a frame without image or it contains video image in it." 


        
        #Check for all the image are displayed and images are part of the news stories.
        #all the web elements id will be part of CSV file in automation frame work
        for i in range (1,countimageList2+1):
            conv=str(i)
            imageWebElement='"'+'(//img[@class=\'lmFAjc\'])'+'['+conv+']'+'"'
            u='driver.find_element_by_xpath'+'('+imageWebElement+')'
            eval(u).is_displayed()
            
              
    def test_2checkUk(self):
        print "in checkUk"  
        ukElement     = "//span[@class='cc5fC'][contains(text(),'U.K.')]"
        ukWebElement  = WebDriverWait(driver,10).until(lambda driver: driver.find_element_by_xpath(ukElement)) 
        ukWebElement.is_displayed()

    @classmethod
    def tearDownClass(cls):
        driver.close()   
       
if __name__=='__main__':
    unittest.main()
