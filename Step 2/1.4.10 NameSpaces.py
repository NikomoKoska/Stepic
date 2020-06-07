global_namespaces = {'global': {'parent': None, 'var': []}}
def create(namespace, parent):
    global_namespaces[namespace] = {'parent': parent, 'var': []}

def add(namespace, var):
    global_namespaces[namespace]['var'].append(var)

def get(namespace, var):
    if namespace == 'global' and var not in global_namespaces[namespace]['var']:
        return None
    if var in global_namespaces[namespace]['var']:
        return namespace
    else:
        return get(global_namespaces[namespace]['parent'], var)

num = int(input())
for i in range(num):
    cmd, namesp, arg = input().split()
    if cmd == 'add':
        add(namesp, arg)
    elif cmd == 'create':
        create(namesp, arg)
    elif cmd == 'get':
        print(get(namesp, arg))