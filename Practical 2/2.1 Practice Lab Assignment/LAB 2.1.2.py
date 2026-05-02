# Initial dictionary with 10 predefined records
student = {
    1: "Amit",
    2: "Riya",
    3: "Kiran",
    4: "Neha",
    5: "Arjun",
    6: "Pooja",
    7: "Rahul",
    8: "Sneha",
    9: "Vikram",
    10: "Anjali"
}

# write your code here...

print("Original Dictionary:",student)

k=int(input())
v=input()
student[k]=v
print("After Insertion:",student)

k=int(input())
v=input()
if k in student:
	student[k]=v
print("After Update:",student)

k=int(input())
if k in student:
	student.pop(k)
print("After Deletion:",student)

print("Traversing Dictionary:")
for key in student:
	print(key,":",student[key])