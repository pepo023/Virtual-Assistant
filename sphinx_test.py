import speech_recognition as sr

r = sr.Recognizer()
with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source, duration=1)
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)

speech_text = r.recognize_sphinx(audio).lower().replace("'", "")
print("Sphinx: '" + speech_text + "'")

speech_text = r.recognize_google(audio).lower().replace("'", "")
print("Google: '" + speech_text + "'")

