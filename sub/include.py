from .common import *

class Include(Handler):
    def _include(self):
        self.argParse(['-i' , '-ii'])
        if not self.instances or not self.included_instances:
            raise ArgError("ERROR: action '{}' is used for an instances to {} other instances. Option '-i' and '-ii' must be specified." .format(self.action, self.action))
        post_data = {'object':'relation', 'instances': self.instances, 'included_instances':self.included_instances}
        self.call(post_data)
    def include(self):
        self._include()
    def exclude(self):
        self._include()
