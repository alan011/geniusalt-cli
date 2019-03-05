from .common import *

class Eset(Handler):
    def eset(self):
        self.argParse(['-n' , '-e'])
        if not self.nodes:
            raise ArgError("ERROR: Command 'eset' is used to set environment of nodes. Option '-n' must be specified. If not with '-e', nodes will be set to default environment ''.")

        for name in self.nodes:
            post_data = {'object':'node',
                         'name':name,
                         'environment':self.environment if self.environment else ''}
            self.call(post_data)
