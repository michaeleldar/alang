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
