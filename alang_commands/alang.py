#!/usr/bin/python3
import sys
from alang_commands import *
sys.stderr = 0
script, infile, outfile = sys.argv
indent = ""


def subin():  # takes away a indent
    global indent
    if indent == "":
        print("ERROR, ENDIF CANNOT BE USED WITHOUT A PRECEEDING IF :(")
        outfileo.truncate()
        quit()
    elif indent == "    ":
        indent = ""
    elif indent == "        ":
        indent = "    "
    elif indent == "            ":
        indent = "        "
    elif indent == "                ":
        indent = "        "
    else:
        print("ERROR, TOO MANY NESTED LOOPS :(")
        outfileo.truncate()
        quit()


def scan(line):  # Main compiler
    pass


infileo = open(infile, 'r')
outfileo = open(outfile, 'w')

infileo.seek(0)
line = infileo.readline().split()

while line != "":
    scan(line)
    line = infileo.readline().split()

infileo.close()
outfileo.flush()
outfileo.close()
