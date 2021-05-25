import csv, requests

get_data = requests.get('https://raw.githubusercontent.com/wnarifin/covid-19-malaysia/master/covid-19_my_state.csv').content

with open('data.csv', 'wb') as write_data:
	write_data.write(get_data)
	write_data.close()