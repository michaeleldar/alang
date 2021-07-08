statement = "ELSE"
indent = open('indent', 'r+w')


def translate(line, outfile):
    global indent
    outfile.write(indent + 'else:\n')
    indentc = indent.read()
    indent.write(indentc + "    ")
