import psycopg2
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label


conn = psycopg2.connect(dbname="1", host="127.0.0.1", user="postgres", password="1", port="5433")
cur = conn.cursor()

cur.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY,
        username VARCHAR(50),
        password VARCHAR(50)
    )
''')
conn.commit()


class CenteredBoxLayout(BoxLayout):
    def __init__(self, **kwargs):
        super(CenteredBoxLayout, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = [50, 100, 50, 100]
        self.spacing = 10
        self.size_hint = (None, None)
        self.width = 600  # ширина окна
        self.height = 400  # высота окна
        self.pos_hint = {'center_x': 0.5, 'center_y': 0.5}


class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.login_button_pressed = False

        layout = CenteredBoxLayout()

        self.username_input = TextInput(hint_text='Ваше имя', size_hint=(1, 2.75))
        self.password_input = TextInput(hint_text='Ваш пароль', size_hint=(1, 2.75))

        login_button = Button(text='Войти', on_press=self.login, size_hint=(1, 1.75))
        register_button = Button(text='Зарегистрироваться', on_press=self.switch_to_registration,  size_hint=(1, 1.75))

        layout.add_widget(self.username_input)
        layout.add_widget(self.password_input)
        layout.add_widget(login_button)
        layout.add_widget(register_button)

        self.message_label = Label()
        layout.add_widget(self.message_label)  # Add the message_label to the layout

        self.add_widget(layout)

    def login(self, instance):
        username = self.username_input.text
        password = self.password_input.text

        try:
            conn = psycopg2.connect(
                dbname="1",
                user="postgres",
                password="1",
                host="127.0.0.1",
                port="5433"
            )
            cur = conn.cursor()
            cur.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
            user = cur.fetchone()

            if user is not None:
                self.message_label.text = f'Успешный вход для пользователя: {username}'
            else:
                self.message_label.text = 'Неправильное имя пользователя или пароль'
        except psycopg2.Error as e:
            self.message_label.text = f'Произошла ошибка: {e}'
        finally:
            if conn:
                conn.close()

        if self.message_label.parent:
            self.message_label.parent.remove_widget(self.message_label)

        self.add_widget(self.message_label)

    def switch_to_registration(self, instance):
        self.manager.current = 'registration'

    def switch_to_forgot_password(self, instance):
        self.manager.current = 'forgot_password'  # переключаемся на экран восстановления пароля


class RegistrationScreen(Screen):
    def __init__(self, **kwargs):
        super(RegistrationScreen, self).__init__(**kwargs)

        layout = CenteredBoxLayout()

        self.username_input = TextInput(hint_text='Username', multiline=False, size_hint=(1, 2.75))
        self.password_input = TextInput(hint_text='Password', password=True, multiline=False, size_hint=(1, 2.75))

        register_button = Button(text='Register', on_press=self.register, size_hint=(1, 1.75))
        back_button = Button(text='Back to Login', size_hint=(1, 1.75))
        back_button.bind(on_press=self.switch_to_login)  # Bind the on_press event to the switch_to_login method

        self.message_label = Label()  # Create message_label here

        layout.add_widget(self.username_input)
        layout.add_widget(self.password_input)
        layout.add_widget(register_button)
        layout.add_widget(back_button)
        layout.add_widget(self.message_label)

        self.add_widget(layout)

    def switch_to_login(self, instance):
        self.manager.current = 'login'

    def register(self, instance):
        username = self.username_input.text
        password = self.password_input.text

        try:
            conn = psycopg2.connect(
                dbname="1",
                user="postgres",
                password="1",
                host="127.0.0.1",
                port="5433"
            )
            cur = conn.cursor()
            cur.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
            conn.commit()
            self.message_label.text = f'Новый пользователь зарегистрирован: {username}'
        except psycopg2.Error as e:
            self.message_label.text = f'Произошла ошибка: {e}'
        finally:
            if conn:
                conn.close()

        if self.message_label.parent:
            self.message_label.parent.remove_widget(self.message_label)

        self.add_widget(self.message_label)


class MyApp(App):
    def build(self):
        sm = ScreenManager()
        login_screen = LoginScreen(name='login')
        registration_screen = RegistrationScreen(name='registration')

        sm.add_widget(login_screen)
        sm.add_widget(registration_screen)

        return sm


MyApp().run()
