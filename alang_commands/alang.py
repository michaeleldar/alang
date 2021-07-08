#!/usr/bin/python3

import sys

import writeala
import addala
import comala
import declareala
import def_funcala
import divideala
import elseala
import else_ifala
import endala
import exitala
import ifala
import multiplyala
import randomala
import readintala
import readstrala
import repeatala
import run_funcala
import whileala

sys.stderr = 0
script, infile, outfile = sys.argv
indent = ""
infileo = open(infile)
outfileo = open(outfile)
indinto = open('indent', 'r+w')
infileo.seek(0)
indent = ""
indinto.write(indent)

commands = [writeala, addala, comala,
            declareala, def_funcala, divideala, elseala,
            else_ifala, endala, exitala, ifala, multiplyala,
            randomala, readintala, readstrala, repeatala,
            whileala, run_funcala]


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
