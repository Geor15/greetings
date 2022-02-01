from greets import greetings
from translate import Translator

translator =Translator(to_lang="ru")

for greet in greetings:
    print(translator.translate(greet).capitalize())