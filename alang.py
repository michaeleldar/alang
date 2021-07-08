#!/usr/bin/python3
import sys
from alang_commands import *
import globevars
sys.stderr = 0
script, infile, outfile = sys.argv
#infile = 'examples/def_func.ala'
#outfile = 'examples/def_func.py'


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
    global indent
    c_line = line
    if c_line[0] == "WRITE":
        outfileo.write(indent + 'print(' + c_line[1] + ', end="")\n')
    elif c_line[0] == "ADD":
        outfileo.write(indent + c_line[1] + '=' +
                       c_line[2] + '+' + c_line[3] + '\n')
    elif c_line[0] == "SUBTRACT":
        outfileo.write(indent + c_line[1] + '=' +
                       c_line[2] + '-' + c_line[3] + '\n')
    elif c_line[0] == "MULTIPLY":
        outfileo.write(indent + c_line[1] + '=' +
                       c_line[2] + '*' + c_line[3] + '\n')
    elif c_line[0] == "DIVIDE":
        outfileo.write(indent + c_line[1] + '=' +
                       c_line[2] + '/' + c_line[3] + '\n')
    elif c_line[0] == "DECLARE":
        outfileo.write(indent + c_line[1] + '=' + c_line[2] + '\n')
    elif c_line[0] == "READSTR":
        outfileo.write(indent + c_line[1] +
                       '=input(' + c_line[2] + ')\n')
    elif c_line[0] == "READINT":
        outfileo.write(indent + c_line[1] +
                       '=int(input(' + c_line[2] + '))\n')
    elif c_line[0] == "IF":
        outfileo.write(indent + 'if ' +
                       c_line[1] + c_line[2] + c_line[3] + ":\n")
        indent = indent + "    "
    elif c_line[0] == "REPEAT":
        outfileo.write(indent + 'for x in range(1,' + c_line[1] + '):\n')
        indent = indent + "    "
    elif c_line[0] == "WHILE":
        outfileo.write(indent + 'while ' +
                       c_line[1] + c_line[2] + c_line[3] + ":\n")
        indent = indent + "    "
    elif c_line[0] == "ELSE_IF":
        outfileo.write(indent + 'elif ' +
                       c_line[1] + c_line[2] + c_line[3] + ":\n")
        indent = indent + "    "
    elif c_line[0] == "ELSE":
        outfileo.write(indent + 'else:\n')
        indent = indent + "    "
    elif c_line[0] == "END":
        subin()
    elif c_line[0] == "DEF_FUNC":
        outfileo.write(indent + 'def ' + c_line[1] + '():\n')
        indent = indent + '    '
    elif c_line[0] == "RUN_FUNC":
        outfileo.write(indent + c_line[1] + '()\n')
    elif c_line[0] == "EXIT":
        outfileo.write(indent + "quit()\n")
    elif c_line[0] == "RANDOM":
        outfileo.write(indent + 'import random\n')
        outfileo.write(
            indent + c_line[1] + '=' + 'random.randint(' + c_line[2] + ',' + c_line[3] + ')\n')
    elif c_line[0] == "COM":
        pass
    else:
        print("ERROR, ", c_line[0], "IS NOT A COMMAND :(")
        outfileo.truncate()
        quit()


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
