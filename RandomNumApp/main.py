import random
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout 

class MyRoot(BoxLayout):
    def __init__(self):
        super(MyRoot,self).__init__()
    def gennum(self):
        self.randnum.text=str(random.randint(0,10000))
class TestApp(App):

    def build(self):
        return MyRoot()

testapp=TestApp()
testapp.run()