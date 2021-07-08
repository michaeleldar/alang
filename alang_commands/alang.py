#!/usr/bin/python3

import sys
import writeala
import addala


sys.stderr = 0
script, infile, outfile = sys.argv
indent = ""
infileo = open(infile)
outfileo = open(outfile)
infileo.seek(0)
indent = ""

commands = [writeala, addala]


def subin():  # takes away a indent
    global indent
    if indent == "":
        print(
            "ERROR, END CANNOT BE USED WITHOUT A PRECEEDING IF, ELSE, ELSE_IF, WHILE, DEF_FUNC OR REPEAT :(")
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
    for command in commands:
        if command.statement == line[0]:
            command.translate(line, indent, outfileo)


line = infileo.readline().split()

while line != "":
    scan(line)
    line = infileo.readline().split()

infileo.close()
outfileo.flush()
outfileo.close()
