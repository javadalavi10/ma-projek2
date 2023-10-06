import math

print("welcome to calculator")

print("+ :sum")
print("-: sub")
print("*: mul")
print("log")
print("factorial")
print("tan")
print("cos")
print("sqrt")
print("sin")
print("/: div")
print("pleae enter your choice")
sd = input()

if sd == "+" or sd == "-" or sd == "*" or sd == "/":
    a = float(input("enter first number:"))
    s = float(input("enter secomb number:"))
else:
    a= float(input("enter first number:"))

if sd=="+":
    result =a + s

if sd == "-":
    result = a - s

elif sd== "*":
    result = a * s

elif sd== "/":
  if s==0: 
    result ="canot divide by zero"
    
  else:
        result = a / s
     
elif sd == "sin":
    result = math.sin(a)

elif sd == "log":
    result = math.log(a)

elif sd == "cos":
    result = math.cos(a)

elif sd == "tan":
    result = math.tan(a)

elif sd == "cot":
    result = math.factorial(a)

elif sd == "sqrt":
    result = math.sqrt,(a)

print(result)
