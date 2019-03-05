from .usage   import Usage
from .scan    import Scan
from .add     import Add
from .delete  import Delete
from .show    import Show
from .pset    import Pset
from .pdel    import Pdel
from .eset    import Eset
from .bind    import Bind
from .joinc   import JoinC
from .lock    import Lock
from .include import Include
from .push    import Push
from .cset    import Cset
from .clone   import Clone
from .common  import *

class CommandDispatcher(Usage, Scan, Add, Show, Delete, Pset, Eset, Pdel, Lock, Bind, Include, Push, JoinC, Cset, Clone):
    action_supported = {'scan', 'add', 'del','delete', 'show', 'pset','eset', 'cset', 'pdel', 'lock', 'unlock','bind', 'unbind', 'include', 'exclude', 'joinc', 'unjc', 'push', 'showb', 'clone'}

    def __init__(self, action, args):
        self.action = action
        if self.action == 'del':
            self.action = 'delete'
        self.args = args
        self.post_data = {'auth_token':self.auth_token,'action':self.action}

    def run(self):
        try:
            getattr(self, self.action)()
        except ArgError as e:
            raise SystemExit(str(e))
