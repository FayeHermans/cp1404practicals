"""
Prac 06: Languages
Est time: 15min
Start time: 6:50pm
Finnish time:
"""

from prac_06.programming_language import ProgrammingLanguage

python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
print(python)

programming_languages = [python, ruby, visual_basic]
print("The dynamically typed languages are:")
for item in programming_languages:
    if item.is_dynamic():
        print(item.name)
