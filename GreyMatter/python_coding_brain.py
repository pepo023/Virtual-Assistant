"""
This module provides the python coding workspace for the assistant. It enables the assistant to detect keywords
of the python language in a programing context. This module is very similar to the more abstract and general module
brain.py
"""
import os
from GreyMatter.SenseCells.tts import tts
from GreyMatter.SenseCells.stt import stt
from GreyMatter.SenseCells.assistant_sleep import hey_assistant
from GreyMatter.SpeechCodingAbilities.LanguageTypeConversations import list_conversations
from GreyMatter.general_conversations import goodbye


def python_coding_brain():

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

    tts("Python programing mode on!")

    """
    Prompt the user to what he/she wants to do
        Wait for a response for a certain amount of time
        If no response is present turn off the assistant
    """

    tts("Prompt me!")
    speech_text = stt()

    stop_coding = 0     # Signals that the user doesn't want to code anymore

    while stop_coding == 0:

        # Shutdown assistant
        if check_message(['stop', 'coding']):
            stop_coding = 1     # The user doesn't want to code anymore

        elif check_message(['create', 'python', 'file']) or check_message(['new','python','file']):
            tts("Let's create a file")
            speech_text = ""    # Empty the string otherwise it will keep entering the same elif

        elif check_message(['create', 'list']):
            list_string = list_conversations.basic_list_conversation()
            PyFile = open(os.path.join('C:\\Users\\Pepo0\\Documents\\Python File Playground\\', 'PythonList.py'), 'w+')
            PyFile.write(list_string)
            PyFile.close()
            goodbye()
            exit(0)
        else:
            speech_text = hey_assistant()
