from Products.PloneTestCase import PloneTestCase as ptc
from Products.PloneTestCase import layer

SiteLayer = layer.PloneSite

class OshaStatusLayer(SiteLayer):
    @classmethod
    def setUp(cls):
        ptc.setupPloneSite(products=[])
        SiteLayer.setUp()


class TestCase(ptc.PloneTestCase):
    layer = OshaStatusLayer

