import io

types = [
    ('All in One', 'all-in-one', ('nightly', 'latest')),
    ('UML CD + OntoUML', 'class-editor', ('nightly', 'latest')),
    ('UML CD + OntoUML', 'class-editor', ('1.0.0', '1.0.0')),
    ('BORM ORD', 'borm-editor', ('nightly', 'latest')),
    ('FSM', 'fsm-editor', ('nightly', 'latest')),
    ('FSM', 'fsm-editor', ('1.0.0', '1.0.0')),
    ('Petri Nets', 'petrinets', ('nightly', 'latest')),
    ('Petri Nets', 'petrinets', ('1.0.0', '1.0.0')),
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
