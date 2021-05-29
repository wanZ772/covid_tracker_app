import csv

date_filter = []

with open('data.csv', 'r') as raw_data:
	data = csv.DictReader(raw_data)
	
	for check_date in data:
		if (check_date['date'] not in date_filter):
			date_filter.append(check_date['date'])
		else:
			pass
			
	raw_data.close()
	
with open('data.csv', 'r') as raw_data:
	data = csv.DictReader(raw_data)
	
	for retrive_data in data:
		if (retrive_data['date'] == date_filter[-1]):
			state = retrive_data['state'].replace('WP ', '')
			print(retrive_data['state'].replace('WP ', ''), retrive_data['new_cases'])