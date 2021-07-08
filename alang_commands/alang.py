#!/usr/bin/python3

import sys

import writeala
import addala
import comala
import declareala


sys.stderr = 0
script, infile, outfile = sys.argv
indent = ""
infileo = open(infile)
outfileo = open(outfile)
indinto = open('indent', 'r+w')
infileo.seek(0)
indent = ""
indinto.write(indent)

commands = [writeala, addala, comala, declareala]


def scan(line):  # Main compiler
    for command in commands:
        if command.statement == line[0]:
            command.translate(line, outfileo)


line = infileo.readline().split()

while line != "":
    scan(line)
    line = infileo.readline().split()

infileo.close()
outfileo.flush()
outfileo.close()
