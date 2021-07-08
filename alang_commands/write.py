statement = "WRITE"


def translate(line, indent, outfile):
    outfile.write(indent + 'print(' + line[1] + ')\n')
