statement = "WRITE"

infilet = open('/home/$USER/alang/global_vars/infile', 'r')
outfilet = open('/home/$USER/alang/global_vars/outfile', 'r')
indent = open('/home/$USER/alang/global_vars/indent', 'r')
infileo = open(infilet.read(), 'w')


def translate():
