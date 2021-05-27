from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen
from kivymd.uix.card import MDCard
from matplotlib import pyplot
from random import randrange
from kivy.uix.button import Button
from kivy.utils import platform 
import requests
from datetime import date



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
	if (i['attributes']['OBJECTID'] == 108):
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
		'database-outline',
		'information-outline'
	]
footer_buttons = [
		'view-dashboard',
		'newspaper-variant',
		'microsoft-xbox-controller-menu',
		'chart-line-stacked',
		'database',
		'information'
	]

covid_data = ['total', 'active', 'recovered', 'deaths']
global_covid_data = ['global_total', 'global_active', 'global_recovered', 'global_deaths']


class MainFunction(Screen):
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
				total_cases = []
				week_day = []
				day = "{}".format(date.today()).split('-')
				minus_day = 7
				
				
				for i in range(7):
					week_day.append("{}/{}".format(int(day[2]) - minus_day, day[1]))
					total_cases.append(randrange(1000, 10000))
					minus_day -= 1
				
				pyplot.plot(week_day,total_cases, linestyle = 'dashed', marker = '*', markerfacecolor = 'blue', color = 'red')
				pyplot.savefig('week.png')
				
				self.ids.chart_for_week.source = 'week.png'
					
					
			
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
	