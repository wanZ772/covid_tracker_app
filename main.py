from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen
from kivymd.uix.card import MDCard
from kivy.garden.graph import LinePlot, Graph
from random import randrange
from kivy.uix.button import Button
from kivy.utils import platform 
import requests
from datetime import date
from threading import Thread
from time import sleep



api = requests.get('https://coronacache.home-assistant.io/corona.json').json()['features']
states = requests.get('https://api.azanpro.com/zone/states.json').json()['states']


global_confimed,global_deaths,global_recover,global_active = 0,0,0,0
for global_data in range(len(api)):
	
	global_confimed = global_confimed + (api[global_data]['attributes']['Confirmed'])
	global_deaths = global_deaths + (api[global_data]['attributes']['Deaths'])
	try:
		global_active = global_active + (api[global_data]['attributes']['Active'])
		global_recover = global_recover + (api[global_data]['attributes']['Recovered'])
	except:
		pass
global_data = [global_confimed,global_deaths,global_recover,global_active]

for i in api:
	if (i['attributes']['OBJECTID'] == 109):
		get_total = i['attributes']['Confirmed']
		get_deaths = i['attributes']['Deaths']
		get_recover = i['attributes']['Recovered']
		get_active = i['attributes']['Active']
		get_tested = i['attributes']['People_Tested']
		get_hospitalized = i['attributes']['People_Hospitalized']
		get_ir = i['attributes']['Incident_Rate']
		get_mr = i['attributes']['Mortality_Rate']

data = [get_total, get_deaths, get_recover, get_active]

with open('old_data.log', 'r') as old_data_file:
	old_data = old_data_file.read().split(',')
	old_data_file.close()

if (platform == 'win'):
	from kivy.core.window import Window
	Window.size = (300,500)

footer_buttons_outline = [
		'view-dashboard-outline',
		'newspaper-variant-outline',
		'menu',
		'chart-line',
		'database-refresh',
		'information-outline'
	]
footer_buttons = [
		'view-dashboard',
		'newspaper-variant',
		'xbox-controller-menu',
		'chart-line-stacked',
		'database-refresh',
		'information'
	]

covid_data = ['total', 'active', 'recovered', 'deaths']
global_covid_data = ['global_total', 'global_active', 'global_recovered', 'global_deaths']


class MainFunction(Screen):
	def refresh_database(self):
		with open('data.csv', 'w') as write_database:
			write_database.write(requests.get('https://raw.githubusercontent.com/wnarifin/covid-19-malaysia/master/covid-19_my_state.csv').text)
			write_database.close
		self.ids.refresh_status.icon = 'database-check'
		self.ids['database-refresh'].icon = 'database-check'
		sleep(1)
		self.ids.screen_manager.current = 'global_screen'
	def on_touch_move(self, move):
		if ((self.ids.screen_manager.current == 'global_screen') or (self.ids.screen_manager.current == 'local_screen')):
			if (move.x < move.ox):
				self.ids.screen_manager.current = 'local_screen'
				self.ids.screen_manager.transition.direction = 'left'
				
				self.ids.local_button.text_color = (230/255,0,0,1)
				self.ids.global_button.text_color = (105/255,105/255,105/255,1)
				self.ids.local_button.text = "[b]Local[/b]"
				
				self.ids.global_button.text = "Global"
				
				
				self.ids.local_button.font_size = '20sp'
				self.ids.global_button.font_size = '15sp'
				
				
			elif (move.x > move.ox):
				self.ids.screen_manager.current = 'global_screen'
				self.ids.screen_manager.transition.direction = 'right'
				
				self.ids.global_button.text_color = (230/255,0,0,1)
				self.ids.local_button.text_color = (105/255,105/255,105/255,1)
				
				
				self.ids.local_button.text = "Local"
				self.ids.global_button.text = "[b]Global[/b]"
				self.ids.local_button.font_size = '15sp'
				self.ids.global_button.font_size = '20sp'
			
	
	def change_statistics(self, get_target):
		if (get_target == 1):
			self.ids.screen_manager.current = 'local_screen'
			self.ids.screen_manager.transition.direction = 'left'
			
			self.ids.local_button.text_color = (230/255,0,0,1)
			self.ids.global_button.text_color = (105/255,105/255,105/255,1)
			self.ids.local_button.text = "[b]Local[/b]"
			
			self.ids.global_button.text = "Global"
			
			
			self.ids.local_button.font_size = '20sp'
			self.ids.global_button.font_size = '15sp'
		else:
			self.ids.screen_manager.current = 'global_screen'
			self.ids.screen_manager.transition.direction = 'right'
			
			self.ids.global_button.text_color = (230/255,0,0,1)
			self.ids.local_button.text_color = (105/255,105/255,105/255,1)
			
			
			self.ids.local_button.text = "Local"
			self.ids.global_button.text = "[b]Global[/b]"
			self.ids.local_button.font_size = '15sp'
			self.ids.global_button.font_size = '20sp'
	def highlight_button(self, get_button):
		for i in range(6):
			self.ids[str(footer_buttons_outline[i])].icon = footer_buttons_outline[i]
		self.ids[str(footer_buttons_outline[get_button])].icon = footer_buttons[get_button]
		
		if (get_button != 0):
			self.remove_widget(self.ids.statistic_mode)
			
			if (get_button == 2):
				self.ids.cases_by_states.clear_widgets()
				for i in states:
					self.ids.cases_by_states.add_widget(
							Button(
									text = "{}: Null".format(i)
								)
						)
			elif (get_button == 3):
				self.ids.chart_for_week.clear_widgets()
				total_cases = [6976,6509,7289,7478,7857,8290,9020]
				days = []
				
				day = "{}".format(date.today()).split('-')
				
				minus_day = 7
				
				for minus in range(0,7):
					days.append(int(day[2]) - minus)
				days = sorted(days)
				print(days)
				
				
				graph = Graph(ylabel = "X1000", xlabel = "Month: {}".format(day[1]), x_ticks_major = 1, y_ticks_minor = 1, y_ticks_major = 1, 
				  y_grid_label=True, x_grid_label=True, padding=5, x_grid=True, y_grid=True, 
				  xmin=days[0], xmax=days[6], ymin=1, ymax=10)
			
				plot = LinePlot(line_width = 1, color=[1, 0, 0, 1])
				
				
				pointers = []
				
				for i in range(len(days)):
					print(total_cases[i] / 1000)
					pointers.append((days[i], total_cases[i] / 1000))
				plot.points = pointers
				
				
				graph.add_plot(plot)
				self.ids.chart_for_week.add_widget(graph)
					
					
			elif (get_button == 4):
				print(1)
				Thread(target = self.refresh_database).start()
		else:
			self.add_widget(self.ids.statistic_mode)
			

	def test(self):
		pass
	def __init__(self):
		super().__init__()
		
		
		self.ids.screen_manager.current = 'global_screen'
		(self.ids[str(footer_buttons_outline[0])].icon) = footer_buttons[0]
		
		
		
		
		# if (str(old_data[0]) != str(date.today())):
		if (str(old_data[1]) != str(get_total)):
			new_data = [str(date.today()), str(get_total), str(get_total - int(old_data[1]))]
			
			
			with open('old_data.log', 'w') as write_new_data:
				write_new_data.write(','.join(new_data))
				write_new_data.close()
			with open('old_data.log', 'r') as new:
				new_total_today = new.read().split(',')
				new.close()
				
				
			if (get_total != int(new_total_today[2])):
				self.ids.total_today.text = new_total_today[2]
				self.ids.total_today_detail.text = new_total_today[2]
		else:
			if (old_data[1] != old_data[2]):
				self.ids.total_today.text = old_data[2]
				self.ids.total_today_detail.text = old_data[2]
		
		self.ids.last_date.text = old_data[0]
		
		self.ids.total_detail.text = old_data[1]
		self.ids.active_detail.text = str(get_active)
		self.ids.recovered_detail.text = str(get_recover)
		self.ids.people_tested.text = str(get_tested)
		self.ids.people_hospitalized.text = str(get_hospitalized)
		self.ids.death_detail.text = str(get_deaths)
		self.ids.incident_rate.text = str(get_ir)
		self.ids.mortality_rate.text = str(get_mr)
		


			
			
		
		for fetch_data in range(len(covid_data)):
			self.ids[str(covid_data[fetch_data])].text = str(data[fetch_data])
			self.ids[str(global_covid_data[fetch_data])].text = str(global_data[fetch_data])

		


class MainApp(MDApp):
	def build(self):
		return MainFunction()
if ('__main__' == __name__):
	MainApp().run()
	
