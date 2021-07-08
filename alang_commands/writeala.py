statement = "WRITE"
indent = open('indent', 'r').read()


def translate(line, outfile):
    outfile.write(indent + 'print(' + line[1] + ')\n')
