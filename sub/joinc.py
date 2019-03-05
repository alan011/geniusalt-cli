from .common import *

class JoinC(Handler):
    def _join(self):
        self.argParse(['-n', '-c'])
        if not self.nodes or not self.clusters:
            raise ArgError("ERROR: action '{}' is used to {} node objects to cluster objects. Option '-n' and '-c' must be specified. ".format(self.action, self.action))

        post_data = {'object':'relation', 'nodes': self.nodes, 'clusters': self.clusters}
        self.call(post_data)
    def joinc(self):
        self._join()
    def unjc(self):
        self._join()
