import random
temperatures = []

for i in range(7):
	temperatures.append(random.randint(26,40))

days_of_the_week = ["Sunday" , "Monday" , "Tuesday" , "Wednesday" , "Thursday" , "Friday" , "Saturday"]

good_days_count = 0

for i in temperatures:
	if (i % 2) == 0:
			good_days_count += 1
print(good_days_count)

highest_temp = 0
lowest_temp = 100

for i in temperatures:
	if i >= lowest_temp:
		lowest_temp = i
	if i >= highest_temp:
		highest_temp = i
lowest_temp_day_index = temperatures.index(lowest_temp)
highest_temp_day_index = temperatures.index(highest_temp)
print(highest_temp , lowest_temp)

highest_temp_day = days_of_the_week[highest_temp_day_index]
lowest_temp_day = days_of_the_week[lowest_temp_day_index]

sum = 0
for i in temperatures:
	sum = sum + i
avg_temp = sum / length(temperatures)

above_avg_days = []

for i in temperatures:
	if i >= avg_temp:
		above_avg_days.append(days_of_the_week[i])

for i in days_of_the_week:
	print(i , ": " , temperatures[i])
print("*")
print("Shelly had " , good_days_count , " good days")
print("*")
print("The hottest temperature was: " , highest_temp , " on " , highest_temp_day)
print("The coldest temperature was: " , lowest_temp , " on " , lowest_temp_day)
print("*")
print("The average temperature was: " , avg_temp)
print("The days with above average temperature were: " , above_avg_days)