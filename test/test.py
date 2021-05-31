import csv


date_filter = []

with open('week_data.csv', 'r') as raw_data:
	one_week = csv.DictReader(raw_data)
	
	for get_date in one_week:
		if (get_date['date'] not in date_filter):
			date = get_date['date'].split('-')
			# print(date[2])
			date_filter.append((date[2], get_date['new_cases']))
	raw_data.close()
	

print(date_filter)
# for seven_days in range(-6, 0):
	# print(date_filter[seven_days])