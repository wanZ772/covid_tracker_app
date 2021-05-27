from kivy.app import App
from math import cos
from kivy.garden.graph import Graph, MeshLinePlot
from random import randrange
from kivy.uix.screenmanager import Screen

total_cases = [6493,6320,6976,6509,7289,7478,7857]
days = [0,2,3,4,5,6]

class TestFunction(Screen):
		def show_graph(self):
			graph = Graph(x_ticks_major = 1, y_ticks_minor = 1, y_ticks_major = 1, 
				  y_grid_label=True, x_grid_label=True, padding=5, x_grid=True, y_grid=True, 
				  xmin=1, xmax=7, ymin=0, ymax=10)
			
			plot = MeshLinePlot(color=[1, 0, 0, 1])
			
			
			pointers = []
			
			for i in days:
				print(total_cases[i] / 1000)
				pointers.append((i, total_cases[i] / 1000))
			plot.points = pointers
			
			
			graph.add_plot(plot)
			self.ids.show_here.add_widget(graph)
	
class TestApp(App):
	def build(self):
		# graph = Graph(x_ticks_major = 1, y_ticks_minor = 1, y_ticks_major = 1, 
                  # y_grid_label=True, x_grid_label=True, padding=5, x_grid=True, y_grid=True, 
                  # xmin=1, xmax=7, ymin=0, ymax=10)
		
		# plot = MeshLinePlot(color=[1, 0, 0, 1])
		
		
		# pointers = []
		
		# for i in days:
			# print(total_cases[i] / 1000)
			# pointers.append((i, total_cases[i] / 1000))
		# plot.points = pointers
		
		
		# graph.add_plot(plot)
		# return(graph)
		# print(sin(80 / 10.))
		return TestFunction()
if ('__main__' == __name__):
	TestApp().run()