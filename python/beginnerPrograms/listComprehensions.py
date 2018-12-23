# Made by Ch1pless

import random
a = [random.randrange(0,100,1) for i in range(random.randrange(5,50,1))]
b = [a[ind] for ind in range(len(a)) if a[ind] % 2 == 0 and a[ind] not in a[slice(0,ind)]]

print("Random List Input: " + str(a) + '\n' + "Even List Output: " + str(b))
input("\nPress any key to exit\n"+'*'*20)
