# Author Yongdong Xi (Oct 19)

q = float(input("What is the day of the month?"))
m1 = float(input("What is the month?"))
if m1 >= 3:
    m2 = m1
else:
    m2 = m1 + 12
year = float(input("What is the year?"))
j = year//100
k = year % 100

the_day_of_the_week = ((q + ((26 * (m2 + 1)) // 10)) + k + (k // 4) + (j // 4) + 5 * j) % 7
h = the_day_of_the_week

if h == 0:
    print("the day is the Saturday")
elif h == 1:
    print("the day is the Sunday")
elif h == 2:
    print("the day is the Monday")
elif h == 3:
    print("the day is the Tuesday")
elif h == 4:
    print("the day is the Wdenesday")
elif h == 5:
    print("the day is the Tursday")
elif h == 6:
    print("the day is the Friday")
