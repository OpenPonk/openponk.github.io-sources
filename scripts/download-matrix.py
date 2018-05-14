import StringIO

types = [
    ('All in One', 'all-in-one', ('outdated', 'latest')),
    ('UML CD + OntoUML', 'uml', ('0.9.x', '0.9.3')),
    ('BORM ORD', 'borm', ()),
    ('FSM', 'fsm', ()),
    ('Petri Nets', 'petrinets', ()),
    ('DEMO (WIP)', 'demo', ()),
]

header = '''.. list-table:: Download Matrix
   :header-rows: 1

   * - Build
     - Version
     - Linux
     - Windows
     - image only
'''

baseUrl = 'https://openponk.ccmi.fit.cvut.cz/builds'

platforms = ['linux', 'windows', 'image']

ga = 'ga(''send'', ''event'', ''Downloads'', ''download'', ''{type}-{platform}-stable'')'

anchor = '<a href="' + baseUrl + '/openponk-{platform}-{version}.zip" onclick="' + ga + '">download</a>'

ind = '   '
in2 = ind + '  - '

stream = StringIO.StringIO()

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
