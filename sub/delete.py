from .common import *

class Delete(Handler):
    def delete(self):
        self.argParse(['-n', '-m', '-i', '-c'])
        if self.nodes:
            for name in self.nodes:
                post_data = {'object':'node', 'name':name}
                self.call(post_data)

        if self.clusters:
            for name in self.clusters:
                post_data = {'object':'cluster', 'name':name}
                self.call(post_data)

        if self.modules:
            for name in self.modules:
                answer = input("Warning: all instances belong to module '{}' will be deleted cascadedly.\nDo you really want to do that? [Y/N]".format(name))
                if answer == 'Y':
                    post_data = {'object':'module', 'name':name}
                    self.call(post_data)
                else:
                    print("OK, To delete module '{}' aborted.".format(name))

        if self.instances:
            for name in self.instances:
                post_data = {'object':'instance', 'name':name}
                self.call(post_data)
