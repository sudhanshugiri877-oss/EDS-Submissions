from datetime import date

date_str1 =input()
date_str2 =input()

y1, m1, d1=map(int, date_str1.split('-'))
y2, m2, d2=map(int, date_str2.split('-'))

d1_obj=date(y1, m1, d1)
d2_obj=date(y2, m2, d2)

delta=d2_obj-d1_obj

print(delta.days)