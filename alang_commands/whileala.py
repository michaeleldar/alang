statement = "WHILE"
indent = open('indent', 'w+')


def translate(line, outfile):
    global indent
    outfile.write(indent + 'while' + line[1] + line[2] + line[3] + ':\n')
    indentc = indent.read()
    indent.write(indentc + "    ")
