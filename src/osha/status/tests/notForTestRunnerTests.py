from zc.testbrowser.browser import Browser
import unittest

class TestCertification(unittest.TestCase):
    
    def test_form(self):
        url = 'http://osha.europa.eu/en/campaigns/hw2008/sign/index_html'
        browser = Browser()
        browser.open(url)
        self.assertTrue('Online Application Form' in browser.contents)
        
    def test_formSubmission(self):
        url = 'http://osha.europa.eu/scripts/signcharter?txtLanguage=en&txtOrganisation=test&txtAddress=test&txtPostalcode=test&txtCity=test&selCountry=UK&txtFirstname=test&txtLastname=test&txtFunction=&txtEmail=test@syslab.com&txtTelephone=test&txtOther=&Submit=SUBMIT'
        browser = Browser()
        browser.open(url)
        self.assertTrue('Healthy Workplaces - Good for you. Good for business.' in browser.contents)

        
def test_suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCertification))
    return suite