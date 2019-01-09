from GreyMatter.SenseCells import stt, tts
from GreyMatter.SpeechProcessingTools.speech_manipulation import check_message

def module_importer():
    tts("Which module?")
    speech_text = stt()
    if check_message(['pandas'], speech_text):
        tts("Got it!")
        return "import pandas as pd"
    elif check_message(['numpy'], speech_text):
        tts("Got it!")
        return "import numpy as np"
    elif check_message(['a', 'module', 'from', 'math', 'plot', 'library'], speech_text):
        tts("Which module?")
        speech_text = stt()
        if check_message(['python', 'plot'], speech_text):
            tts("Got it!")
            return "import matplotlib.pyplot as plt"
        elif check_message(['colors'], speech_text):
            tts("Got it!")
            return "from matplotlib.colors import ListedColormap"
        else
            return "nothing_imported"
    else
        return "nothing_imported"