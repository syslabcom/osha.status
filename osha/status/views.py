from zope.component import adapts #@UnresolvedImport
from zope.interface import implements
from zope.publisher.interfaces.browser import IBrowserRequest, IBrowserView
from zope.app.component.interfaces import ISite
from osha.status.interfaces import IStatus

class Status(object):
    implements(IBrowserView)
    adapts(ISite, IBrowserRequest)

    def __init__(self, context, request):
        self.context = context
        self.request = request
        
    def __call__(self, status = 'invalid'):
        if status != 'invalid':
            IStatus(self.context).status = status
        return self.index()
        
    def isStatusGood(self):
        return IStatus(self.context).status == 'Good'