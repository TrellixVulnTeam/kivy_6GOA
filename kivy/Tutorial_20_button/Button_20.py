   # we do not need to all the file in kvy just two and three file is enough
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.core.window import Window
# set the app size
# Window.size=(500,700)


Builder.load_file('calc.kv')
# create the new class and inherit the Layout

class MyLayout(Widget):
    pass

class CalculatorApp(App):
    def build(self):
        return MyLayout()


if __name__=='__main__':
    CalculatorApp().run()