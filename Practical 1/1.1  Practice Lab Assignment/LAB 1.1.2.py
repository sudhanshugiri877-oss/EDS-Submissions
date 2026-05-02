import math
n=int(input())

if (n>1) and (n<=9):
	n1=n**2
	print(n1)

elif (n>=10) and (n<=99):
	n2=math.sqrt(n)
	print(f"{n2:.2f}")

elif (n>=100) and (n<=999):
	n3=math.cbrt(n)
	print(f"{n3:.2f}")

else:
	print("Invalid")