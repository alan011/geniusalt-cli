from .common import *

class Add(Handler):
    def add(self):
        self.argParse(['-n','-e','-m','-pr', '-po', '-i','-p', '-c' ])
        if not (self.nodes or self.modules or self.instances or self.clusters):
            raise ArgError("ERROR: Add command requires an object name, which can be specified with option '-n, -m, -i or -c'.")
        if (self.nodes and self.modules) or (self.nodes and self.instances):
            self.error("ERROR: Option '-n' cannot be used with '-m' or '-i' when to add an object.")

        if self.nodes:
            for name in self.nodes:
                post_data = {'object':'node', 'name':name}
                if self.environment:
                    post_data['environment'] = self.environment
                self.call(post_data)

        if self.modules:
            for name in self.modules:
                post_data = {'object':'module', 'name':name}
                if self.pillar_required:
                    post_data['pillar_required'] = self.pillar_required
                if self.pillar_optional:
                    post_data['pillar_optional'] = self.pillar_optional
                self.call(post_data)

        if self.instances:
            if not self.module_belong:
                raise ArgError("ERROR: Instance must belong to a module, use '-m' to specify it.")
            for name in self.instances:
                post_data = {'object':'instance', 'name':name, 'module_belong': self.module_belong}
                if self.pillars:
                    post_data['pillar'] = self.pillars
                if self.environment:
                    post_data['environment'] = self.environment
                self.call(post_data)

        if self.clusters:
            for name in self.clusters:
                post_data = {'object':'cluster', 'name':name}
                if self.cluster_members:
                    post_data['nodes'] = self.cluster_members
                if self.bind_instances:
                    post_data['instances'] = self.bind_instances

                self.call(post_data)
