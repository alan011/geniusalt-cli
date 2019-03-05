class Usage(object):
    @staticmethod
    def usage():
        print("""
===================================
Usage:
    gnsalt command [<object options>] [<LongTerms options>]

===> Command list:
    scan            Auto add Modules or Nodes. This will also update a module if pillar.json has changed.
                    Supported options: '-m', '-n'
    add             To add a Module, Instance or Node.
                    Supported options: '-n','-e','-m','-pr', '-po', '-i','-p'
                    If '-m' used with '-i', means to add an instance which belongs to module specified by '-m'.
    del/delete      To delete Modules, Instances or Nodes.
                    Supported options: '-n', '-m', '-i'
    show            To show data of Modules, Instances or Nodes.
                    Supported options: '-n', '-m', '-i', '--short', '--instance'
    pset            To set pillar of instance.
                    Supported options: '-i' , '-p', '-e'
    pdel            To remove pillar from a instance.
                    Supported options: '-i' , '-p', '-e'
    eset            To set environment of a node.
                    Supported options: '-n' , '-e'
    include         To set instances to include other instances.
                    Supported options: '-i' , '-ii'
    exclude         To set instances to exclude included instances.
                    Supported options: '-i' , '-ii'
    bind            To set nodes to bind instances or modules. This is only set on DB level, not apply to the real hosts.
                    Supported options: '-n', '-i', '-m'
    unbind          To set nodes to unbind instances or modules. This is only set on DB level, not apply to the real hosts.
                    Supported options: '-n', '-i', '-m'
    joinc           To set nodes to join into cluster. This is only set on DB level, not apply to the real hosts.
                    Supported options: '-n', '-c'
    unjc            To set nodes to unjoin from cluster. This is only set on DB level, not apply to the real hosts.
                    Supported options: '-n', '-c'
    push            To apply instances or modules to the real hosts(nodes). This will make real change on hosts.
                    Supported options: '-n', '-m', '-i', '--checkself', '--only-module'
                    If '-i' or '-m' objects specified, only the specified instances or modules will be applied, not the whole pillar bound to this node.
    lock            To lock objects to prevent it to be pushed to a real host.
                    If to push an locked object, An error will be given.
                    Supported options: '-n', '-m', '-i'
    unlock          To unlock locked objects.
                    Supported options: '-n', '-m', '-i'
    showb           To show nodes which has bound the specified instance or module.
                    Supported options: '-i', '-m'

===> object options:
    -n node1,node2,...
        To specify 'Node' basic objects.

    -m mod1,mod2,...
        To specify 'Module' basic objects.

    -pr var1,var2,var3...
        To specify pillar variables required for a module. Only available when to 'add' a module manually.

    -po var1,var2,var3...
        To specify optional pillar variables for a module. Only available when to 'add' a module manually.

    -i instance1,instance2,...
        To specify 'Instance' basic objects.

    -ii instance1,instance2,...
        To specify instances to be included. Only available for 'include' command.
        If an instance which included others instances bound to a node, key '__include__' will be auto added as a pillar variable of this instance, which value is a dict included pillars of other instances.

    -p var1=value1,var2=value2,...  (for pset)
       var1,var2,var3,...           (for pdel)
        To specify 'pillar' data. Value of pillars could not contain ','.

    -e envronment
        To specify envronment for nodes or pillar. Do not support multi-values seporated by ','.

===> Boolean LongTerms:
    --short
        Available for 'show' and 'showb' command.
        To show only object names, not all attributes of object.

    --instance
        Only available when to 'show' modules with '-m' option.
        To show instances of a module when showing modules.

    --only-module
        Only available for 'push' command with only '-n' option. Cannot used with '-i'.
        To push nodes with only module basics, no any instance pushed.

    --all-instances
        Only available for 'push' command with '-n' and '-m' option. Cannot used with '-i'.
        To push all instances of a module, not only the module basics.

===================================""")
