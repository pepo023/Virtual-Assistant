import speech_recognition as sr
# from GreyMatter.SenseCells.tts import tts


def stt():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)

    try:
        speech_text = r.recognize_google(audio).lower().replace("'", "")
        print("Melissa thinks you said '" + speech_text + "'")
        return speech_text
    except sr.UnknownValueError:
        print("Melissa could not understand audio")
        return "no prompt"    # Return this to indicate that no message was received.
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition\
        service {0}".format(e))
        exit(0)


def check_message(check):
    """"
    This function checks if the items in the list (specified in argument) are
    present in the user's input speech. Is "check" a subset of the user's input?
    """
    words_of_message = speech_text.split()  # separate input string into list of strings
    if set(check).issubset(set(words_of_message)):  # set removes any duplicates from word list
        return True
    else:
        return False
