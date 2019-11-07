# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import kivy
kivy.require('1.0.6')

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.textinput import TextInput

class LoginScreen(AnchorLayout):
    
    def __init__(self,**kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.cols = 2
        self.add_widget(Label(text='User Name'))
        self.username = TextInput(multiline=False)
        self.add_widget(self.username)
        self.add_widget(Label(text='Password'))
        self.password = TextInput(multiline=False)
        self.add_widget(self.password)


class DBAJam(App):
    
    def build(self):
        return LoginScreen()

if __name__ == "__main__":
    DBAJam().run()

