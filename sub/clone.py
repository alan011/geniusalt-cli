from .common import *

class Clone(Handler):
    def clone(self):
        self.argParse(['-n', '--from-node' ])
        if not self.nodes:
            raise ArgError("ERROR: Clone command requires an node name, which can be specified with option '-n'")
        if not self.clone_target_node:
            raise ArgError("ERROR: Clone command requires an existing target node, which can be specified with option '--from-node'")

        for name in self.nodes:
            post_data = {'object':'node', 'name':name, '--from-node': self.clone_target_node}
            self.call(post_data)
