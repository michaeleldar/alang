statement = "RANDOM"
indent = open('indent', 'r').read()


def translate(line, outfile):
    outfile.write(indent + 'import random')
    outfile.write(
        indent + line[1] + '=random.randint(' + line[2] + ',' + line[3] + ')\n')
