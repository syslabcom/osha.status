from zope.interface.interface import Interface
from zope.schema import TextLine
class IStatus(Interface):
    """
    Contains the status of the Site
    """
    status = TextLine(
                     title=u"Status",
                     required = True)