from .common import *
from collections import OrderedDict
class Show(Handler):
    def _show_object(self, name_list, obj_type, post_data):
        post_data['object'] = obj_type
        if obj_type == 'module':
            post_data['--instance'] = self.show_instances

        if name_list:
            for name in name_list:
                post_data['name'] = name
                # print(post_data)
                self.call(post_data)
        else:
            self.call(post_data)

    def show(self):
        self.argParse(['-n', '-c', '-m', '-i', '--short', '--instance'])
        opt_types = OrderedDict({'-n':'node', '-c': 'cluster', '-m':'module', '-i':'instance'})
        post_data = {'--short':self.show_short}
        trigger = 0

        ### To show specified type objects.
        for opt,obj_type in filter(lambda o: o[0] in self.args, opt_types.items()):
            self._show_object(getattr(self, obj_type+'s'), obj_type, post_data)
            trigger += 1

        ### To show all objects.
        if trigger == 0:
            for obj_type in opt_types.values():
                print("===> {}s:".format(obj_type.title()))
                self._show_object(None, obj_type, post_data)


    def showb(self):
        self.argParse(['-m', '-i', '--short'])
        if not (self.modules or self.instances):
            raise ArgError("ERROR: Option '-m' or '-i' must be specified.")
        if self.modules and self.instances:
            raise ArgError("ERROR: Option '-m' and '-i' cannot be specified at the same time.")

        post_data = {'--short': self.show_short}
        for obj_type in filter(lambda obj_type: getattr(self, obj_type+'s'), ('module','instance')):
            post_data['object'] = obj_type
            objects =  getattr(self, obj_type+'s')
            if len(objects) != 1:
                raise ArgError("ERROR: Multi-objects specification is not allow with 'showb' command.")
            post_data['name'] = objects[0]
            self.call(post_data)
