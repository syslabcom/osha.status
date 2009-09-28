from persistent.dict import PersistentDict

from zope.annotation.interfaces import IAnnotations
from zope.app.component.interfaces import ISite
from zope.component import adapts #@UnresolvedImport
from zope.interface import implements

from osha.status.interfaces import IStatus

KEY = 'osha.status'

class Status(object):
    implements(IStatus)
    adapts(ISite)
    
    def __init__(self, context):
        self.context = context
        annotations = IAnnotations(context)
        mapping = annotations.get(KEY)
        if mapping is None:
            mapping = annotations[KEY] = PersistentDict({'status' : 'Bad'})
        self.mapping = mapping
            
    def _setStatus(self, value):
        if value == 'True':
            self.mapping['status'] = 'Good'
        else:
            self.mapping['status'] = value
        
    def _getStatus(self):
        return self.mapping['status']
    
    status = property(_getStatus, _setStatus)
