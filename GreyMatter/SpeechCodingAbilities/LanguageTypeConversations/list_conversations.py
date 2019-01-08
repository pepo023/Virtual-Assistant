from GreyMatter.SenseCells.tts import tts
from GreyMatter.SenseCells.stt import stt
from GreyMatter.SpeechProcessingTools.speech_manipulation import check_message
from GreyMatter import general_conversations


# List generating function
def list_func(list_name, elements_list):
    list_length = len(elements_list)

    if list_length == 0:
        my_list = list_name + " = []"
    elif list_length == 1:
        my_list = list_name + " = [" + elements_list[0] + "]"
    else:
        my_list = list_name + " = ["
        for i in range(list_length - 1):
            my_list += "'" + elements_list[i] + "'" + ", "
        my_list += "'" + elements_list[-1] + "'" + "]"
    return my_list


def basic_list_conversation():
    tts("What is the name of the list?")
    list_name = stt()
    tts("Append elements to the list or leave it empty?")
    list_elements_intent = stt()                                #  What the user wants to do
    if check_message(['empty'], list_elements_intent):
        tts("Creating empty list for you")
        elements_list = []
        return list_func(list_name, elements_list)

    elif check_message(['cancel', 'list'], list_elements_intent) or check_message(['erase', 'list'], list_elements_intent):
        tts("List not created!")
        empty_list = []
        return empty_list

    else:
        tts("Tell me the elements of your list")
        elements_string = stt()
        elements_list = elements_string.split()     # Separate the words in the string into a list of strings
        tts("I'll append that now")
        return list_func(list_name, elements_list)


