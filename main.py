from kivy.app import App
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout

kv = Builder.load_file("guessing.kv")

class GuessingApp(App):
    def build(self):
        return FloatLayout()

if __name__ == "__main__":
    GuessingApp().run()