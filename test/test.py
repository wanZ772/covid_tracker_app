from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen
from kivy.utils import platform

if (platform == 'win'):
	from kivy.core.window import Window
	
	Window.size = (300,500)


class TestFunction(Screen):
	pass
class TestApp(MDApp):
	def build(self):
		return TestFunction()
if ('__main__' == __name__):
	 TestApp().run()