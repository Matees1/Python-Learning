def addTwoNumbers(num1, num2):
    return float(num1) + float(num2)

def multiplyTwoNumbers(num1, num2):
    return float(num1) * float(num2)

def divideTwoNumbers(num1, num2):
    return float(num1) / float(num2)

def remainderOfTwoNumbers(num1, num2):
    return float(num1) % float(num2)

def subtractTwoNumbers(num1, num2):
    return float(num1) - float(num2)

x = input("Please enter in a number: ")
y = input("Please enter in a second number: ")

addition = addTwoNumbers(x, y)
difference = subtractTwoNumbers(x,y)
multiplication = multiplyTwoNumbers(x, y)
divided = divideTwoNumbers(x,y) 
divRemainder = remainderOfTwoNumbers(x,y)

print(f"Your numbers added are: {addition}")
print(f"Your numbers subtracted are {difference}")
print(f"Your numbers multiplied are: {multiplication}")
print(f"Your numbers divided are: {divided}, and the remainder is {divRemainder}")