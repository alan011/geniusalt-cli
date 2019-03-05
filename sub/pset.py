from .common import *

class Pset(Handler):
    def pset(self):
        self.argParse(['-i' , '-p', '-e', '-n'])
        if not self.instances or not self.pillars:
            raise ArgError("ERROR: action 'pset' can only be used to set pillars of instance objects. Option '-i' and '-p' must be specified, option '-e' can be optionally used to set environment related pillars.")
        if self.environment and self.nodes:
            raise ArgError("ERROR: action 'pset' cannot be used with '-n' and '-e' together.")

        for name in self.instances:
            post_data = {'object':'instance', 'name':name, 'pillar':self.pillars}
            if self.nodes:
                post_data['nodes'] = self.nodes
            elif self.environment:
                post_data['environment'] = self.environment
            self.call(post_data)
