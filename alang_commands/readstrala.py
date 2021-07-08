statement = "READSTR"
indent = open('indent', 'r').read()


def translate(line, outfile):
    outfile.write(indent + line[1] + '=input(' + line[2] + ')\n')
