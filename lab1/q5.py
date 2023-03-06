#n1=int(input("Enter the number 1 "))
#n2=int(input("Enter the number 2 "))
#n3=int(input("Enter the number 3 "))
n1,n2,n3=10,30,50
if(n1>n2)and(n1>n3):
	largest=n1
if(n2>n3)and(n2>n1):
	largest=n2
else:
	largest=n3

print("the largest is",largest)