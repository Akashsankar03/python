from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.app import MDApp

class HelloScreen(Screen):
    pass

class HelloApp(MDApp):
    def build(self):
        # Load the KV file
        return Builder.load_file('hello.kv')

if __name__ == '__main__':
    HelloApp().run()
