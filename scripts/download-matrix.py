import io

types = [
    ('All in One', 'all-in-one', ('v2.0.2', 'v2.0.2')),
    ('UML CD + OntoUML', 'class-editor', ('v2.0.2', 'v2.0.2')),
    ('BORM ORD', 'borm-editor', ('v2.0.1', 'v2.0.1'), 'https://github.com/OpenPonk/borm-editor'),
    ('FSM', 'fsm-editor', ('v2.0.1', 'v2.0.1')),
    ('Petri Nets', 'petrinets', ('v2.0.1', 'v2.0.1')),
    ('All in One', 'all-in-one', ('nightly', 'latest')),
    ('UML CD + OntoUML', 'class-editor', ('nightly', 'latest'), 'https://github.com/OpenPonk/class-editor'),
    ('BORM ORD', 'borm-editor', ('nightly', 'latest'), 'https://github.com/OpenPonk/borm-editor'),
    ('FSM', 'fsm-editor', ('nightly', 'latest'), 'https://github.com/OpenPonk/fsm-editor'),
    ('Petri Nets', 'petrinets', ('nightly', 'latest'), 'https://github.com/OpenPonk/petrinets'),
]

header = '''.. list-table:: Download Matrix
   :header-rows: 1

   * - Build
     - Version
     - Linux
     - Windows
     - Pharo image
'''

platforms = ['linux', 'win', 'pharo-image']

ind = '   '
in2 = ind + '  - '

stream = io.StringIO()

stream.write(header)
stream.write('\n')
	
for arr in types:
    name = arr[0]
    plugin = arr[1]
    versions = arr[2]

    stream.write(ind)

    if len(arr)==4:
        stream.write('* - `')
        stream.write(name)
        stream.write(' <')
        stream.write(arr[3])
        stream.write('>`_\n')
    else:
        stream.write('* - **')
        stream.write(name)
        stream.write('**\n')
   
    stream.write(in2)
    if len(versions) == 0:
        stream.write('TBA\n')
        for plat in platforms:
            stream.write(in2)
            stream.write('\n')
    else:
        stream.write(versions[0])
        stream.write('\n')
        for plat in platforms:
            stream.write(in2)
            stream.write(':download-link:`')
            stream.write(plugin)
            stream.write(',')
            stream.write(versions[1])
            stream.write(',')
            stream.write(plat)
            stream.write('`\n')

with open('download-matrix.txt', 'w') as f:
    f.write(stream.getvalue())
