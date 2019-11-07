import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Color
from kivy.graphics import Ellipse
from kivy.graphics import Line
from random import random
from kivy.uix.button import Button

class MyPaintWidget(Widget):
    def on_touch_down(self, touch):
        with self.canvas:
            Color(random(), random(), random())
            d = 10.
            Ellipse(pos=(touch.x - d / 2, touch.y - d / 2), size=(d, d))
            touch.ud['line'] = Line(points=(touch.x, touch.y))
            
            print(touch)
    
    def on_touch_move(self,touch):
        touch.ud['line'].points += [touch.x, touch.y]
        
        print(touch.ud['line'].points)
    

class MyPaintApp(App):
    
    def build(self):
        parent = Widget()
        self.painter = MyPaintWidget()
        clearbtn = Button(text='Clear')
        clearbtn.bind(on_release=self.clear_canvas)
        parent.add_widget(self.painter)
        parent.add_widget(clearbtn)
        return parent
    
    def clear_canvas(self,obj):
        self.painter.canvas.clear()
    
if __name__ == '__main__':
    MyPaintApp().run()