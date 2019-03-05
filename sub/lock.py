from .common import *

class Lock(Handler):
    def _lock(self):
        self.argParse(['-n' , '-m', '-i', '-c'])
        if not (self.instances or self.nodes or self.modules):
            raise ArgError("ERROR: action '{}' requires at least one of option '-i', '-m' or '-n', '-c'.".format(self.action))

        if self.nodes:
            for name in self.nodes:
                post_data = {'object':'node', 'name':name}
                self.call(post_data)
        if self.clusters:
            for name in self.clusters:
                post_data = {'object':'cluster', 'name':name}
                self.call(post_data)
        if self.instances:
            for name in self.instances:
                post_data = {'object':'instance', 'name':name}
                self.call(post_data)
        if self.modules:
            for name in self.modules:
                post_data = {'object':'module', 'name':name}
                self.call(post_data)

    def lock(self):
        self._lock()

    def unlock(self):
        self._lock()
