from zope.component import adapts #@UnresolvedImport
from zope.interface import implements
from zope.publisher.interfaces.browser import IBrowserRequest, IBrowserView
from zope.app.component.interfaces import ISite

class Status(object):
    implements(IBrowserView)
    adapts(ISite, IBrowserRequest)

    def __init__(self, context, request):
        self.context = context
        self.request = request
        
    def __call__(self):
        return "All good!"