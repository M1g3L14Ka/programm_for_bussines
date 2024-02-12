from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen


class LoginWindow(Screen):
    pass


class AuthScreen(Screen):
    pass


class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(LoginWindow(name="LoginScreen"))
        sm.add_widget(AuthScreen(name="AuthScreen"))

        return sm

    s


MyApp().run()
