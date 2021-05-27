from matplotlib import pyplot
from random import randrange
from datetime import date

total_cases = []

week_day = []

day = "{}".format(date.today()).split('-')

minus_day = 7

for i in range(7):
	try:
		week_day.append("{}/{}".format(int(day[2]) - minus_day, day[1]))
		minus_day -= 1
	except:
		pass
print(week_day)

for i in week_day:
	total_cases.append(randrange(1000, 10000))
	
pyplot.plot(week_day,total_cases, linestyle = 'dashed', marker = '*', markerfacecolor = 'orange', color = 'red')
pyplot.savefig('week.png')


