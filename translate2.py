from langdetect import detect
from googletrans import Translator

# detected_language= detect("hello how are you?")
# print(detected_language)
sentence=str(input("say....."))

detected_language= detect(sentence)
#print(detected_language)


translator = Translator()

#Reference for IS0-639-1 codes
#https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes
translated_sentence = translator.translate(sentence,src=detected_language,dest='kn')



print(translated_sentence.text)