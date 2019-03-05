from .common import *

class Bind(Handler):
    def _bind(self):
        self.argParse(['-n', '-i', '-m', '-c'])
        if not (self.nodes or self.clusters) or not (self.instances or self.modules):
            raise ArgError("ERROR: action '{}' is used to {} instances or modules to node or cluster objects. Option '-n' or '-c' must be specified,  '-i' or '-m' must also be specified.".format(self.action, self.action))
        if self.clusters:
            if not self.instances:
                raise ArgError("ERROR: Instance must be specified when binding clusters.")
            if self.modules:
                raise ArgError("ERROR: Modules cannot be bind with clusters.")
            post_data = {'object':'relation', 'clusters': self.clusters, 'bind_instances': self.instances}
        else:
            post_data = {'object':'relation', 'nodes': self.nodes}
            if self.modules:
                post_data['bind_modules'] = self.modules
            if self.instances:
                post_data['bind_instances'] = self.instances
        self.call(post_data)
    def bind(self):
        self._bind()
    def unbind(self):
        self._bind()
