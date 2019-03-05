import json, requests, re, yaml, sys
from .config import *

class ArgError(Exception):
    pass

class APICaller(object):
    def post_caller(self, api_url, post_data=None, isjson=True):
        ### make request.
        param = 'json' if isjson else 'data'
        try:
            r = requests.post(api_url, **{param: post_data})
        except:
            return "API ERROR: host not reachable.\n  API URL: {}\n  {}: {}".format(api_url, param, str(post_data))

        ### handle with return data.
        if r.status_code == 200:
            try:
                return_data = r.json()
            except ValueError:  #This means data returned is a normal string, which cannot be used with r.json().
                return r.text
            else:
                return return_data
        elif r.status_code == 500:
            err_message = "API ERROR: API corrupt.\n"
            if r.text:
                err_message += r.text
            return err_message
        else:
            return "API returned incorrectly: {}\nstatus code: {}".format(r.text, r.status_code)

class Handler(APICaller):
    api        = GENIUSALT_API
    auth_token = AUTH_TOKEN
    action    = None
    args      = None

    ### Object attributes parsed from args.
    nodes     = None
    clone_target_node = None
    clusters  = None
    instances = None
    modules   = None
    pillars   = None
    pillar_required   = None
    pillar_optional   = None
    environment       = None
    included_instances = None
    module_belong = None
    cluster_members = None
    bind_instances = None ### for cluster add.
    show_short = False
    show_instances = False
    # push_checkself  = False
    push_only_module = False
    push_all_instances = False

    ### action result
    api_return = None

    def _set_longTerm(self,longTerm,attr,default=True):
        setattr(self, attr, default)
        while longTerm in self.args:
            self.args.remove(longTerm)

    def _get_option_value(self, opt):
        """
        If opt is not the last arg and next arg after opt is not an option specifier,
        then next arg is the value of this opt.
        Note: self.args will be changed after running this method.
        """
        l = len(self.args)
        i = self.args.index(opt)
        val = self.args.pop(i + 1) if i < l - 1 and not re.search('^\-{1,2}\w+', self.args[i + 1]) else None
        self.args.pop(i)
        return val

    def _pillar_parse(self, items):
        """
        To parse value specified by '-p'.
        Legal items may like ['p1=v1', 'p2=v2', ...], or ['p1', 'p2', ...].
        Note: If '=' in item, string before the first '=' is treated as the pillar name,
              rest string after the first '=' is treated as the value of this pillar.
              So pillar value could be an empty string, or contain other '='.
        """
        pillars = {}
        for i in items:
            if '=' in i:
                p_name          = i.split('=')[0]
                value_index     = i.index('=') + 1
                pillars[p_name] = i[value_index:]
            else:
                pillars[i] = None
        return pillars

    def _split_values(self, opt, pillar_parse=False):
        """
        To split option values seperated by ',' to list.
        """
        _values = self._get_option_value(opt)
        values  = _values.split(',') if _values else []
        items   = [ n for n in filter(lambda v: v, values)]
        if pillar_parse:
            items = self._pillar_parse(items)
        return items if items else None

    def argParse(self, supported_options):
        args = self.args.copy()
        for i in filter(lambda o: o in supported_options, args):
            if i == '-p':
                self.pillars = self._split_values(i, pillar_parse=True)
            if i == '-e':
                self.environment = self._get_option_value(i)
            if i == '-i':
                if self.action == 'add' and '-c' in args:
                    self.bind_instances = self._split_values(i)
                else:
                    self.instances = self._split_values(i)
            if i == '-m':
                if self.action == 'add' and '-i' in args:
                    self.module_belong = self._get_option_value('-m')
                else:
                    self.modules = self._split_values(i)
            if i == '-c':
                self.clusters = self._split_values(i)
            if i == '-n':
                if self.action == 'add' and '-c' in args:
                    self.cluster_members = self._split_values('-n')
                else:
                    self.nodes = self._split_values(i)
            if i == '--from-node':
                self.clone_target_node = self._get_option_value(i)
            if i == '-ii':
                self.included_instances = self._split_values(i)
            if i == '-pr':
                self.pillar_required = self._split_values(i)
            if i == '-po':
                self.pillar_optional = self._split_values(i)
            if i == '--short':
                self._set_longTerm('--short','show_short')
            if i == '--instance':
                self._set_longTerm('--instance','show_instances')
            # if i == '--checkself':
            #     self._set_longTerm('--checkself','push_checkself')
            if i == '--only-module':
                self._set_longTerm('--only-module','push_only_module')
            if i == '--all-instances':
                self._set_longTerm('--all-instances','push_all_instances')

        if self.args:  # Remained args are illegal for action.
            raise ArgError("ERROR: invalid arguments '{}' found for action '{}'".format(self.args, self.action))

        self.args = args

    def handleAPIReturn(self):
        if isinstance(self.api_return, str): ### Means operation returns incorrectly.
            print(self.api_return)
        elif isinstance(self.api_return, dict):   ### Means operation returns correctly.
            if self.api_return.get('data'):
                for obj in self.api_return['data']:
                    if self.show_short:
                        print(obj['name'])
                    else:
                        print(obj['name'], end=':\n  ')
                        print(yaml.dump([{k:v} for k,v in obj.items()], default_flow_style=False).replace('\n','\n  '))
            if self.api_return.get('message'):
                print(self.api_return['message'])
            if self.api_return.get('pushlog'):
                for node in self.api_return['pushlog']:
                    print("===> Push log for node: %s" % node)
                    print(*self.api_return['pushlog'][node], sep='')

    def call(self, post_data):
        self.post_data.update(post_data)
        self.api_return = self.post_caller(self.api, self.post_data)
        self.handleAPIReturn()
