statement = "RUN_FUNC"
indent = open('indent', 'r').read()


def translate(line, outfile):
    outfile.write(indent + line[1] + '()\n')
