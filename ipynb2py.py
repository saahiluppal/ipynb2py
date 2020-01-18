import json
import sys

"""
-space 
-s 
-> include space
"""

ipynb_name = sys.argv[1]
py_name = sys.argv[2] if len(sys.argv)>=3 else 'main.py'

with open(ipynb_name) as handle:
    output = handle.read()

script = ''

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