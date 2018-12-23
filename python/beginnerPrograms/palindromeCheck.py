# Made by Ch1pless

userinput = input("Input a word to check if it is a palindrome: ")
word = userinput.lower()
rev = word[::-1]
if word == rev :
	print(userinput + " is a palindrome.")
else :
	print(userinput + " is not a palindrome.")
input("\nPress any key to exit\n"+'*'*20)
