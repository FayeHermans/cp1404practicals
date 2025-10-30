"""
CP1404 Practical 05
Hexadecimal colour lookup
"""

COLOUR_CODES = {"aquamarine": "#7fffd4", "bitter lemon": "#cae00d", "cadmium green": "#006b3c",
                "caribbean green": "#00cc99", "coral": "#ff7f50", "corn": "#fbec5d", "cotton candy": "#ffbcd9",
                "dandelion": "#f0e130", "deep jungle green": "#004b49", "glossy grape": "#ab92b3"}
# I had a little too much fun picking colours :)

colour_name = input("Enter a colour: ").lower()
while colour_name != "":
    print(f"{colour_name}'s colour code is {COLOUR_CODES.get(colour_name)}")
    colour_name = input("Enter a colour: ").lower()
