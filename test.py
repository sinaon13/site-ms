from kivy.app import App

from kivy.uix.button import  Button

from kivy.uix.textinput import TextInput

from kivy.uix.boxlayout import BoxLayout
from threading import Thread
def f1():
    Part1_Box1___main_Buttons___().run()

def f2():
    Part2_Box2___Buttons_OnPresses___().run()

class Part1_Box1___main_Buttons___(App):
    def build(self):
        
        self.box.add_widget(Button(text = "Add Button", size_hint = (.1, .1)))
        self.box.add_widget(Button(text = "Add TextBox", size_hint = (.1, .1), on_press = Part2_Box2___Buttons_OnPresses___().func1))
        self.box.add_widget(Button(text = "Add Label", size_hint = (.1, .1)))
        self.box.add_widget(Button(text = "Delete Item", size_hint = (.1, .1)))
        self.box.add_widget(Button(text = "Save", size_hint = (.1, .1)))
        return self.box

class Part2_Box2___Buttons_OnPresses___(App):
    def build(self):
        self.box = BoxLayout(size_hint = (5, 5))
        return self.box

    def func1(self, instance):
        self.box.add_widget(TextInput(text = "", size_hint = (.5, .5), pos = (100, 100)))
        return self.box

Thread(target = f1).start()
Thread(target = f2).start()
