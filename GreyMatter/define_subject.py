import re   # Regular expressions module
import wikipedia
from GreyMatter.SenseCells.tts import tts

def define_subject(speech_text):
    words_of_message = speech_text.split()
    words_of_message.remove('define')
    cleaned_message = ' '.join(words_of_message)

    try:
        wiki_data = wiki_data.replace("'","")
        tts(wiki_data)
    except wikipedia.exceptions.DisambiguationError as e:
        tts('Can you please be more specific? You may'
            ' choose something from the following.')
        print("Can you please be more specific? You may choose something"
              "from the following.; {0}".format(e))