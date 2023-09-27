from googletrans import Translator, LANGUAGES

def translate(sentence, dest_lang):
    try:
        translator = Translator()
        translated = translator.translate(sentence, src='auto', dest=dest_lang)
        return translated.text
    except Exception as e:
        return str(e)
    
sentence = input("Enter your sentence: ")
dest_lang = input("Enter the language code for the preferred language: ")

if dest_lang in LANGUAGES:
    print("This sentence in",LANGUAGES[dest_lang].capitalize(),"is:",translate(sentence,dest_lang))
else:
    print("This library does not support",dest_lang)