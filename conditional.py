light = "pink"

if(light == "red"):
    print("stop")
elif(light == "green"):
    print("go")
    
elif(light == "yellow"):
       print("look")

else:
     print("light is broken")

print("end of code")   

marks = int(input("Enter your marks: "))

if marks >= 90:
    grade = "A"
elif marks >= 80:
    grade = "B"
elif marks >= 70:
    grade = "C"
else:
    grade = "D"

# Corrected print statement
print("Grade of the student ->", grade)
# OR using f-string
print(f"Grade of the student -> {grade}")


# WAP to find the greatest of 3 numbers entered by the user.

a = int(input("enter a number: "))
b = int(input("enter a number: "))
c = int(input("enter a number: "))

if(a >= b and a >= c):
  print("first number", a)
elif( b >= c):
    print("second number", b)
else:
    print("third number", c)   
