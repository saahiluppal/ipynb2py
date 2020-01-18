import json
import sys

ipynb_path = None
py_name = 'main.py'
space = False

script = ''

arguments = sys.argv[1:]
for arg in arguments:
    if arg.endswith('ipynb'):
        ipynb_path = arg
    elif arg.endswith('py'):
        py_name = arg
    elif arg.startswith('-'):
        if 's' in arg:
            space = True

if not ipynb_path:
    print('No notebook selected')
    exit()
if not py_name:
    print('Default Python file => main.py')

with open(ipynb_path) as handle:
    output = handle.read()

contents = json.loads(output)

for cell in contents['cells']:
    if cell['cell_type'] == 'code':
        if cell['source']:
            source = ''.join(cell['source'])
            if space:
                script+=(source + '\n\n')
            else:
                script+=(source + '\n')

with open(py_name,'w') as handle:
    handle.writelines(script)