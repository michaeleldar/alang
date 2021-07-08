statement = "DEF_FUNC"
indent = open('indent', 'w+')


def translate(line, outfile):
    global indent
    outfile.write(indent + 'def ' +
                  line[1] + '(' + line[2] + ',' + line[3] + ',' + line[4] + ')\n')
    indentc = indent.read()
    indent.write(indentc + "    ")
