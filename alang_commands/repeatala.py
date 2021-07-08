statement = "REPEAT"
indent = open('indent', 'r+w')


def translate(line, outfile):
    global indent
    outfile.write(indent + 'for x in range(0,' + line[1] + '):\n')
    indentc = indent.read()
    indent.write(indentc + "    ")
