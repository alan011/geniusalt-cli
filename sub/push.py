from .common import *

class Push(Handler):
    def push(self):
        self.argParse(['-n', '-c', '-m', '-i', '--all-instances', '--only-module'])
        if not (self.nodes or self.clusters):
            raise ArgError("ERROR: action 'push' requires node or cluster objects specified.")

        if self.clusters:
            if self.nodes or self.modules or self.instances:
                raise ArgError("ERROR: clusters cannot be pushed together with other objects.")
            post_data = {'object':'push', 'clusters': self.clusters}
        else:
            post_data = {'object':'push',
                         'nodes':self.nodes,
                         '--only-module':self.push_only_module,
                         '--all-instances':self.push_all_instances}
            if self.modules:
                post_data['bind_modules'] = self.modules
            if self.instances:
                post_data['bind_instances'] = self.instances
        self.call(post_data)
