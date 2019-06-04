from translate import Translator
translator= Translator(to_lang="Spanish")
translation = translator.translate("hi, my name is prasad, what yours")
print(translation)

translator= Translator(from_lang="Spanish",to_lang="English")
translation = translator.translate(translation)
print(translation)