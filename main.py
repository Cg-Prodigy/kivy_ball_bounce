from kivy.app import App
from kivy.uix.widget import Widget
from kivy.metrics import dp
from kivy.graphics.vertex_instructions import Line, Rectangle, Ellipse
from kivy.graphics.context_instructions import Color
from kivy.properties import Clock
import random
from kivy.utils import rgba
from kivy.core.window import Window, window_info


class WidgetBuild(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.rad = dp(100)
        self.dx, self.dy = 2, 2
        with self.canvas:
            self.circle = Ellipse(pos=(self.center_x, self.center_y),
                                  size=(self.rad, self.rad))
            Clock.schedule_interval(self.animate, 1/60)

    def on_size(self, *args):
        self.circle.pos = (self.center_x-self.rad/2, self.center_y-self.rad/2)

    def animate(self, dt):
        x, y = self.circle.pos
        w, h = self.circle.size
        diff_x = self.width-(x+w)
        diff_y = self.height-(y+h)
        if diff_x < 0 or x < 0:
            self.dx *= -1
        if diff_y < 0 or y < 0:
            self.dy *= -1
        x += self.dx
        y += self.dy
        self.circle.pos = (x, y)


class MainApp(App):
    Window.clearcolor = (.4, .4, .4, 1)

    def build(self):
        return WidgetBuild()


MainApp().run()
