from kivy.app import App

from kivy.uix.button import  Button

from kivy.uix.textinput import TextInput

from kivy.uix.boxlayout import BoxLayout

class Box1___main_Buttons___(App):
    def build(self):
        self.box = BoxLayout(size_hint = (1, 1), spacing = (20))
        self.box.add_widget(Button(text = "Add Button", size_hint = (.1, .1)))
        self.box.add_widget(Button(text = "Add TextBox", size_hint = (.1, .1)))
        self.box.add_widget(Button(text = "Add Label", size_hint = (.1, .1)))
        self.box.add_widget(Button(text = "Delete Item", size_hint = (.1, .1)))
        self.box.add_widget(Button(text = "Save", size_hint = (.1, .1)))
        return self.box
Box1___main_Buttons___().run()
