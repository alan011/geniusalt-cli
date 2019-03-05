from .common import *

class Cset(Handler):
    def cset(self):
        self.argParse(['-c' , '-i', '-n'])
        if not self.clusters:
            raise ArgError("ERROR: Option '-c' must be specified with action 'cset'.")
        if len(self.clusters) != 1:
            raise ArgError("ERROR: multi-clusters are not allowed with action 'cset'.")
        if self.instances and len(self.instances) > 1:
            raise ArgError("ERROR: multi-instances are not allowed to bind to one cluster.")

        for name in self.clusters:
            post_data = {'object':'cluster', 'name':name}
            if self.nodes:
                post_data['nodes'] = self.nodes
            if self.instances:
                post_data['instances'] = self.instances
            self.call(post_data)
