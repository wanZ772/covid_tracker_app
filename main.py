from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen
from kivymd.uix.card import MDCard
from kivy.utils import platform 
import requests
from datetime import date


api = requests.get('https://coronacache.home-assistant.io/corona.json').json()['features']

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
	
	def __init__(self):
		super().__init__()
		self.ids.screen_manager.current = 'global_screen'
		(self.ids[str(footer_buttons_outline[0])].icon) = footer_buttons[0]
		
		
		
		
		if (str(old_data[0]) != str(date.today())):
			if (str((old_data[1]) != str(get_total))):
				try:
					new_data = [str(date.today()), str(get_total), str(get_total - int(old_data[1]))]
					with open('old_data.log', 'w') as write_new_data:
						write_new_data.write(','.join(new_data))
						write_new_data.close()
					
					if (int(old_data[1]) - int(old_data[2]) > 0):
						with open('old_data.log', 'r') as new_data:
							today_confirm = new_data.read().split(',')
							self.ids.total_today.text = today_confirm[2]
				except:
					pass
		else:
			if (int(old_data[1]) - int(old_data[2]) > 0):
				self.ids.total_today.text = "{}".format(old_data[2])
		
		
		
		for fetch_data in range(len(covid_data)):
			self.ids[str(covid_data[fetch_data])].text = str(data[fetch_data])
			self.ids[str(global_covid_data[fetch_data])].text = str(global_data[fetch_data])
class MainApp(MDApp):
	def build(self):
		return MainFunction()
if ('__main__' == __name__):
	MainApp().run()
	