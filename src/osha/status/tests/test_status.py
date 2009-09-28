from osha.status.views import Status
from osha.status.interfaces import IStatus
from zope.interface import implements
from zope.app.component.interfaces import ISite
from zope.annotation.interfaces import IAttributeAnnotatable
import unittest

from osha.status.tests.base import TestCase

class MockContext(object):
    implements(ISite, IAttributeAnnotatable)
    def __init__(self):
        self.properties = {}
    def getProperty(self, property_name):
        return self.properties[property_name]


class AllTests(TestCase):
    def test_goodStatus(self):
        context = MockContext()
        view = Status(context, None)
        IStatus(context).status = "True"
        self.assertTrue(view.isStatusGood())

    def test_badStatus(self):
        context = MockContext()
        view = Status(context, None)
        IStatus(context).status = "False"
        self.assertFalse(view.isStatusGood())

def test_suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(AllTests))
    return suite

if __name__ == '__main__':
    unittest.main(defaultTest='test_suite')