Name= input("please enter your name:")
family=input("please enter your family:")
city=input("please enter your city:")
country= "lran"

f =float(input("Enter the grade of the first lesson:"))
a = float(input("Enter the grade of the second lesson:"))
s = float(input("Enter the grade of the third lesson:"))
d=(a+s+f)/3

print("student",Name,family,"you",city,country)

if d < 10 :
    print("The card is broken","&quot\U0001F923&quot")

else:
    print(d)




