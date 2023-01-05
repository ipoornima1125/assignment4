#question 3
import random
i,j=0,0
ans=0
for k in range(0,10):
    i=random.randint(1,11)
    j=random.randint(1,11)
    print("question",k+1,":",i,"*",j,"=")
    ans=int(input("ans:"))
    if ans==i*j:
        print("right")
    else:
        print("wrong, the answer is",i*j)


#Question 2
year= int(input("enter year:"))
if( year%4==0):
    if( year%100==0):
        if( year%400==0):
         print("it is a leap year")
        else:
         print("it is not a leap year")

else:
    print("it is not a leap year")

#Question 4
for i in range(1, 200):
    if i % 5 == 2 and i % 6 == 3 and i % 7 == 2:
        print("Number of candies is ", i)

marks = int(input("enter marks of student:"))  # question 1
if (marks >= 80):
    print("A")
elif (marks < 80 and marks >= 60):
    print("B")
elif (marks < 60 and marks >= 50):
    print("C")
elif (marks < 50 and marks >= 45):
    print("D")
elif (marks < 45 and marks >= 25):
    print("E")
else:
    print("F")
