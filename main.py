from kivy.app               import App
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.behaviors     import ButtonBehavior
from kivy.lang.builder      import Builder
from kivymd.app             import MDApp
from kivymd.uix.screen      import Screen 
from kivymd.uix.label       import MDLabel, MDIcon 
from kivymd.theming         import ThemeManager
from kivymd.uix.button      import MDRoundFlatButton
from kivy.properties        import ObjectProperty
from kivy.uix.boxlayout     import BoxLayout
from kivy.uix.scrollview    import ScrollView
from kivy.core.text         import LabelBase
#from minha_materia          import meu_texto
class MyMainWidget(ScreenManager):
    pass

class Menu(Screen):
    pass

class Introducao(Screen):
    def voltar(self):
        MDApp.get_running_app().root.current = "menu"

class Calculadora(Screen):
    def voltar(self):
        MDApp.get_running_app().root.current = "menu"

class Exercicios(Screen):
    def voltar(self):
        MDApp.get_running_app().root.current = "menu"

class MainApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Red"
        self.theme_cls.primary_hue ="A700"
        Builder.load_string(open('main.kv', encoding = "utf-8").read())
        return MyMainWidget()
        

MainApp().run()