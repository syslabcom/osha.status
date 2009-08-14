from osha.theme.tests.test_rss import TestOshaRSS
import unittest
from slc.alertservice.tests import BasicTests as AlertServiceTests

def test_suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(AlertServiceTests))
    suite.addTest(unittest.makeSuite(TestOshaRSS))
    return suite
