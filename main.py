from kivy.app import App
from KivyCalendar import DatePicker
from kivy.uix.screenmanager import ScreenManager, Screen

class PatientScreen(Screen):
    pass

class SymptomScreen(Screen):
    pass

class SaveScreen(Screen):
    pass

class My_manager(ScreenManager):
    pass

class MedHelperApp(App):
    def build(self):
        return My_manager()


if __name__ == '__main__':
    MedHelperApp().run()
