from Products.Five import zcml
from Products.Five import fiveconfigure
from Testing import ZopeTestCase as ztc

from Products.PloneTestCase import PloneTestCase as ptc
from Products.PloneTestCase import layer

SiteLayer = layer.PloneSite

class OshaStatusLayer(SiteLayer):
    @classmethod
    def setUp(cls):
        import osha.status
        zcml.load_config('configure.zcml', osha.status)
        import osha.theme
        zcml.load_config('configure.zcml', osha.theme)
        import textindexng
        zcml.load_config('configure.zcml', textindexng)
        import slc.clicksearch
        zcml.load_config('configure.zcml', slc.clicksearch)
        import slc.xliff
        zcml.load_config('configure.zcml', slc.xliff)
        fiveconfigure.debug_mode = False
        ztc.installPackage('osha.status', quiet=True)
        ptc.setupPloneSite(products=[], extension_profiles=['osha.theme:default'])
        SiteLayer.setUp()


class TestCase(ptc.PloneTestCase):
    layer = OshaStatusLayer

