statement = "ELSE"
indent = open('indent', 'w+')


def translate(line, outfile):
    global indent
    outfile.write(indent + 'else:\n')
    indentc = indent.read()
    indent.write(indentc + "    ")
