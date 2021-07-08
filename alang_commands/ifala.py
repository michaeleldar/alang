statement = "IF"
indent = open('indent', 'r+w')


def translate(line, outfile):
    global indent
    outfile.write(indent + 'if' + line[1] + line[2] + line[3] + ':\n')
    indentc = indent.read()
    indent.write(indentc + "    ")
