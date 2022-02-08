import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import  ObjectProperty

class MainWindow(Screen):
    password = ObjectProperty(None)
    
    def clear(self):
        self.password.text = ""
class SecondWindow(Screen):
    pass

class WindowManager(ScreenManager):
    pass
kv = Builder.load_file("cool.kv")

class CoolsApp(App):
    def build(self):
        return kv


if __name__ == "__main__":
    CoolsApp().run()