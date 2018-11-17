from GreyMatter import general_conversations
from GreyMatter import tell_time
from GreyMatter import define_subject


def brain(name, speech_text):

    def check_message(check):
        """"
        This function checks if the items in the list (specified in argument) are
        present in the user's input speech.
        """
        words_of_message = speech_text.split()  # separate input string into list of strings
        if set(check).issubset(set(words_of_message)):  # set removes any duplicates from word list
            return True
        else:
            return False

    # if elif ladder to check input message
    # check until you find that your words of message contains a subset.
    if check_message(['who', 'are', 'you']):
        general_conversations.who_are_you()

    elif check_message(['how', 'i', 'look']) or check_message(['how', 'am', 'i']):
        general_conversations.how_am_i()

    elif check_message(['tell', 'joke']):
        general_conversations.tell_joke()

    elif check_message(['who', 'am', 'i']):
        general_conversations.who_am_i(name)

    elif check_message(['where', 'born']):
        general_conversations.where_born()

    elif check_message(['how', 'are', 'you']):
        general_conversations.how_are_you()

    elif check_message(['like', 'milk']):
        general_conversations.echamela()

    # Assistant tells the current time
    elif check_message(['time']):
        tell_time.what_is_time()

    # Define subject from wikipedia
    elif check_message(['define']):
        define_subject.define_subject(speech_text)

    # Shutdown the assistant
    elif check_message(['goodbye']):
        general_conversations.goodbye()
        exit(0)

    else:
        general_conversations.undefined()
