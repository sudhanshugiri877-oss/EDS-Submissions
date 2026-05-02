n = int(input())

marks = list(map(int, input().split()))

failed = False

for m in marks:
	if m<40:
		failed = True
		break

if failed:
	print("Fail")
else:

	aggregate = sum(marks)/n

	if aggregate > 75:
		grade="Grade: Distinction"

	elif aggregate>=60:
		grade="Grade: First Division"

	elif aggregate>=50:
		grade="Grade: Second Division"

	elif aggregate>=40:
		grade="Grade: Third Division"

	print(f"Aggregate Percentage: {aggregate:.2f}")
	print(grade)