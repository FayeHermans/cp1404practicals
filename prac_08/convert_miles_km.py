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
        miles_value = self.valid_number()
        km_value = miles_value * MILES_TO_KM
        self.root.ids.output_label.text = str(km_value)

    def handle_increment(self, change):
        """Pressing buttons will add or subtract '1' from input """
        new_value = float(self.root.ids.input_miles.text) + change
        self.root.ids.input_miles.text = str(new_value)

    def valid_number(self):
        """Check if input is valid number """
        try:
            value = float(self.root.ids.input_miles.text)
            return value
        except TypeError:
            return 0.0

MilesConverterApp().run()
