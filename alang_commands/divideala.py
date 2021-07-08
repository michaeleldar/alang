statement = "DIVIDE"
indent = open('indent', 'r').read()


def translate(line, outfile):
    outfile.write(indent + line[1] + '=' + line[2] + '/' + line[3] + '\n')
