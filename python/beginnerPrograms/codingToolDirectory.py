# Made by Ch1pless

import subprocess

choice = input(
"Directory\n"+\
"-"*30+\
"\n1. Atom for Personal Projects\n\
2. CMD for Python\\beginnerPrograms\n\
Input: ")

cmd = subprocess.Popen("cmd.exe /k", stdin=subprocess.PIPE)

if choice == '1' :
	cmd.communicate(b"cd D:\\ProgrammingEscapades\\Personal-Projects\natom .\n")
elif choice == '2' :
	cmd.communicate(b"cd D:\\ProgrammingEscapades\\Personal-Projects\\python\\beginnerPrograms\nstart cmd\n")
