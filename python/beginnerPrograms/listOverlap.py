# Made by Ch1pless

import random

a = [random.randrange(0,20,1) for i in range(random.randrange(5,20,1))]
b = [random.randrange(0,20,1) for i in range(random.randrange(5,20,1))]
c = [a[ind] for ind in range(len(a)) if a[ind] in b and a[ind] not in a[slice(0,ind,1)]]

print("List 1: " + str(a) + '\n' + "List 2:" + str(b))
if len(c) == 0 :
	print("No matching numbers.")
else :
	print("Matching Numbers: " + str(c))
input("\nPress any key to exit\n"+'*'*20)
