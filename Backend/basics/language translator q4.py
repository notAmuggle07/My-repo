from googletrans import Translator, LANGUAGES

sentence = input("Enter your sentence: ")
translator = Translator()
translated = translator.translate(sentence, src='auto', dest='en')
print("This sentence is in:",LANGUAGES[translated.src].capitalize())