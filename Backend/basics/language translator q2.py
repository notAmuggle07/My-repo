from googletrans import Translator

def translate_to_english(sentence):
    try:
        translator = Translator()
        translated = translator.translate(sentence, src='auto', dest='en')
        return translated.text
    except Exception as e:
        return str(e)

sentence = input("Enter your sentence: ")

translated_text = translate_to_english(sentence)
print("This sentence translates to:", translated_text)