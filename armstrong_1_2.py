print('Name = Anmol UID = 21BCS2898')
number = int(input("Enter a number: "))
sum = 0
length = len(str(number))
temp = number
while temp > 0:
   digit = temp % 10
   sum += digit ** length
   temp //= 10
if number == sum:
   print(f"{number}is an Armstrong number")
else:
   print(f"{number} is not an Armstrong number")