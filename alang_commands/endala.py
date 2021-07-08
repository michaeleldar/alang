import subin
statement = "END"
indent = open('indent', 'r').read()


def translate(line, outfile):
    subin.main(outfile)
