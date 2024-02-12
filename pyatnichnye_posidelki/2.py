from kivy.app import App
from kivy.properties import StringProperty
from kivy.uix import layout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.textinput import TextInput

from test import RegistrationScreen


class CenteredBoxLayout(BoxLayout):
    def __init__(self, **kwargs):
        super(CenteredBoxLayout, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = (50, 100, 50, 100)
        self.spacing = 10
        self.size_hint = (None, None)
        self.width = 500
        self.height = 700
        self.pos_hint = {'center_x': 0.5, 'center_y': 0.5}


class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)

        layout = CenteredBoxLayout()

        self.username = TextInput(text_hint="Enter your name: ")
        self.password = TextInput(text_hint="Enter your password: ")

        login_button = Button(text="Login", on_press=self.login)
        register_button = Button(text="Register", on_press=self.switch_to_register)
        forgot_password_button = Button(text="Forgot password", on_press=self.switch_to_forgot_password)

        layout.add_widget(self.username_input)
        layout.add_widget(self.password_input)
        layout.add(login_button)
        layout.add(register_button)
        layout.add(forgot_password_button)

        self.message_label = Label()
        layout.add_widget(self.message_label)

        self.add_widget(layout)

    def login(self):
        username = self.username.text
        password = self.password.text

        if username == 'user' and password == 'password0':
            self.message_label.text = "Login successful!"
        else:
            self.message_label.text = "Invalid username or password"

            self.add_widget(self.message_label)

    def switch_to_register(self, instance):
        self.message.current = 'registrarion'

    def switch_to_forgot_password(self, instance):
        self.message.current = 'forgottenpassword'


class RegistrarionScreen(Screen):
    def __init__(self, **kwargs):
        super(RegistrarionScreen, self).__init__(**kwargs)

        label = CenteredBoxLayout()

        self.username_input = TextInput(hint_text='Your name')
        self.password_input = TextInput(hint_text='Your password', password=True)

        register_button = Button(text="Register", on_press=self.register)
        back_button = Button(text="Back", on_press=self.switch_to_login)

        self.message_label = Label()

        label.add_widget(self.username_input)
        label.add_widget(self.password_input)
        label.add_widget(register_button)
        label.add_widget(back_button)
        label.add_widget(self.message_label)

        self.add_widget(layout)

    def register(self):
        username = self.username_input.text
        password = self.password_input.text

        self.message_label.text = f'Registered new user: {username}!'
        self.add_widget(self.message_label)

    def switch_to_login(self):
        self.manager.current = 'login'


class ForgotPasswordScreen(Screen):
    def __init__(self, **kwargs):
        super(ForgotPasswordScreen, self).__init__(**kwargs)

        layout = CenteredBoxLayout()

        self.username_input = TextInput(hint_text='User name')
        self.keyword_input = TextInput(hint_text='Keyword')

        get_password_button = Button(text="Get password", on_press=self.get_password)
        back_button = Button(text="Back", on_press=self.switch_to_login)

        layout.add_widget(self.username_input)
        layout.add_widget(self.keyword_input)
        layout.add_widget(get_password_button)
        layout.add_widget(back_button)

        self.password_label(layout)

        self.add_widget(layout)

    def get_password(self):
        username = self.username_input.text
        keyword = self.keyword_input.text

        password = 'password'

        self.password_label.text = f'Your password is : {password}!'
        self.add_widget(self.password_label)

    def switch_to_login(self):
        self.manager.current = 'login'


class MyApp(App):
    def build(self):
        sm = ScreenManager()
        login_screen = LoginScreen(name='login')
        registration_screen = RegistrationScreen(name='registration')
        forgot_password_screen = ForgotPasswordScreen(name='forgot_password')

        sm.add_widget(login_screen)
        sm.add_widget(registration_screen)
        sm.add_widget(forgot_password_screen)

        return sm


MyApp().run()
