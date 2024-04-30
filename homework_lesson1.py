#Decisions at the Crossroad

#Task1 code_correction
number = int(input ("Enter a number: "))

if number > 0:
    print("The number is positive.")
elif number == 0:
    print("The number is zero.")
else:
    print("The number is negative.")

    
#The Greatest Showdown
#Task1 identify_the_greatness
num1 = float(input("Enter the first number: "))
num2 = float(input("Please enter another number: "))
num3 = float(input("Enter the last number: "))

if num1 > num2 and num1 > num3:
    print(f"{num1} is the largest")
elif num2 > num1 and num2> num3:
    print(f"{num2} is the largest")
elif num3 > num1 and num3 > num2:
    print(f"{num3} is the largest")


#Task2
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

largest = max(num1, num2, num3)

smallest = min(num1, num2, num3)

print("The smallest number is", smallest)
print("The largest number is", largest)