"""
CP1404 Prac 08
GUI program to convert miles to km.
"""

from kivy.app import App
from kivy.lang import Builder

MILES_TO_KM = 1.60934

class MilesConverterApp(App):
    """ MilesConverterApp is a Kivy App for converting miles to kilometres """
    def build(self):
        """ build the Kivy app from the kv file """
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_calculate(self):
        """Convert the user input from miles to km """
        km_value = int(self.root.ids.input_miles.text) * MILES_TO_KM
        self.root.ids.output_label.text = str(km_value)




MilesConverterApp().run()
