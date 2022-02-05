
from kivy.core.window import Window
from kivy.config import Config
from kivy.properties import Clock, StringProperty, BooleanProperty

# Config.set('input', 'mouse', 'mouse,multitouch_on_demand')
# Window.size = (960, 600)
# Window.minimum_width, Window.minimum_height = Window.size

from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition, FallOutTransition, WipeTransition, \
    SwapTransition, FadeTransition, SlideTransition
from kivy.uix.label import Label
from kivy import utils
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

from time import *


class MyScreenManager(ScreenManager):
    def __init__(self, **kwargs):
        super(MyScreenManager, self).__init__(**kwargs)


class DisplayTime(Screen):
    my_time = StringProperty("")

    def __init__(self, **kwargs):
        super(DisplayTime, self).__init__(**kwargs)
        self.my_time = str(strftime("%H:%M:%S"))

        Clock.schedule_interval(self.update_time, 1)

    def update_time(self, dt):
        # print(strftime("%H:%M:%S"))
        self.my_time = str(strftime("%H:%M:%S"))


class Menu(Screen):
    pass


class SettingsScreen(Screen):

    def __init__(self, **kwargs):
        super(SettingsScreen, self).__init__(**kwargs)
        self.display_on_off = True


class Screen3(Screen):
    pass


class RootBoxLayout(BoxLayout):
    def __init__(self, **kwargs):
        super(RootBoxLayout, self).__init__(**kwargs)

    def change_back(self, widget: Button, label: Label):
        widget.background_color = 1, 1, 1, .6
        label.color = 1, 1, 1, .4
        print("Hello")

    def change_back2(self, widget: Button, label: Label):
        widget.background_color = 1, 1, 1, 0
        color = utils.get_color_from_hex("#dedddc")
        label.color = color


class TimeApp(App):

    display_on_off = BooleanProperty()

    def __init__(self, **kwargs):
        super(TimeApp, self).__init__(**kwargs)
        self.display_on_off = True

    def activate_display(self):
        if self.display_on_off:
            self.display_on_off = False
        else:
            self.display_on_off = True
        print(self.display_on_off)

    def build(self):
        sm = MyScreenManager(transition=FadeTransition())
        sm.add_widget(DisplayTime(name="displaytime"))
        sm.add_widget(Menu(name="menu"))
        sm.add_widget(SettingsScreen(name="settings"))

        return sm


if __name__ == "__main__":
    TimeApp().run()
