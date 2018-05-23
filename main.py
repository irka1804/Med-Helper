from kivy.app import App
from KivyCalendar import CalendarWidget
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
import pymongo

patient = {
            "name":"lf	"
          , "surname":""
          , "localization":{
                  "temporal":False
                , "frontal":False
                , "hindhead":False
                }
          , "nature":{
                  "throbbing":False
                , "constant":False
                }
          , "appearance": {"d":0, "m":0, "y":0}
          }
coll = 0

class PatientScreen(Screen):
    def set_name(self):
        global coll, patient
        patient["name"] = self.ids.name.text
        patient["surname"] = self.ids.surname.text

class SymptomScreen(Screen):
    pass


class SaveScreen(Screen):
    def save(self):
        coll.insert_one(patient)

class My_manager(ScreenManager):
    def set_symptom(self, s):
        global patient
        local_ids = self.ids[s].ids
        obj = self.ids[s]
        for i in local_ids:
            try:
                patient[s][i] = obj.ids[i].text
                continue
            except:
                pass
            try:
                patient[s][i] = obj.ids[i].active
                continue
            except:
                pass
            try:
                date = obj.ids[i].active_date
                patient[s]['d'] = date[0]
                patient[s]['m'] = date[1]
                patient[s]['y'] = date[2]
            except:
                print("Error in writing values")


class MedHelperApp(App):
    def build(self):
        conn = pymongo.MongoClient('localhost', 27017)
        db = conn.db
        global coll 
        coll = db.patients
        return My_manager()


if __name__ == '__main__':
    MedHelperApp().run()
