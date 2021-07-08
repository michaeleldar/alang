statement = "DECLARE"


def translate(line, indent, outfile):
    outfile.write(indent + line[1] + '=' + line[2] + '\n')
