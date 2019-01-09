from GreyMatter.SpeechCodingAbilities.PerceptronTraining import Perceptron_model
from GreyMatter.SenseCells import tts, stt
from GreyMatter.SpeechCodingAbilities.speech_manipulation import check_message
from GreyMatter.SpeechCodingAbilities.LanguageTypeConversations import python_module_importer_conv as py_miconv


def ml_model_trainer(PyFile):
    tts("Do you wish to import any python modules?")
    speech_text = stt()
    if check_message(['yes'], speech_text) or check_message(['of', 'course'], speech_text):
        PyFile.write(py_miconv.module_importer())           # Module importer returns the string for the intended module
        done_importing = False                              # Keeps track if the user wants to continue importing
        while done_importing:
            tts("Are you done importing?")
            speech_text = stt()
            if check_message(['yes'], speech_text):
                done_importing = True
            else:
                PyFile.write(py_miconv.module_importer())
    # Decide which ML model to implement
    tts("Which model you want to train?")
    speech_text = stt()


