from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.factory import Factory
from kivy.properties import ObjectProperty
from kivy.lang import Builder, Parser, ParserException
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.graphics import Color,Line,Rectangle
from kivy.uix.textinput import TextInput
from kivy.properties import NumericProperty
import math
from functools import partial
                                                                 
DS_ROOT = os.path.dirname(__file__)

DS_KVS = os.path.join(DS_ROOT,'ds_kvs')
DS_CLASSES = [c[:-3] for c in os.listdir(DS_KVS)

class Root(FloatLayout):
	screen_manager = ObjectProperty(None)	
	child = ObjectProperty(None) 

	def change_kv(self,*largs):
		child = self.screen_manager.current_screen.children[0]
		with open(child.kv_file, 'rb') as file:
			text = file.read().decode('utf8')
		kv_container = self.screen_manager.current_screen
		try:
			parser = Parser(content = txt)
			kv_container.clear_widgets()
			widget = Factory.get(parser.root.name)()
			Builder._apply_rule(widget,parser.root,parser.root)
			kv_container.add_widget(widget)
		except (SyntaxError, ParserException) as e:
			self.show_error(e)
		except Exception as e:
			self.show_error(e)	 

class DS(App):
	pass

Factory.register('Root', cls=Root)
	
if __name__=='__main__':
    DS().run()
