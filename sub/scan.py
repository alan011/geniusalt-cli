from .common import *

class Scan(Handler):
    def scan(self):
        self.argParse(['-n', '-m'])
        if not ('-n' in self.args or '-m' in self.args):
            raise ArgError("ERROR: Action 'scan' requires at least one option in '-n' or '-m'.")

        if '-n' in self.args:
            post_data = {'object': 'node'}
            self.call(post_data)

        if '-m' in self.args:
            post_data = {'object': 'module'}
            self.call(post_data)
