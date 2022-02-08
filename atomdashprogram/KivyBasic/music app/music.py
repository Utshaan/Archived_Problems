import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label
from kivy.uix.popup import Popup

class Menu(Screen):
    pass

class Scales(Screen):
    pass

class Chords(Screen):
    pass

class P(FloatLayout):
    pass

class Widgets(Widget):
    def btn(self):
        show_popup()


def show_popup():
    show = P()

    popupwindow = Popup(title="popup window", content=show, size_hint=(None, None), size=(400,500))

    popupwindow.open()

kv = Builder.load_file("music.kv")

class Music(App):
    def build(self):
        return Widgets()

if __name__ == "__main__":
    Music().run()