statement = "READINT"
indent = open('indent', 'r').read()


def translate(line, outfile):
    outfile.write(indent + line[1] + '=int(input(' + line[2] + '))\n')
