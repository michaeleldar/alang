statement = "EXIT"
indent = open('indent', 'r').read()


def translate(line, outfile):
    outfile.write(indent + "quit()\n")
