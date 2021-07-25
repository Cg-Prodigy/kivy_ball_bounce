from kivy.app import App
from kivy.uix.widget import Widget
from kivy.metrics import dp
from kivy.graphics.vertex_instructions import Line, Rectangle, Ellipse
from kivy.properties import Clock


class WidgetBuild(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.rad = dp(50)
        self.dx = -1
        self.dy = -1
        with self.canvas:
            self.t_circle = Ellipse(pos=self.center, size=(self.rad, self.rad))
        Clock.schedule_interval(self.update_frames, 1/60)

    def on_size(self, *args):
        self.t_circle.pos = (self.center_x-self.rad/2,
                             self.center_y-self.rad/2)

    def update_frames(self, dt):
        x, y = self.t_circle.pos
        w, h = self.t_circle.size
        diff_x = self.width-(x+w)
        diff_y = self.height-(y+h)
        if diff_x < 0 or x < 0:
            self.dx = -self.dx
        if diff_y < 0 or y < 0:
            self.dy = -self.dy
        x += self.dx
        y += self.dy
        self.t_circle.pos = (x, y)


class MainApp(App):
    def build(self):
        return WidgetBuild()


MainApp().run()
