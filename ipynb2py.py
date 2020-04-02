import json
from absl import app
from absl import flags

"""
-space 
-s 
-> include space
"""

FLAGS = flags.FLAGS

flags.DEFINE_string('ipynb', None, "Notebook Path")
flags.DEFINE_bool('space', False, 'Include Space after each Cell')
flags.DEFINE_boolean('debug', False, 'Produces debugging output.')
flags.DEFINE_string('py', None, "Script Path")

def main(argv):
    if FLAGS.debug:
        print('Non-Flag Arguments:', argv)

    assert FLAGS.ipynb != None, "Notebook Name not provided"

    if not FLAGS.py:
        FLAGS.py = FLAGS.ipynb.replace('.ipynb', '.py')

    with open(FLAGS.ipynb) as handle:
        output = handle.read()

    script = ''

    contents = json.loads(output)

    for cell in contents['cells']:
        if cell['cell_type'] == 'code':
            if cell['source']:
                source = ''.join(cell['source'])
                if FLAGS.space:
                    script+=(source + '\n\n')
                else:
                    script+=(source + '\n')

    with open(FLAGS.py,'w') as handle:
        handle.writelines(script)
    
if __name__ == '__main__':
    app.run(main)