#Write a python program to calculate area of 10 different circles. Given the pie = 22/7 and radius of the circles entered by user using Simple Function, Parameterized Function.. 
# Return Type with function and return type with parameterized Functions

def area(radius):
    pie = 3.14
    area = round(pie * radius * radius,2)
    return area

print('''Name : Anmol
        Uid : 21BCS2898''')
for i in range(11):
    r = int(input("Enter radius\n"))
    ar = area(r)
    print("Area of circle is " + str(ar))
