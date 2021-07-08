indento = open('indent', 'r+w')
indent = indento.read()
indentf = ""


def main(outfileo):  # takes away a indent
    global indent
    global indentf
    if indent == "":
        print(
            "ERROR, END CANNOT BE USED WITHOUT A PRECEEDING IF, ELSE, ELSE_IF, WHILE, DEF_FUNC OR REPEAT :(")
        outfileo.truncate()
        quit()
    elif indent == "    ":
        indentf = ""
    elif indent == "        ":
        indentf = "    "
    elif indent == "            ":
        indentf = "        "
    elif indent == "                ":
        indentf = "        "
    else:
        print("ERROR, TOO MANY NESTED LOOPS :(")
        outfileo.truncate()
        quit()
    indento.write(indentf)
