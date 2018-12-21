# Made by Ch1pless

number = int(input("What number do you want the divisors of? "))

div = [num for num in range(1,number+1) if number % num == 0]

print("List of Divisors of " + str(number) + ": " + str(div))
print('*'*20)
