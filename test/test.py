from kivy.app import App
from kivy.uix.screenmanager import Screen



class TestFunction(Screen):
	def remove_text(self):
		self.ids.main_layout.remove_widget(self.ids.remove_this)
	# def __init__(self):
		# super().__init__()
		# self.remove_widget(self.ids.remove_this)
		# self.add_widget(self.ids.remove_this)
class TestApp(App):
	def build(self):
		return TestFunction()
if ('__main__' == __name__):
	TestApp().run()